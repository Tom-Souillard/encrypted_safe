## English
___

# Deployment Process for encrypted_safe

## Overview
This document outlines the deployment process for the encrypted_safe application. The application is built using Python, Flask for the web framework, and SQLAlchemy for database interactions. It is containerized using Docker, which simplifies the deployment across different environments. The continuous integration and deployment pipeline is managed through GitHub Actions.

## Prerequisites
Before proceeding with the deployment, ensure that the following requirements are met:
- **Docker** is installed on the deployment server.
- **Git** is installed on the deployment server.
- Access to the **GitHub repository** where the encrypted_safe project is hosted.
- Proper **environment variables** are set up (e.g., database credentials, API keys).

## Deployment Steps

### 1. Environment Setup
Ensure that the production environment is prepared for deployment:
- **Security**: Confirm that all operating system and software patches are up-to-date to minimize vulnerabilities.
- **Networking**: Configure necessary firewall rules to allow traffic to the required ports (default: 5000 for Flask).
- **Dependencies**: Install Docker and Docker Compose if multi-container deployment is needed.

### 2. Clone Repository
Clone the encrypted_safe repository from GitHub to the local environment on the deployment server:
```bash
git clone https://github.com/Tom-Souillard/encrypted_safe.git
cd encrypted_safe
```

### 3. Configure Environment Variables
Set up the necessary environment variables or use a `.env` file to configure:
- Database URLs
- Secret keys
- Any third-party API credentials

Example of setting environment variables in the shell:
```bash
export DATABASE_URL="postgresql://user:password@localhost/dbname"
export SECRET_KEY="your_secret_key"
```

### 4. Build Docker Image
Build the Docker image using the Dockerfile provided in the repository. This will install all the Python dependencies and package the application.
```bash
docker build -t encrypted_safe .
```

### 5. Run the Docker Container
Deploy the application by running it in a Docker container:
```bash
docker run -d -p 5000:5000 --env-file .env encrypted_safe
```
This command will start the application in detached mode, binding it to port 5000 on the host.

### 6. Verify Deployment
After deployment, verify that the application is running correctly:
- **Health Check**: Navigate to `http://server-ip:5000/health` to check the health endpoint that should return a status code of 200.
- **Functionality Check**: Test key functionalities to ensure that everything operates as expected.

### 7. Enable Continuous Deployment (Optional)
Set up a CI/CD pipeline using GitHub Actions to automate the deployment process. Configure GitHub Actions to listen for push events to the main branch and trigger the workflow to rebuild and redeploy the application:
```yaml
# Example GitHub Actions setup
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Build and Push Docker image
      run: |
        docker build -t encrypted_safe .
        docker push encrypted_safe
    - name: Deploy
      run: |
        docker pull encrypted_safe
        docker run -d -p 5000:5000 encrypted_safe
```

## Rollback Procedure
In case of a failed deployment, ensure that you have a rollback plan:
- **Backup**: Always keep backups of databases and important configurations.
- **Previous Docker Images**: Keep previous Docker images for quick rollback.

## Maintenance and Monitoring
- **Logs**: Regularly check application and server logs for any unusual activity.
- **Updates**: Regularly update the application and its dependencies to patch any vulnerabilities.

## Conclusion
This deployment process is designed to ensure a consistent, secure, and maintainable deployment pipeline for the encrypted_safe application, leveraging Docker and GitHub Actions for efficiency and scalability.

___
## Français 
___
# Processus de déploiement pour encrypted_safe

## Vue d'ensemble
Ce document décrit le processus de déploiement de l'application encrypted_safe. L'application est construite avec Python, utilise Flask comme framework web, et SQLAlchemy pour les interactions avec la base de données. Elle est conteneurisée avec Docker, ce qui simplifie le déploiement dans différents environnements. Le pipeline d'intégration continue et de déploiement est géré via GitHub Actions.

## Prérequis
Avant de procéder au déploiement, assurez-vous que les exigences suivantes sont remplies :
- **Docker** est installé sur le serveur de déploiement.
- **Git** est installé sur le serveur de déploiement.
- Accès au **dépôt GitHub** où le projet encrypted_safe est hébergé.
- Les **variables d'environnement** appropriées sont configurées (ex. : identifiants de base de données, clés API).

## Étapes du déploiement

### 1. Configuration de l'environnement
Assurez-vous que l'environnement de production est prêt pour le déploiement :
- **Sécurité** : Confirmez que tous les correctifs du système d'exploitation et des logiciels sont à jour pour minimiser les vulnérabilités.
- **Réseau** : Configurez les règles du pare-feu nécessaires pour permettre le trafic vers les ports requis (par défaut : 5000 pour Flask).
- **Dépendances** : Installez Docker et Docker Compose si un déploiement multi-conteneurs est nécessaire.

### 2. Clonage du dépôt
Clonez le dépôt encrypted_safe de GitHub dans l'environnement local sur le serveur de déploiement :
```bash
git clone https://github.com/Tom-Souillard/encrypted_safe.git
cd encrypted_safe
```

### 3. Configuration des variables d'environnement
Configurez les variables d'environnement nécessaires ou utilisez un fichier `.env` pour configurer :
- URLs de la base de données
- Clés secrètes
- Identifiants de toute API tierce

Exemple de configuration des variables d'environnement dans le shell :
```bash
export DATABASE_URL="postgresql://user:password@localhost/dbname"
export SECRET_KEY="your_secret_key"
```

### 4. Construction de l'image Docker
Construisez l'image Docker en utilisant le Dockerfile fourni dans le dépôt. Cela installera toutes les dépendances Python et empaquetera l'application.
```bash
docker build -t encrypted_safe .
```

### 5. Exécution du conteneur Docker
Déployez l'application en la lançant dans un conteneur Docker :
```bash
docker run -d -p 5000:5000 --env-file .env encrypted_safe
```
Cette commande démarrera l'application en mode détaché, en la liant au port 5000 de l'hôte.

### 6. Vérification du déploiement
Après le déploiement, vérifiez que l'application fonctionne correctement :
- **Vérification de santé** : Naviguez vers `http://adresse-du-serveur:5000/health` pour vérifier le point de terminaison de santé qui devrait retourner un code de statut 200.
- **Vérification de fonctionnalité** : Testez les fonctionnalités clés pour vous assurer que tout fonctionne comme prévu.

### 7. Activer le déploiement continu (facultatif)
Configurez un pipeline CI/CD avec GitHub Actions pour automatiser le processus de déploiement. Configurez GitHub Actions pour écouter les événements de push sur la branche principale et déclencher le workflow pour reconstruire et redéployer l'application :
```yaml
# Exemple de configuration GitHub Actions
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Build and Push Docker image
     

 run: |
        docker build -t encrypted_safe .
        docker push encrypted_safe
    - name: Deploy
      run: |
        docker pull encrypted_safe
        docker run -d -p 5000:5000 encrypted_safe
```

## Procédure de retour en arrière
En cas de déploiement échoué, assurez-vous d'avoir un plan de retour en arrière :
- **Sauvegarde** : Gardez toujours des sauvegardes des bases de données et des configurations importantes.
- **Images Docker précédentes** : Conservez les images Docker précédentes pour un retour rapide.

## Maintenance et surveillance
- **Logs** : Vérifiez régulièrement les journaux d'application et du serveur pour toute activité inhabituelle.
- **Mises à jour** : Mettez régulièrement à jour l'application et ses dépendances pour corriger toute vulnérabilité.

## Conclusion
Ce processus de déploiement est conçu pour garantir un pipeline de déploiement cohérent, sécurisé et maintenable pour l'application encrypted_safe, en tirant parti de Docker et GitHub Actions pour l'efficacité et la scalabilité.