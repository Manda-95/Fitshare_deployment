# FitShare Project

Ce projet utilise Docker pour exécuter une application comprenant une base de données MySQL, un backend en FastAPI et un frontend en Vue.js avec Vuetify.

## Prérequis

- [Docker](https://www.docker.com/) installé sur votre machine
- [Docker Compose](https://docs.docker.com/compose/) installé

## Installation et Lancement

1. **Cloner le projet** :
   ```bash
   git clone <URL_DU_REPO>
   cd FitShare
   ```

2. **Lancer le projet avec Docker Compose** :
   ```bash
   docker-compose up --build
   ```
   - Cela démarre tous les services définis dans `docker-compose.yml`, y compris la base de données, le backend et le frontend.

3. **Accéder aux services** :
   - **Frontend** : [http://localhost:5173/](http://localhost:5173/)
   - **Backend** : [http://localhost:8000/](http://localhost:8000/)
   - **phpMyAdmin** (pour la gestion de la base de données) : [http://localhost:8080/](http://localhost:8080/)

## Initialisation des données dans la base de données

Pour mettre des données de base dans la base de données MySQL :

1. **Accéder à phpMyAdmin** :
   - Rendez-vous sur [http://localhost:8080/](http://localhost:8080/)

2. **Créer la base de données** :
   - Si la base de données `fitshare_database` n'existe pas encore, créez-la.
   - Si elle existe déjà, supprimez toutes les tables à l'intérieur pour partir d'une base propre.

3. **Importer le fichier `dump.sql`** :
   - Dans phpMyAdmin, sélectionnez la base de données `fitshare_database`.
   - Cliquez sur l'onglet **Importer**.
   - Importez le fichier `dump.sql` situé dans le dossier `db/init` du projet.

## Arrêter le projet

Pour arrêter les conteneurs Docker :
```bash
docker-compose down
```

## Notes supplémentaires

- Si vous rencontrez des problèmes, assurez-vous que vos ports (3306 pour MySQL, 8080 pour phpMyAdmin, 8000 pour le backend, et 5173 pour le frontend) ne sont pas utilisés par d'autres services sur votre machine.
- Vous pouvez également vérifier les journaux des conteneurs pour diagnostiquer les problèmes :
  ```bash
  docker-compose logs
  ```

N'hésitez pas à signaler tout problème ou question dans le dépôt du projet.
