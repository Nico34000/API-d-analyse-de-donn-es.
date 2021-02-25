import logging
from flask import Flask, abort
from functions_panda import latest_by_country, average_year, per_capi
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/latest_by_country/<country>')
def by_country(country):
    # on veut la valeur la plus récente des emissions
    # totales pour le pays demandé
    if country in country_list():
        return latest_by_country(country)
    elif country.lower()==country:
        return latest_by_country(country.capitalize())
    else:
        return abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # on cherche la moyenne des émissions totales au niveau mondial
    # pour une année demandée
    if year in year_list():
        return average_year(year)
    else:
        return abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    if country in country_list():
        return per_capi(country)
    elif country.lower()==country:
        return latest_by_country(country.capitalize())
    else:
        return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
