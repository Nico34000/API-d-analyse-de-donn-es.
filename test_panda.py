import json
import pandas
import pandas as pd
url = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', header = 2, names = ['id', 'Country', 'year','emission','values','footnote','source'])
#url = url.drop(url.columns[0], axis=1)

def convert_list():
    area_dict = set(url['Country'].tolist())

def choix_pays(convert_list):
    url = pandas.read_csv('co2.csv', header = 2, names = ['id', 'Country', 'year','emission','values','footnote','source'])
    data_pays = url.loc[url['Country'].isin([convert_list])].sort_values(['year'], ascending = False)
    # data_pays = (csv.sort_values(['year'], ascending=False)[result])
    res = {}
    res["Country"] = str(data_pays.iloc[0][1])
    res["year"] = int(data_pays.iloc[0][2])
    res["values"] = float(data_pays.iloc[0][4])
    return json.dumps(res)




