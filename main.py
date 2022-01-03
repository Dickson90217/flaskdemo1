from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('./index.html')


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


@app.route('/today/<path:name>')
def get_date(name):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'{name} {date}'


if __name__ == '__main__':
    app.run(debug=True)
