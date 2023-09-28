# Flask installation

## Rappels de la philosophie Python

Pour connaitre l'ensemble des règles en Python pour bien programmer dans ce langage, tapez la ligne de commande suivante dans un shell Python :

```bash
import this 
```

Cette commande affichera les règles fondamentales suivantes :

```txt
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

Flask c'est un micro-framework. Il permet de faire des API et des application Web dynamiques.
Il est moins utiliser que PHP avec Symfony ou Laravel (frameworks en PHP).

## Installation et définition de fichier app.py

Exemple de structure d'une mini-application en Flask avec ses données et ses vues

```txt
myapp
├── Data
│   ├── authors.py
│   └── users.py
├── app.py        <-- le point d'entrée avec les routes, il dispatch les routes en renvoyant une vue au navigateur
|── templates
   ├── base.html
   └── index.html
```

Dans un premier temps créer un dossier myapp sur votre bureau et créez le fichier suivant :

app.py, permet d'écrire les routes de votre application, il se trouve à la racine de l'application.

```python
from flask import Flask

# une instance de l'application 
app = Flask(__name__) 

"""
"/" : correspond à la route http://localhost:5000

@app.route permet de définir une route 
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

"""
"/users" : correspond à la route http://localhost:5000/users
"""
@app.route("/users")
def users():
    return "<p>tous les utilisateurs</p>"
```

### Windows 

Dans un terminal sur votre bureau et dans un dossier où vous souhaitez démarrer le projet

```bash
python -m venv myapp
```

Dans un PowerShell, toujours dans le dossier myapp

```bash
.\myapp\Scripts\Activate
```

Résumé dans l'invite de commande 

```bash
myapp\Scripts\activate

# installation de Flask
pip install flask
```

Commandes utiles 

Démarrer le serveur sur le port 5000 en localhost :

```bash
flask run
```

Puis, on installera Flask dans le dossier virtualisé, notez que les dépendances suivantes seront également installées :

- Werkzeug: implémente WSGI, la norme Python standard entre les applications et les serveurs.

- Jinja: est un langage de modèle qui rend les pages que votre application sert.

- MarkupSafe: est livré avec Jinja. Il échappe aux entrées non fiables lors du rendu des modèles pour éviter les attaques par injection.

- ItsDangerous: signe de manière sécurisée les données pour garantir leur intégrité. Cela est utilisé pour protéger le cookie de session de Flask.

- Click: est un framework pour écrire des applications en ligne de commande. Il fournit la commande flask et permet d'ajouter des commandes de gestion personnalisées.

Blinker: fournit une prise en charge des signaux.

### Sous Mac ou Linux

Résumé des commandes 

```bash
python -m venv .venv
. .venv/bin/activate
pip install flask

flask run 
```

## Désactivation de la virtualisation 

Attention, pour chaque session de votre console, vous devez activer l'environnement.

Pour désactiver et supprimer l'environnement, tapez la commande suivante :

```bash

# Mac ou Linux
deactivate

# Dans cmder pour Windows
.\\Scripts\\deactivate.bat

# Suppression du dossier d'environement
rm -rf env

# Pour désactiver l'environement
deactivate

# Dans cmder pour Windows
.\\Scripts\\deactivate.bat

```

### Création d'un fichier de dépendance

Afin de spécifier les dépendances utilisées dans votre projet, vous devez créer le fichier suivant. Cela permettra de partager vos projets et de les migrer facilement sur un autre poste de travail.

Entrez dans votre environnement virtualisé

```bash

# commande permettant d'écrire les dépendances dans ce fichier avec leurs versions.
pip freeze > requirements.txt

# Sous Windows
pip list > requirements.txt
```

Nous allons maintenant créer une petite application pour découvrir un peu mieux le micro-framework Flask

### Organisation des dossiers

- Un dossier "static" pour les assets.
- Un dossier "templates" pour les vues.
- Un dossier "tests" pour les tests.

## Création des templates et fichiers statiques

Nous allons partir de données d'exemple, créez le fichier users.py dans le dossier Data dans notre projet myapp.

Data/users.py

```python
users = [
    {
        "id": 0,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "bio": "Développeur Python passionné. Amateur de jeux vidéo."
    },
    {
        "id": 1,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 28,
        "bio": "Ingénieure logiciel avec une expertise en Python. Aime la randonnée."
    },
    {
        "id": 2,
        "name": "Bob Johnson",
        "email": "bob@example.com",
        "bio": "Étudiant en informatique, aime coder en Python. Fan de musique."
    },
    {
        "id": 3,
        "name": "Eva Wilson",
        "email": "eva@example.com",
        "age": 35,
        "bio": "Développeuse Python senior. Passionnée de photographie."
    }
]
``` 

### 01 Exercice configuration

1. Affichez les données d'exemple dans la page index.html, en utilisant la route "/" (créez une nouvelle route)

Pour le reload tapez la ligne de commande suivante :

```python
flask run --reload
```

**Indication** sur les ternaires, ils permettent d'afficher en ligne des valeurs de manière conditionnelle, pratique dans les templates :

```python
a = True
'a est vrai' if a else 'a est faux'
# a est vrai

a = False
'a est vrai' if a else 'a est faux'
# a est faux
```

2. Créez une nouvelle route pour afficher l'ensemble des auteurs dans une nouvelle vue. 

**Correction** 

- On importe les données dans le fichier app.py 

```python
# Import relatif à un dossier et fichier
from Data.authors import authors 
```

- Puis, on crée la route dans le fichier **app.py** avec la méthode **route** du **décorateur @app** 

```python

@app.route("/authors")
def authors():
    # premier paramètre le template, deuxième paramètre c'est les données passées à la vu
    return render_template('authors.html', authors=authors)
```

- Il faut également créer le fichier authors.html dans le dossier templates

```python
<ul>
    {% for author in authors %}
    <li>{{ author['last_name'] }}</li>
    <li>{{ author['first_name'] }}</li>
    <li>{{ author['nationality'] }}</li>
    <li>{{ author['famous_work'] }}</li>
    {% endfor %}
</ul>

```

3. Utilisez maintenant le template de base et faites en sorte que toutes vos vues soient étendues de ce fichier base.html

- les templates 

**base.html**

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flask</title>
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">
<nav>
  <ul>
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
 
  {% block content %}{% endblock %}
</section>
```

**index.html** ce fichier est étendu du fichier base.html

```html
{% block header %}
<h1>List</h1>
{% endblock %}

{% block content %}
<table class="table table-dark">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">email</th>
            <th scope="col">age</th>
        </tr>
    </thead>
    <tbody>
        {% for user in users %}
            TODO : affichez les informations suivantes Name, email et age si cette information existe.
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

- fichier app.py

```python
from flask import Flask, render_template
from Data import users

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', users=users)
```

Pour la suite, pensez à taper la commande suivante pour surveiller les changements dans les fichiers et être en mode développement.

```bash
flask run --reload --extra-files 'templates/*.html' --debug
```

### 02 Exercice afficher les données users

Affichez les données users dans le dictionnaire **users** pour la route "/".

### 03 Exercice la bio de chaque user dans un nouveau fichier 

**Rappel** 

Pour définir une route dynamique on écrira :

La syntaxe suivante permet de définir un paramètre dynamique 

```python
# <id> == paramètre dynamique user/191  ==> id sera égale à 191
@app.route("/user/<id>")

```

Puis la fonction reprends le nom du paramètre pour récupérer la valeur

```python
@app.route("/user/<id>")
def user(id):
    return f"id : {id}"

```

**Deuxième exemple**

```python
@app.route("/user/<name>")
def user(name):
    return f"Name : {name}"

```

Utilisez une page spécifique pour afficher le détail d'un utilisateur voir la clé bio :

La route sera dynamique dans le template, écrivez le code suivant :

```python
<a href="user/{{user['id']}}">{{ user['name'] }}</a>
```

Dans le fichier app.py vous décorez une route dynamique avec la syntaxe suivante :

```python
# id route dynamique avec une valeur 
@app.route('/user/<id>')
def user(id):
    return f"hello {id}" 
```

### 04 Exercice affichez un auteur

Refaire la même chose que l'exercice 03 pour les auteurs, affichez tous les informations si elles existent pour un auteur.

## Route POST ( Exercice 05)

Pensez à importer le module request de Flask.

Nous allons voir comment maintenant traiter les routes POST ou GET, dans l'exemple qui suit vous avez les deux verbes possibles HTTP passés en paramètre de la méthode route :

```python 
@app.route('/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        pass
    else:
        pass
```

Indication pour récupérer en méthode POST les données du formulaire, vous utiliserez le code suivant, vérifiez que votre formulaire est en mode POST.

```python
 email = request.form.get('email')
```

Terminez cette mise en place en ajoutant un utilsateur user qui n'est pas déjà présent dans les données ( travaillez sur la liste users).

## 01 TP films

**Par équipe de 2 personnes**.

1. Développez maintenant une application avec deux pages une page home.html et une page picture.html, utilisez également un template base.html

**Fonctionnalités**

Détails des urls

- GET /api/pictures: Obtenir la liste de tous les films.
- GET /api/picture/<int:id>: Obtenir un film par ID.

```python
pictures = [
    {"id": 0, "title": "Inception", "director": "Christopher Nolan"},
    {"id": 1, "title": "The Shawshank Redemption", "director": "Frank Darabont"},
    {"id": 2, "title": "Pulp Fiction", "director": "Quentin Tarantino"},
    {"id": 3, "title": "The Godfather", "director": "Francis Ford Coppola"},
    {"id": 4, "title": "The Dark Knight", "director": "Christopher Nolan"}
]
```

2. (Facultatif) Créez un lien **shuffle** qui mélange la liste des films, pensez à faire une fonction en Python dans votre projet pour vous aider.

- GET /api/shuffle/ Obtenir la liste des films à chaque présenter de manière aléatoire 

### 02 TP ajouter un user

Par équipe de 2 

1. Créez une page permettant d'ajouter un utilisateur à notre dictionnaire users. (première application développée ensemble).

*Utilisez la fonction flash de Flask pour vérifier l'existence d'un utilisateur, faites la gestion des erreurs.
Aidez-vous de la documentation pour faire cela.*

2. Essayez maintenant de faire la méthode **DELETE**, pour supprimer un utilisateur ( dans les données users).