import json
import pandas

url = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                      'emission', 'values', 'footnote', 'source'])
# url = url.drop(url.columns[0], axis=1)


def convert_country_to_liste():
    dict_country = set(url['Country'].tolist())


def lastest_by_country(convert_country_to_liste):
    url = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                          'emission', 'values', 'footnote', 'source'])
    data_pays = url.loc[url['Country'].isin([convert_country_to_liste])].sort_values(['year'], ascending=False)
    # data_pays = (csv.sort_values(['year'], ascending=False)[result])
    res = {}
    res["Country"] = str(data_pays.iloc[0][1])
    res["year"] = int(data_pays.iloc[0][2])
    res["values"] = float(data_pays.iloc[0][4])
    return json.dumps(res)