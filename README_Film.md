# 🎬 Film Recommendation System (MovieLens 20M) 🎬

A Python-based film recommendation system built on the **MovieLens 20M dataset**, combining **content-based filtering** and **collaborative signals** to suggest relevant movies to users.

This project demonstrates how textual metadata (genres) and user ratings can be combined to generate personalized movie recommendations using classical machine learning techniques.

---

## Overview

The system recommends movies by analyzing:

- **Movie genres** using TF-IDF vectorization and cosine similarity
- **User ratings behavior**, focusing on highly rated movies (ratings ≥ 4.0)
- **Popularity fallback**, when user history is unavailable

It is designed to be simple, interpretable, and easy to extend for learning or experimentation purposes.

---

## Recommendation Strategy

The recommendation logic follows a hybrid approach:

1. **Cold start users**  
   If a user has no ratings, the system recommends the most popular movies based on rating count.

2. **User preference detection**  
   The user's favorite movie is identified as the one with the highest rating.

3. **Collaborative signal**  
   Other users who rated the same movie highly are identified, and their favorite movies are used as candidates.

4. **Content-based ranking**  
   Movie genres are vectorized using **TF-IDF**, and recommendations are ranked using **cosine similarity**.

5. **Fallback mechanism**  
   If collaborative candidates are unavailable, the system falls back to pure content-based recommendations.

---

## Project Structure

```
Film-Recommendation-System/
├── movie.csv            # Movie metadata (movieId, title, genres)
├── rating.csv           # User ratings (userId, movieId, rating)
├── recommendation.py    # Main recommendation logic
└── README.md            # Project documentation
```

---

## Dataset

This project uses the **MovieLens 20M dataset**, which contains:

- 20 million ratings
- 27,000+ movies
- 138,000+ users

Genres are preprocessed by removing separators and formatting inconsistencies before vectorization.

Dataset source:
- https://grouplens.org/datasets/movielens/

The dataset can be downloaded automatically using KaggleHub.

---

## Requirements

Python **3.8+** is recommended.

Install dependencies:

```bash
pip install pandas scikit-learn kagglehub
```

Libraries used:

- **Pandas** – data loading and manipulation  
- **Scikit-learn** – TF-IDF vectorization and cosine similarity  
- **KaggleHub** – dataset download utility  

---

## Usage

### 1. Download the Dataset (Optional)

Uncomment the following lines in the code to download the MovieLens dataset automatically:

```python
path = kagglehub.dataset_download("grouplens/movielens-20m-dataset")
print("Path to dataset files:", path)
```

Ensure `movie.csv` and `rating.csv` are accessible in the working directory.

---

### 2. Generate Recommendations

Use the `recommendation` function:

```python
recommendation(user_id, top=5)
```

Example:

```python
recommendation(15, top=5)
```

This returns a list of movie titles recommended for the specified user.

---

## Core Techniques Used

- **TF-IDF Vectorization** on movie genres
- **Cosine Similarity** for content comparison
- **User-based filtering** using high-rating overlap
- **Popularity-based fallback** for cold-start scenarios

These techniques ensure recommendations remain meaningful even with sparse user data.

---


---

# Version Française

---

# 🎬 Système de Recommandation de Films (MovieLens 20M) 🎬

Un système de recommandation de films basé sur Python, construit sur le **jeu de données MovieLens 20M**, combinant le **filtrage basé sur le contenu** et les **signaux collaboratifs** pour suggérer des films pertinents aux utilisateurs.

Ce projet démontre comment les métadonnées textuelles (genres) et les évaluations des utilisateurs peuvent être combinées pour générer des recommandations de films personnalisées en utilisant des techniques classiques d'apprentissage automatique.

---

## Présentation

Le système recommande des films en analysant :

- **Les genres de films** en utilisant la vectorisation TF-IDF et la similarité cosinus
- **Le comportement d'évaluation des utilisateurs**, en se concentrant sur les films très bien notés (notes ≥ 4.0)
- **Le repli sur la popularité**, lorsque l'historique de l'utilisateur n'est pas disponible

Il est conçu pour être simple, interprétable et facile à étendre à des fins d'apprentissage ou d'expérimentation.

---

## Stratégie de Recommandation

La logique de recommandation suit une approche hybride :

1. **Utilisateurs en démarrage à froid**  
   Si un utilisateur n'a pas d'évaluations, le système recommande les films les plus populaires basés sur le nombre d'évaluations.

2. **Détection des préférences utilisateur**  
   Le film préféré de l'utilisateur est identifié comme celui avec la note la plus élevée.

3. **Signal collaboratif**  
   Les autres utilisateurs ayant attribué une note élevée au même film sont identifiés, et leurs films préférés sont utilisés comme candidats.

4. **Classement basé sur le contenu**  
   Les genres de films sont vectorisés en utilisant **TF-IDF**, et les recommandations sont classées par **similarité cosinus**.

5. **Mécanisme de repli**  
   Si les candidats collaboratifs ne sont pas disponibles, le système se replie sur des recommandations purement basées sur le contenu.

---

## Structure du Projet

```
Film-Recommendation-System/
├── movie.csv            # Métadonnées des films (movieId, title, genres)
├── rating.csv           # Évaluations des utilisateurs (userId, movieId, rating)
├── recommendation.py    # Logique principale de recommandation
└── README.md            # Documentation du projet
```

---

## Jeu de Données

Ce projet utilise le **jeu de données MovieLens 20M**, qui contient :

- 20 millions d'évaluations
- Plus de 27 000 films
- Plus de 138 000 utilisateurs

Les genres sont prétraités en supprimant les séparateurs et les incohérences de formatage avant la vectorisation.

Source du jeu de données :
- https://grouplens.org/datasets/movielens/

Le jeu de données peut être téléchargé automatiquement en utilisant KaggleHub.

---

## Prérequis

Python **3.8+** est recommandé.

Installez les dépendances :

```bash
pip install pandas scikit-learn kagglehub
```

Bibliothèques utilisées :

- **Pandas** – chargement et manipulation des données  
- **Scikit-learn** – vectorisation TF-IDF et similarité cosinus  
- **KaggleHub** – utilitaire de téléchargement de jeux de données  

---

## Utilisation

### 1. Télécharger le Jeu de Données (Optionnel)

Décommentez les lignes suivantes dans le code pour télécharger automatiquement le jeu de données MovieLens :

```python
path = kagglehub.dataset_download("grouplens/movielens-20m-dataset")
print("Chemin vers les fichiers du jeu de données:", path)
```

Assurez-vous que `movie.csv` et `rating.csv` sont accessibles dans le répertoire de travail.

---

### 2. Générer des Recommandations

Utilisez la fonction `recommendation` :

```python
recommendation(user_id, top=5)
```

Exemple :

```python
recommendation(15, top=5)
```

Cela retourne une liste de titres de films recommandés pour l'utilisateur spécifié.

---

## Techniques Principales Utilisées

- **Vectorisation TF-IDF** sur les genres de films
- **Similarité Cosinus** pour la comparaison de contenu
- **Filtrage basé sur l'utilisateur** utilisant le chevauchement des notes élevées
- **Repli basé sur la popularité** pour les scénarios de démarrage à froid

Ces techniques assurent que les recommandations restent pertinentes même avec des données utilisateur clairsemées.

---