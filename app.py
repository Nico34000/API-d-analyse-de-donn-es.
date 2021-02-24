import logging
from flask import Flask
from functions_panda import latest_by_country, average_year, per_capi
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    # utilisé pour tester si l'app fonctionne bien
    return "hello world"


@app.route('/latest_by_country/<country>')
def by_country(country):
    # on veut la valeur la plus récente des emissions
    # totales pour le pays demandé
    # logging.debug(f"Pays demandé : {country}")
    return latest_by_country(country)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # on cherche la moyenne des émissions totales au niveau mondial
    # pour une année demandée
    return average_year(year)
    # logging.debug(f"Année demandée : {year}")
    # if year=="1975":
    #     return json.dumps({"year":"1975", "total":12333555.9})
    # else:
    #     abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    # logging.debug(f"Pays demandé : {country}")
    return per_capi(country)


if __name__ == "__main__":
    app.run(debug=True)
