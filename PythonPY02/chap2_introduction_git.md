# Git 

Vérifiez que vous avez git sur votre machine

```bash
git --version
```

- Créez un compte sur Github

Mettre maintenant les informations mis sur Github dans votre configuration locale de Git, par exemple si vous vous appelez Tony avec un mail tony@tony.fr sur Github :

```bash
git config --global user.name Tony 
git config --global user.email tony@tony.fr
```

## Créez un dépôt sur Github 


1. Créez un dépôt sur Github par exemple **exercices_ECI**

Puis dans un dossier à vous 

```bash
# initialiser le dépôt (obligatoire), crée l'historique
git init
# on versionne un fichier mis dans la staging 
git add README.md
# Pour versionner tous les fichiers
# git add .

# premier commit
git commit -m "first commit"

# Changez la branche pour fonctionner avec Github qui est sur main pas master
git branch -M main
# Remote distant (lien avec votre dépôt local et distant)
git remote add origin https://github.com/Antoine07/exercices_ECI.git

# push le fichier / les fichiers sur la branche principale
git push -u origin main

```

Attention pour chaque push vous allez devoir mettre votre mot de passe.

Pour supprimer votre remote :

```bash
git remote remove origin
```

- Tous les autres push se feront avec les commandes suivantes :

```bash
git add .
git commit -m "second commit"
git push
```