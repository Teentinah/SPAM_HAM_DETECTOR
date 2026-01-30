## 🌐 Déploiement sur Render.com (gratuit)

### 1️⃣ Préparation du dépôt

1. Crée un dépôt Git :

```bash
git init
git add .
git commit -m "Spam detector initial"
```

2. Pousse le code sur GitHub (ou GitLab) :

```bash
git remote add origin https://github.com/ton-compte/spam-detector.git
git push -u origin main
```

---

### 2️⃣ Création du service Render

1. Va sur `https://render.com` et connecte ton compte GitHub.
2. Clique sur **New → Web Service**.
3. Sélectionne ton dépôt.
4. Render va détecter automatiquement :
   - `render.yaml` (configuration)
   - Python comme runtime

---

### 3️⃣ Fichier `render.yaml`

Ce fichier décrit le service web :
- Runtime : Python
- Commandes d’installation : `pip install -r requirements.txt`
- Commande de démarrage : `python app.py`

Tu n’as normalement rien à modifier.

---

### 4️⃣ Variables d’environnement (optionnel)

Par défaut :
- L’API écoute sur le port fourni par Render (`$PORT`)
- C’est déjà géré dans `app.py` :

```python
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
```

---

### 5️⃣ Tester l’API en ligne

Une fois le déploiement terminé, Render te donne une URL du type :

`https://ton-service.onrender.com`

Endpoints :
- `GET /health`
- `POST /predict`

Tu peux tester avec `curl`, Postman, ou adapter l’URL dans `flutter_example.dart`.

