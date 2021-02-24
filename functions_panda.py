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


def average_year(year):
    url = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                          'emission', 'values', 'footnote', 'source'])
    data_year = url.loc[url['year'].isin([year])]
    data_year = data_year[(data_year["emission"] == 'Emissions (thousand metric \
    tons of carbon dioxide)')]
    print(data_year)
    mean_year = data_year.mean()['values']
    result = {}
    result["year"] = year
    result["total"] = float(mean_year)
    return json.dumps(result)
  
  
def per_capi(country):
    url = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                          'emission', 'values', 'footnote', 'source'])
    capita = url.loc[url['Country'].isin([country])]
    capita = capita[(capita["emission"] == 'Emissions per capita(metric tons \
    of carbon dioxide)')]
    result = {}
    longeur = len(capita)
    for i in range(longeur):
        result[str(capita.iloc[i][2])]=float(capita.iloc[i][4])
    return json.dumps(result)




