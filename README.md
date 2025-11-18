# 🎯 Quiz Django Interactive

Une application de quiz interactive en temps réel avec mode solo et duel, thème sombre, et timer de 15 secondes par question.

## ✨ Caractéristiques

- **🎮 Mode Solo**: 10 questions aléatoires avec feedback immédiat
- **⚔️ Mode Duel**: 2 joueurs alternent, voir qui gagne
- **⏱️ Timer**: 15 secondes par question avec auto-submit
- **🎨 Design**: Thème noir/gris professionnel, responsive mobile
- **📚 36 Questions**: 7 thèmes, 3 niveaux de difficulté
- **📊 Explications**: Chaque réponse a une explication pédagogique

## 🛠️ Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes

```bash
# 1. Cloner ou télécharger le projet
cd projet_final

# 2. Créer un environnement virtuel
python -m venv .venv

# 3. Activer l'environnement
# Sur Windows:
.venv\Scripts\Activate.ps1
# Sur Mac/Linux:
source .venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Faire les migrations (créer la BD)
python manage.py migrate

# 6. Lancer le serveur
python manage.py runserver
```

## 🚀 Utilisation

1. **Ouvrir le navigateur**: http://127.0.0.1:8000/
2. **Choisir un mode**:
   - **Solo**: Répondre à 10 questions aléatoires
   - **Duel**: Affronter quelqu'un dans un quiz
3. **Sélectionner un thème** (optionnel)
4. **Répondre aux questions** en 15 secondes par question
5. **Voir les résultats** avec le score final

## 📁 Structure du projet

```
projet_final/
├── manage.py                 # Commandes Django
├── requirements.txt          # Dépendances
├── README.md                 # Ce fichier
├── TUTORIEL.md              # Guide d'apprentissage complet
│
├── quizsite/                # Configuration principale
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── quiz/                    # Application principale
│   ├── models.py           # Modèle Question
│   ├── views.py            # Logique (solo, duel)
│   ├── urls.py             # Routes
│   ├── templates/quiz/
│   │   ├── base.html       # Layout commun
│   │   ├── index.html      # Accueil
│   │   ├── round.html      # Mode solo
│   │   └── duel.html       # Mode duel
│   └── static/quiz/
│       └── styles.css      # Styles (thème noir/gris)
│
└── db.sqlite3              # Base de données
```

## 🎓 Concepts clés

Pour comprendre comment fonctionne cette application, lisez **[TUTORIEL.md](./TUTORIEL.md)** qui explique:

- 🏗️ Architecture Django (Models, Views, Templates)
- 🗄️ Base de données (ORM, Queries)
- 🌐 HTTP et Sessions
- 🎨 CSS et Responsive Design
- ⏱️ JavaScript et Timer
- 🔄 Flux de l'application

## 🎮 Thèmes disponibles

- 📚 Géographie
- 📖 Histoire
- 🔬 Science
- 🧮 Mathématiques
- 🧬 Biologie
- 🎭 Art
- 💻 Technologie

## 🔧 Admin Panel

Pour ajouter des questions:

```bash
# Créer un compte admin
python manage.py createsuperuser

# Aller sur http://127.0.0.1:8000/admin/
# Se connecter et ajouter des questions
```

## 📊 Statistiques

- **Total questions**: 36
- **Thèmes**: 7
- **Niveaux**: Facile, Moyen, Difficile
- **Questions par round**: 10 (aléatoires)
- **Temps par question**: 15 secondes

## 🎯 Fonctionnalités avancées

- ✅ Sélection aléatoire de questions
- ✅ Feedback immédiat avec explications
- ✅ Score en temps réel
- ✅ Mode duel avec alternance de joueurs
- ✅ Barre de progression
- ✅ Timer circulaire avec animation
- ✅ Thèmes visuels multiples
- ✅ Responsive design (mobile/desktop)

## 🚀 Prochaines améliorations possibles

- Système de score persistant (sauvegarde en BD)
- Leaderboard global
- Mode multijoueur en ligne (WebSockets)
- Système de badges/achievements
- Export PDF des résultats
- Difficulté personnalisable

## 📝 Technologies utilisées

| Tech | Usage |
|------|-------|
| **Python** | Langage backend |
| **Django 4.2** | Framework web |
| **SQLite** | Base de données |
| **HTML 5** | Structure pages |
| **CSS 3** | Styles et responsive |
| **JavaScript** | Timer et interactivity |

## 🤝 Contribution

Ce projet est open source! Pour contribuer:
1. Ajouter des questions dans `populate_db_extended.py`
2. Améliorer le CSS dans `quiz/static/quiz/styles.css`
3. Ajouter des fonctionnalités dans `quiz/views.py`

## 📞 Support

En cas de problème:
1. Vérifier que Python et pip sont installés
2. Vérifier que le venv est activé
3. Relancer le serveur avec `python manage.py runserver`
4. Lire le [TUTORIEL.md](./TUTORIEL.md) pour plus de détails

## 📜 Licence

Ce projet est libre d'utilisation à titre éducatif.

---

**Prêt à tester? Lancez le serveur et amusez-vous! 🎮**

