## 🧭 Guide 4H – Projet Spam Detector (Python + Flask + Flutter)

### 0️⃣ Pré-requis
- **Python 3.9+** installé
- `pip` fonctionnel
- Un éditeur de code (VS Code, PyCharm, etc.)

Arborescence dans ce dossier :

```
.
├── app.py
├── train_model.py
├── test_api.py
├── requirements.txt
├── GUIDE_4H.md
├── README.md
├── DEPLOYMENT.md
├── render.yaml
├── flutter_example.dart
├── data/
│   └── spam_dataset.csv
└── models/
    ├── spam_model.pkl        (généré après entraînement)
    └── vectorizer.pkl        (généré après entraînement)
```

---

### 1️⃣ Heure 1 – Installation & prise en main

1. Ouvrir un terminal dans ce dossier.
2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

3. Ouvrir `train_model.py` et lire les grandes étapes :
   - Chargement des données
   - Séparation train/test
   - TF-IDF + Naive Bayes
   - Sauvegarde du modèle

4. Ouvrir `data/spam_dataset.csv` pour voir quelques exemples de messages.

---

### 2️⃣ Heure 2 – Entraîner le modèle & comprendre la sortie

Dans le terminal :

```bash
python train_model.py
```

Ceci va :
- Charger le CSV
- Entraîner le modèle
- Afficher la **précision** et un **rapport de classification**
- Sauvegarder `models/spam_model.pkl` et `models/vectorizer.pkl`

Note les points suivants :
- Précision (par ex. ~95 %)
- Où le modèle se trompe (voir le rapport)

---

### 3️⃣ Heure 3 – API Flask + tests

1. Lancer l’API :

```bash
python app.py
```

2. Dans un autre terminal, tester :

```bash
python test_api.py
```

3. Comprendre les endpoints :
- `GET /health` → Vérification que l’API tourne
- `POST /predict` → Corps JSON `{"message": "ton texte ici"}`

4. Regarder le JSON de sortie :
   - `prediction` : `"spam"` ou `"ham"`
   - `confidence_spam` / `confidence_ham` : score en %

---

### 4️⃣ Heure 4 – Flutter + déploiement

1. Ouvrir `flutter_example.dart`.
2. Repérer :
   - L’URL de l’API (à adapter : localhost ou Render)
   - Le champ texte + bouton
   - L’affichage du résultat (spam / ham + confiance)
3. Intégrer ce code dans ton projet Flutter existant.

4. Pour le déploiement, lire `DEPLOYMENT.md` (Render.com).

---

### ✅ Checklist finale
- [ ] `pip install -r requirements.txt` exécuté
- [ ] `python train_model.py` exécuté sans erreur
- [ ] `models/spam_model.pkl` et `models/vectorizer.pkl` présents
- [ ] `python app.py` lance l’API sans erreur
- [ ] `python test_api.py` renvoie une prédiction
- [ ] Exemple Flutter adapté et connecté à l’API
- [ ] Déploiement configuré sur Render (optionnel)

