from types import MethodDescriptorType
from flask import Flask, render_template, request, make_response
from datetime import datetime
from flask.helpers import url_for

import pandas as pd
from pm25 import get_pm25, get_six_pm25
import json

app = Flask(__name__)


@app.route('/')
def index():
    name = 'jerry'
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'name': name,
        'date': date,
    }

    return render_template('./index.html', context=context)


@app.route('/pm25-data', methods=['GET', 'POST'])
def get_pm25_json():
    columns, values = get_pm25()
    site = [data[1] for data in values]
    pm25 = [data[-1] for data in values]
    print(site, pm25)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datas = [[value[1], value[-1]]for value in values]
    datas = sorted(datas, key=lambda x: x[-1])

    data = {'columns': columns, 'site': site, 'pm25': pm25,
            'hightest': datas[-1], 'lowest': datas[0], 'date': date}
    return json.dumps(data, ensure_ascii=False)


@app.route('/pm25-charts')
def pm25_charts():

    return render_template('/pm25-charts.html')


@app.route('/six-pm25', methods=['GET', 'POST'])
def get_pm25_six_json():
    datas = get_six_pm25()
    data = {'city': list(datas.keys()), 'pm25': list(datas.values())}

    return json.dumps(data, ensure_ascii=False)


@app.route('/pm25', methods=['GET', 'POST'])
def pm25():
    if request.method == 'GET':
        print('GET')
        columns, values = get_pm25()

    if request.method == 'POST':
        if request.form.get('reverse'):
            columns, values = get_pm25(type=1)
        elif request.form.get('ascending'):
            columns, values = get_pm25(type=2)

    return render_template('./pm25.html', columns=columns, values=values)


@app.route('/stocks')
def stock():
    all_stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]

    return render_template('./stock.html', stocks=all_stocks)


@app.route('/bmi/name=<name>&height=<height>&weight=<weight>')
def get_bmi(name, height, weight):
    try:
        bmi = round(eval(weight)/(eval(height)/100)**2, 2)
        return f'{name} bmi={bmi}'

    except Exception as e:
        return str(e)


@app.route('/sum/x=<a>&y=<b>', methods=['GET'])
def get_sum(a, b):
    total = eval(a)+eval(b)
    return str(total)


@app.route('/today/<string:name>')
def get_date(name):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'{name} {date}'


if __name__ == '__main__':
    app.run(debug=True)
