import logging
from flask import Flask, abort, jsonify
from functions_panda import latest_by_country, average_year, per_capi
from functions_panda import country_list, year_list
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

logging.basicConfig(
    filename='app_log.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)




@app.route('/latest_by_country/<country>')
def by_country(country):
    # on veut la valeur la plus récente des emissions
    # totales pour le pays demandé
    app.logger.info("Lancement de la fonction by_country")
    app.logger.warning(f"Acces a la route: latest_by_country/")
    if country in country_list():
        app.logger.debug(f"route demande: latest_by_country/ {country}")
        return jsonify(latest_by_country(country))
        app.logger.debug(f"Operation reussi: {country}")
    elif country.lower() == country:
        app.logger.debug(f"route demande: latest_by_country/ {country}")
        return jsonify(latest_by_country(country.capitalize()))
        app.logger.debug(f"Operation reussi: {country}")
    else:
        app.logger.error(f"la route demande n'existe pas: {country}")
        return abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # on cherche la moyenne des émissions totales au niveau mondial
    # pour une année demandée
    app.logger.warning(f"Acces a la route")
    if year in year_list():
        app.logger.debug(f"route demande :/average_by_year/ {year}")
        return jsonify(average_year(year))
    else:
        app.logger.error(f"la route demande n'existe pas: {year}")   
        return abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    app.logger.warning(f"Acces a la route")    
    if country in country_list():
        app.logger.debug(f"Route demande: /per_capita{country}")
        return jsonify(per_capi(country))
    elif country.lower() == country:
        app.logger.debug(f"route demande: /per_capita {country}")
        return jsonify(per_capi(country.capitalize()))
    else:
        app.logger.error(f"La route demande n'existe pas: {country}")
        return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
