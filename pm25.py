from sqlite3.dbapi2 import Cursor
import pandas as pd
import path
import sqlite3
six_cities = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
url = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
df = pd.read_csv(url).dropna()


def get_county_pm25(county):
    county_pm25 = df.groupby('county').get_group(
        county)[['Site', 'PM25']].values.tolist()

    return county_pm25


def get_six_pm25():
    df = pd.read_csv(url).dropna()
    six_pm25 = {}

    for city in six_cities:

        six_pm25[city] = round(df.groupby(
            'county').get_group(city)['PM25'].mean(), 2)

    return six_pm25


def get_pm25(type=0):

    columns = ['county', 'Site', 'PM25']
    values = df[columns].values.tolist()
    if type == 1:
        values = sorted(values, key=lambda x: x[-1], reverse=True)
    elif type == 2:
        values = sorted(values, key=lambda x: x[-1], reverse=False)

    return columns, values


def get_county():

    countys = []
    for county in df['county']:
        if county not in countys:
            countys.append(county)

    countys = countys[1:] + countys[0:1]
    return countys
