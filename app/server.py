"""Importez les bibliothèques nécessaires :
time pour la gestion du temps.
os pour effectuer des opérations sur le système d'exploitation.
cheroot.wsgi pour le serveur WSGI CherryPy."""
import cherrypy, sys
from app import create_app
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

conf = SparkConf().setAppName("movie_reco-server")
sc = SparkContext(conf=conf, pyFiles=['engine.py', 'app.py'])

# Obtenez les chemins des jeux de données des films et des évaluations à partir des arguments de la ligne de commande
movies_set_path = sys.argv[1] if len(sys.argv) > 1 else ""
ratings_set_path = sys.argv[2] if len(sys.argv) > 2 else ""

# Créez l'application Flask :
app = create_app(sc, movies_set_path, ratings_set_path)

"""
# Configurez et démarrez le serveur CherryPy :
cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 5432, 'engine.autoreload.on': False})
cherrypy.engine.start()"""