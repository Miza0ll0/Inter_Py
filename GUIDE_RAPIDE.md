# 🚀 Guide Rapide: Comment fonctionne le Quiz

Une explication super simple et visuelle.

---

## 📱 Ce que voit l'utilisateur

### Étape 1: Accueil
```
┌─────────────────────────────┐
│   🎯 Quiz Interactive       │
├─────────────────────────────┤
│ 🎯 Mode Solo                │
│ Testez vos connaissances    │
│ [Choisir un thème ▼]        │
│ [Démarrer le quiz solo]     │
│                             │
│ ⚔️ Mode Duel                │
│ Affrontez un adversaire     │
│ [Joueur 1: ______]          │
│ [Joueur 2: ______]          │
│ [Choisir un thème ▼]        │
│ [Démarrer le duel]          │
└─────────────────────────────┘
```

### Étape 2: Question
```
┌─────────────────────────────┐
│ Question 3 / 10             │
│ ████░░░░░░░░░░░░░░░░░░░░░░ │
│                             │
│ ⏱️  15 (Timer circulaire)    │
│                             │
│ Quelle est la capitale?     │
│ ○ Paris                     │
│ ○ Lyon                      │
│ ○ Marseille                 │
│ ○ Nice                      │
│                             │
│ [Valider la réponse]        │
└─────────────────────────────┘
```

### Étape 3: Feedback
```
┌─────────────────────────────┐
│ Question 3 / 10             │
│                             │
│ Quelle est la capitale?     │
│                             │
│ ✓ Bonne réponse!           │
│ Réponse: Paris              │
│ Explication: Paris est...   │
│                             │
│ [Question suivante →]       │
└─────────────────────────────┘
```

### Étape 4: Résultats
```
┌─────────────────────────────┐
│ 🎉 Round terminé!           │
│                             │
│ Score final                 │
│ 7/10                        │
│ 70% de réussite             │
│                             │
│ [Retour à l'accueil]        │
└─────────────────────────────┘
```

---

## 🧠 Comment ça marche dans le serveur

### **Le serveur Django c'est quoi?**

C'est comme un serveur de restaurant:

```
Toi (Client)              Django (Serveur)
    |                           |
    | "Je veux la question 3"   |
    |-------------------------->|
    |                     Cherche dans la BD
    |                     Question 3: "Quelle capitale?"
    |                     Rend la page HTML
    |<-------------------------|
    | "Voilà ta question"       |
    | Page HTML s'affiche       |
    |                           |
    | Réponds: "Paris"          |
    |-------------------------->|
    |                     Vérifie: Paris = correct ✓
    |                     Score = Score + 1
    |                     Rend la page de feedback
    |<-------------------------|
    | "Bravo! Réponse correcte" |
```

---

## 📊 Structure simple de Django

```
Django = 3 parties

1. Models (BD)           2. Views (Logique)      3. Templates (HTML)
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ class Question   │   │ def quiz_round() │   │ <h1>Question</h1>│
│ ├─ text          │   │  - Reçoit réponse│   │ <form>...        │
│ ├─ choice_a      │   │  - Vérifie        │   │ {% for %}...     │
│ ├─ correct       │   │  - Augmente score│   │ </form>          │
│ └─ theme         │   │  - Rend template│   └──────────────────┘
└──────────────────┘   └──────────────────┘
        ↓                       ↓                      ↓
   Table: quiz_question    Logique métier        Page HTML finale
   (BD SQLite)             (Python)             (Affichée au user)
```

---

## 🔄 Cycle d'une réponse

```
1. Utilisateur
   ↓ Clique sur "Valider"
2. Navigateur
   ↓ Envoie une requête POST avec la réponse
3. Django reçoit
   ↓ Demande: "Est-ce que 'a' = correct?"
4. Models.py
   ↓ Question.objects.get(pk=1)
   ↓ if chosen == q.correct:
   ↓ score += 1
5. Views.py
   ↓ Met à jour la session
   ↓ Rend le feedback
6. Template
   ↓ Crée le HTML avec le feedback
7. Navigateur
   ↓ Affiche "✓ Bonne réponse!"
```

---

## 🎲 Sélection aléatoire

### **Comment les 10 questions sont choisies?**

```
BD: [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, ..., Q36]

Code Python:
    selected = sample([1, 2, 3, ..., 36], 10)
    # Résultat: [7, 2, 34, 9, 15, 3, 28, 11, 5, 22]

Chaque round est différent! 🎲
```

---

## ⏱️ Comment marche le timer?

### **Dans le navigateur (JavaScript)**

```javascript
Chaque seconde:
1. Décrémente remainingTime (15 → 14 → 13 → ... → 0)
2. Met à jour le cercle (SVG stroke-dashoffset)
3. Change la couleur si critique (<5 sec)
4. Si remainingTime <= 0:
   - Désactive le bouton
   - Affiche "Temps écoulé..."
   - Soumet automatiquement le formulaire
```

### **Visuel**

```
15s: ◯ (cercle complet)
10s: ◐ (3/4 du cercle)
5s:  ◒ (1/2 du cercle, rouge ⚠️)
0s:  ◕ (cercle vide, formulaire envoyé)
```

---

## 🎯 Mode Solo vs Mode Duel

### **Mode Solo**

```
Question 1 [User répond] → Question 2 → ... → Question 10 → Résultat
```

Session mémoire:
```python
session['round_qs'] = [3, 7, 12, 5, 9, 2, 15, 8, 11, 4]
session['round_index'] = 0          # Quelle question?
session['score'] = 0                # Combien de points?
```

### **Mode Duel**

```
Question 1 [P1 répond] [P2 répond] → Question 2 → ... → Résultat
```

Session mémoire:
```python
session['duel_qs'] = [3, 7, 12, 5, 9, 2, 15, 8, 11, 4]
session['duel_index'] = 0           # Quelle question?
session['duel_turn'] = 'p1'         # À qui de jouer?
session['duel_scores'] = {'p1': 2, 'p2': 1}  # Score de chacun
session['duel_players'] = {'p1': 'Alice', 'p2': 'Bob'}
```

---

## 🗄️ Base de données (très simple)

### **Table: quiz_question**

| id | text | choice_a | choice_b | choice_c | choice_d | correct | theme | difficulty | explanation |
|----|------|----------|----------|----------|----------|---------|-------|------------|-------------|
| 1 | Quelle est la capitale de la France? | Paris | Lyon | Marseille | Nice | a | Géographie | easy | Paris est la capitale... |
| 2 | Quel océan est le plus grand? | Atlantique | Pacifique | Indien | Arctique | b | Géographie | easy | Le Pacifique couvre... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Requêtes courantes:**
```python
# Toutes les questions
Question.objects.all()

# Seulement Géographie
Question.objects.filter(theme='Géographie')

# Compter
Question.objects.count()  # Affiche: 36

# Obtenir une question spécifique
q = Question.objects.get(pk=1)
print(q.text)  # "Quelle est la capitale..."
```

---

## 🎨 CSS: Comment c'est stylisé?

### **Couleurs (thème sombre)**

```css
--bg: #0f1113;         /* Fond très sombre (noir) */
--panel: #141619;      /* Panel légèrement plus clair */
--text: #e6eef3;       /* Texte clair (blanc-gris) */
--accent: #6c7a89;     /* Couleur principale (gris-bleu) */
```

### **Responsive (adapté à la taille)**

```css
/* Desktop (>768px) */
.panel { width: 800px; padding: 40px; }

/* Mobile (<768px) */
@media (max-width: 768px) {
  .panel { width: 100%; padding: 20px; }
}
```

---

## 🔐 Sécurité: CSRF Token

### **Qu'est-ce que c'est?**

Un token secret pour empêcher les attaques.

```html
<form method="post">
  {% csrf_token %}  <!-- ← Token de sécurité caché -->
  <input type="radio" name="choice" value="a">
  <button>Valider</button>
</form>
```

**Sans ce token**, quelqu'un pourrait créer une fausse page pour "pirater" vos réponses.

---

## 📈 Exemple complet: Répondre à une question

### **Étape par étape**

```
1. Utilisateur ouvre la page
   ↓ Django: GET /round/
   ↓ Views.py récupère la question 3
   ↓ Template affiche: "Quelle est la capitale?"

2. Utilisateur clique sur "Paris"
   ↓ HTML: <input name="choice" value="a" checked>

3. Utilisateur clique "Valider"
   ↓ Django: POST /round/
   ↓ Data: {'choice': 'a', 'csrfmiddlewaretoken': 'xxx'}

4. Views.py reçoit
   ↓ chosen = 'a'
   ↓ q = Question.objects.get(pk=3)
   ↓ if 'a' == q.correct:  # 'a' == 'a' = True
   ↓ score += 1  # 2 + 1 = 3

5. Session mise à jour
   ↓ session['score'] = 3
   ↓ session['round_index'] = 3

6. Django rend le feedback
   ↓ Template: "✓ Bonne réponse!"

7. Utilisateur clique "Question suivante"
   ↓ Views.py augmente l'index
   ↓ Affiche la question 4
```

---

## 🎓 Résumé en image

```
┌─────────────────────────────────────────────┐
│              WEB BROWSER (Client)           │
│  ┌──────────────────────────────────────┐   │
│  │ Page HTML rendue                     │   │
│  │ - Questions                          │   │
│  │ - Boutons                            │   │
│  │ - Timer JavaScript                   │   │
│  │ - Styles CSS                         │   │
│  └──────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
           ↓ GET/POST (HTTP) ↑
┌──────────────────────────────────────────────┐
│        DJANGO SERVER (Logique)               │
│  ┌──────────────────────────────────────┐   │
│  │ Views.py                             │   │
│  │ - Reçoit requête                     │   │
│  │ - Vérifie réponse                    │   │
│  │ - Augmente score                     │   │
│  │ - Rend template                      │   │
│  └──────────────────────────────────────┘   │
│           ↓ ORM Queries ↑                    │
│  ┌──────────────────────────────────────┐   │
│  │ SQLite Database                      │   │
│  │ - Table quiz_question                │   │
│  │ - 36 questions                       │   │
│  │ - Thèmes, réponses, explications     │   │
│  └──────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
```

---

## 🚀 Maintenant vous savez comment ça marche!

**Points clés à retenir:**

1. **Django reçoit les requêtes** du navigateur
2. **Views.py exécute la logique** (vérifier les réponses)
3. **Models.py interroge la BD** (récupérer les questions)
4. **Templates rendent du HTML** (afficher la page)
5. **Sessions gardent en mémoire** le contexte du joueur
6. **JavaScript gère le timer** côté navigateur
7. **CSS stylise** avec un thème sombre

C'est l'architecture classique d'une app web moderne! 🌐

