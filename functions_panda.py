import json
import pandas


def csv_file():
    csv = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                          'emission', 'values', 'footnote', 'source'])
    return csv


def country_list():
    df = csv_file()
    country_list = set(df['Country'].tolist())
    return country_list


def latest_by_country(country):
    df = csv_file()
    df = df.loc[df['Country'].isin([country])].sort_values(['year'],
                                                           ascending=False)
    result = {}
    result["country"] = str(df.iloc[0][1])
    result["year"] = int(df.iloc[0][2])
    result["emissions"] = float(df.iloc[0][4])
    return result


def year_list():
    df = csv_file()
    list_year = set(df['year'].tolist())
    return list_year


def average_year(year):
    df = csv_file()
    df = df.loc[df['year'].isin([year])]
    df = df[(df["emission"] == 'Emissions \
(thousand metric tons of carbon dioxide)')]
    mean_year = df.mean()['values']
    result = {}
    result["year"] = year
    result["total"] = float(mean_year)
    return result


def per_capi(country):
    df = csv_file()
    df = df.loc[df['Country'].isin([country])]
    df = df[(df["emission"] == 'Emissions \
per capita (metric tons of carbon dioxide)')]
    result = {}
    longeur = len(df)
    for i in range(longeur):
        result[int(df.iloc[i][2])] = float(df.iloc[i][4])
    return result
