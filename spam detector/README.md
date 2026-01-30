## Spam Detector – Python + Flask + Flutter

### 🎯 Objectif
Un petit projet complet de détection de spam basé sur :
- **TF-IDF** pour transformer le texte en nombres
- **Naive Bayes** (MultinomialNB) pour la classification
- **Flask** pour exposer une API web
- **Flutter** pour l’interface utilisateur

---

### 📁 Structure simplifiée

```
.
├── app.py               # API Flask (/health, /predict)
├── train_model.py       # Entraînement du modèle
├── test_api.py          # Script de test de l’API
├── requirements.txt     # Dépendances Python
├── GUIDE_4H.md          # Guide pédagogique
├── DEPLOYMENT.md        # Déploiement Render
├── render.yaml          # Config Render
├── flutter_example.dart # Exemple d’app Flutter
├── data/
│   └── spam_dataset.csv # Jeu de données
└── models/
    ├── spam_model.pkl   # Modèle entraîné (généré)
    └── vectorizer.pkl   # TF-IDF (généré)
```

---

### 🚀 Démarrage rapide

1. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

2. **Entraîner le modèle**

```bash
python train_model.py
```

3. **Lancer l’API**

```bash
python app.py
```

4. **Tester l’API**

```bash
python test_api.py
```

---

### 🔌 Endpoints principaux

- **GET `/health`**
  - Vérifie que l’API est en ligne.

- **POST `/predict`**
  - Corps JSON :

```json
{
  "message": "Ton texte ici"
}
```

  - Réponse JSON (exemple) :

```json
{
  "prediction": "spam",
  "label": 1,
  "confidence_spam": 97.3,
  "confidence_ham": 2.7
}
```

---

### 📱 Flutter
- Le fichier `flutter_example.dart` contient une petite app :
  - Champ texte pour le message
  - Bouton "Analyser"
  - Appel HTTP à l’API Flask
  - Affichage du résultat et du score de confiance

Adapte simplement l’URL de l’API (localhost en dev, Render en prod).

---

### 🌐 Déploiement
- Voir `DEPLOYMENT.md` pour un déploiement gratuit sur Render.com
- Le fichier `render.yaml` automatise la configuration (build + start command).

