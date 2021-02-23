import json
import pandas
import pandas as pd
url = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', header = 2, names = ['id', 'Country', 'year','emission','values','footnote','source'])
#url = url.drop(url.columns[0], axis=1)

csv = pd.DataFrame(url)

def choix_pays(csv):
    data_pays = csv.loc[csv['Country']].sort_values(by = 'year', ascending = False)
    # data_pays = (csv.sort_values(['year'], ascending=False)[result])
    res = {}
    res["Country"] = str(data_pays.iloc[0][1])
    res["year"] = int(data_pays.iloc[0][2])
    res["values"] = float(data_pays.iloc[0][4])
    print (json.dumps(res))
    # print([data_pays.iloc[0:1]])
    #return (csv[['Country','year', 'values']][result], [result_2])
choix_pays(csv)


# def max_values(csv,choix_pays):
#     column = csv["values"]
#     max_value = column.max()
#     print(max_value)

# max_values(csv, choix_pays)

