



Les émissions de CO2 pour les pays sont disponibles sur un fichier csv fournit sur le site de l'ONU avec differentes pays en differentes années.  On les affiche en format JSON et 
pour obtenir le resultat voulu , on tape le localhost et on lance chaque requête  pour voir le résultat

Pour pouvoir lancer l'application vous devez télécharger tout les fichiers contenu dans le repo.
Vous allez pouvoir lancer via le script bat : "autorun_test_api.bat" et suivre les instructions.
Tout fonctionne bien ? Parfait vous allez donc pouvoir effectuer vos rêquetes en changeant la route de l'adresse : 

Exemple : http://127.0.0.1:5000/latest_by_country/France

Exemple : http://127.0.0.1:5000/average_by_year/2016

Exemple : http://127.0.0.1:5000/per_capita/Albania

-------------------------------------------------------------------------------------------------------------------------------------------------------
FONCTION DISPONIBLE



-Latest by country :  elle nous donne la valeur plus recente  d'émissions de CO2 pour un pays demandé par l'utilisateur.

-Average by year :  elle nous affiche la valeur moyenne des émissions totale de CO2  pour une année demandé par l'utilisateur.

-Per capita : elle nous affiche les émissions de CO2 de toutes les années  d'un pays demandé par l'utilisateur.
