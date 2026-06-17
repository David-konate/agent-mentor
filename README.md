# 🧑‍🏫 Mentor Senior — Agent IA pédagogique pour la formation CDA

Un agent IA qui joue le rôle d'un **développeur senior** auprès de **développeurs juniors**,
en respectant strictement une convention pédagogique (méthode TCREI, Test de Maîtrise,
limites par techno, sécurité des données).

> **Règle d'or :** l'IA réduit le temps de *recherche*, jamais le temps de *compréhension*.

---

## 🏗️ Architecture

```
Navigateur (front)              Serveur o2switch (back)         API externe
┌──────────────────┐  fetch    ┌──────────────────────┐        ┌──────────┐
│ HTML / CSS / JS  │ ────────► │ Python + Flask        │ ─────► │  Gemini  │
│   (vanilla)      │ ◄──────── │ + convention (prompt) │ ◄───── │ (gratuit)│
└──────────────────┘   JSON    └──────────────────────┘        └──────────┘
```

La **clé API reste côté serveur** : le navigateur ne la voit jamais. ✅

## 📁 Structure du projet

| Fichier | Rôle |
|---|---|
| `prompt.py` | **Le cerveau** : la convention (Articles 1-5) traduite en consignes pour l'IA |
| `gemini_client.py` | Appel à l'API Gemini |
| `app.py` | Serveur Flask : sert le front + route `/api/chat` |
| `passenger_wsgi.py` | Point d'entrée pour o2switch (Passenger) |
| `front/` | L'interface de chat (HTML/CSS/JS) |
| `requirements.txt` | Dépendances Python |
| `.env.example` | Modèle de configuration (à copier en `.env`) |

---

## 💻 Lancer en local (sur ta machine)

```powershell
# 1. Se placer dans le dossier
cd agent-mentor-cda

# 2. Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer la clé API
copy .env.example .env
# puis ouvrir .env et coller ta clé Gemini (https://aistudio.google.com/apikey)

# 5. Lancer
python app.py
```

Ouvre ensuite **http://127.0.0.1:5000** dans ton navigateur.

---

## 🚀 Déploiement sur o2switch

1. **Uploader les fichiers** dans un dossier de ton compte (ex: `~/mentor-cda/`)
   via le gestionnaire de fichiers cPanel ou FTP.
2. Dans cPanel, ouvrir **« Setup Python App »** :
   - **Application root** : `mentor-cda`
   - **Application URL** : le domaine/sous-domaine voulu
   - **Application startup file** : `passenger_wsgi.py`
   - **Application Entry point** : `application`
3. Cliquer **Create**, puis dans la même page :
   - Section **Configuration files** → ajouter `requirements.txt` et cliquer **Run Pip Install**.
   - Section **Environment variables** → ajouter :
     - `GEMINI_API_KEY` = ta clé
     - `GEMINI_MODEL` = `gemini-2.0-flash` (optionnel)
4. Cliquer **Restart**. L'application est en ligne. 🎉

> ⚠️ Ne mets jamais ta clé API dans le code ni dans un fichier commité.
> Sur o2switch, elle vit dans les *Environment variables* de cPanel.

---

## 🎓 Pour la soutenance — points à valoriser

- **Séparation front/back** et pourquoi le Python ne descend pas dans le navigateur.
- **Sécurité** : clé API côté serveur uniquement, jamais exposée au client.
- **Le system prompt** (`prompt.py`) comme implémentation concrète de la convention.
- **Le mode Tuteur/Copilote** qui matérialise l'Article 4 (formation → entreprise).
- **Le Test de Maîtrise** posé en fin de réponse comme garde-fou pédagogique.
