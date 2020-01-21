# Guide d'installation

Pour pouvoir utiliser le projet, il faut commencer par installer
  * python (version 3.7.4) : https://www.python.org/downloads/
  * pip (version 19.2.3) : https://pip.pypa.io/en/stable/installing/

## Création d'un environnement virtuel
* Il faut ensuite créér et lancer l'environnement avec les commandes :  
```
$ pip install virtualenv
$ virtualenv financial_sentiments
$ financial_sentiments\Scripts\activate
```

## Installation des packages
Il faut ensuite lancer la commande :
```
$ pip install -r requirements.txt
```
Où ``requirements.txt`` est le fichier contenant les dépandances fourni dans le dossier.

Il faut ensuite lancer cette commande pour installer le dictionnaire *Spacy* :
```
$ python -m spacy download en_core_web_sm
```

## Lancer le notebook
Il est ensuite possible de lancer le notebook avec la commande :
```
$ jupyter notebook
```
**Il faut bien s'assurer que le dossier contenant les notebooks se situe bien dans le dossier contenant l'environnement virtuel. C'est à dire dans le dossier ``financial_sentiments``.**

Il est maintenant possible depuis jupyter d'ouvrir le dossier du projet et d'accèder au différents notebooks.

## Quitter l'environnement
Pour quitter l'environnement utilisez la commande :
```
$  deactivate
```
