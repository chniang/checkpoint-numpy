# 📊 Analyse des Notes Étudiantes avec NumPy

## 🎯 Objectif

Ce projet a pour but de mettre en pratique l'utilisation de la bibliothèque **NumPy** afin d'effectuer une analyse statistique d’un ensemble de données représentant les notes d’étudiants. L’objectif est de :

- Calculer des mesures statistiques (moyenne, médiane, écart type)
- Identifier des tendances
- Extraire des sous-ensembles significatifs
- Comprendre la distribution des performances dans une échelle de notation donnée

---

## 🧪 Données Utilisées

```python
grades = [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]
🛠️ Fonctionnalités
Le script Python utilise NumPy pour effectuer les opérations suivantes :

✅ Création d’un tableau grades avec NumPy

✅ Calcul de la moyenne, de la médiane et de l’écart type

✅ Détermination du maximum et du minimum

✅ Identification de l’indice de la note la plus élevée

✅ Comptage des étudiants ayant une note supérieure à 90

✅ Calcul du pourcentage d'étudiants ayant une note > 90

✅ Création d’un tableau passing_grades contenant toutes les notes supérieures à 75

✅ Impression de tous les résultats

📦 Technologies
Python

NumPy

📁 Structure du projet

checkpoint-numpy/
│
├── main.py           # Script principal contenant l'analyse NumPy
├── README.md         # Ce fichier
└── .gitignore        # Fichiers à ignorer par Git (optionnel)
▶️ Exécution
Assurez-vous d'avoir installé NumPy :

pip install numpy
Exécutez le fichier principal :

python main.py
✅ Résultats attendus
Le programme affichera :

Moyenne, médiane et écart type des notes

Note la plus élevée et la plus basse

Indice de la note la plus élevée

Nombre et pourcentage de notes supérieures à 90

Tableau des notes supérieures à 75 (passing_grades)

📌 Remarques
Pour extraire les données :

python

grades[grades > 90]      # Pour les notes supérieures à 90
grades[grades > 75]      # Pour les notes supérieures à 75
np.mean(grades > 90) * 100  # Pourcentage d’étudiants > 90
👨‍💻 Auteur
Cheikh Niang – Certifié Python & Data Science – Formation GoMyCode
GitHub : @chniang

📃 Licence
Ce projet est à usage éducatif. Libre à vous de le réutiliser ou le modifier.
