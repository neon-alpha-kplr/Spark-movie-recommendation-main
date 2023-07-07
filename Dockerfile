# Utilisez une image de base contenant Python et Spark
FROM apache/spark:3.4.0
# Définissez le répertoire de travail de l'application
WORKDIR /app
# Install any additional dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
# Installez les dépendances requises
RUN pip3 install -r requirements.txt
# Copie tous les fichiers et répertoires du répertoire de construction vers le répertoire de travail du conteneur.
COPY ./app /app
COPY ./requirements.txt  /app
COPY ./app/ml-latest /ml-latest
# Exposez le port sur lequel l'application Flask sera exécutée
EXPOSE 5432
# Démarrez l'application Flask
CMD ["spark-submit", "server.py", "ml-latest/movies.csv", "ml-latest/ratings.csv"]