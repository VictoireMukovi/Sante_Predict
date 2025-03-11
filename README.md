PrédicSanté - Système Intelligent de Prédiction des Maladies
PrédicSanté est un projet académique développé par les étudiants de l’Université Adventiste de Lukanga (UNILUK) au sein du Groupe GACI, en collaboration avec l’ISTM-L. Ce système intelligent utilise l’apprentissage automatique pour prédire deux maladies majeures : le diabète et les maladies cardiaques.

Description du projet
Ce projet couvre l’intégralité du cycle de vie d’un modèle prédictif en santé, comprenant :

L'exploration des datasets : Analyse préliminaire et compréhension des données issues de bases publiques de santé.

Le prétraitement des données : Nettoyage, traitement des valeurs manquantes, normalisation et sélection des variables pertinentes.

L’entraînement des modèles : Création et apprentissage de deux modèles distincts pour la prédiction du diabète et des maladies cardiaques, basés sur des algorithmes d’apprentissage supervisé.

La validation des modèles : Évaluation rigoureuse des performances des modèles à l’aide de métriques adaptées (précision, rappel, courbe ROC, etc.).

La sauvegarde des modèles : Export des modèles entraînés au format .sav pour réutilisation ultérieure.

Le développement d’une interface utilisateur : Mise en place d’une application web interactive avec Streamlit permettant aux utilisateurs de tester facilement les modèles en saisissant leurs données personnelles et en obtenant une prédiction immédiate.

Fonctionnalités principales
Prédiction personnalisée du risque de diabète.

Prédiction personnalisée du risque de maladies cardiaques.

Interface intuitive et responsive pour faciliter l’utilisation.

Validation des entrées utilisateur pour garantir la qualité des données saisies.

Technologies utilisées
Python (pandas, scikit-learn, pickle)

Streamlit (interface web)

Bibliothèques standard pour le traitement des données

Utilisation
Cloner le dépôt.

Installer les dépendances via pip install -r requirements.txt.

Lancer l’application Streamlit avec la commande :
streamlit run app.py

Saisir les informations demandées dans l’interface pour obtenir une prédiction.

