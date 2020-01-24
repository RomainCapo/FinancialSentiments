=Readme=
==Arboresence==
* Le dossier "030-Developpement" contient les différents notebook retracant les étapes d'élaboration des modèles de machine learning et deep learning.

À l'intérieur de ce dossier se trouve : 
	* le dossier "tools" contient les différentes classe utilitaires crées pour le projet.
	* une archive zip nommé "dataset.zip" qui contient le dossier "dataset" contenant les différents jeux de données utilisés pour le projet.
	* le dossier "saved_model" contient une sauvegarde de certains modèles developpé durant ce projet avec l'extension ".joblib*. Il est possible d'importer ces modèles à l'aide de la librairie Joblib.
	* une archive zip nommé "word2vec.zip" contenant le dossier "word2vec" qui contient deux sous dossier :
  		* le dossier "financialWord2Vec" qui contient le word2vec entrainé avec le vocabulaire financiers.
  		* le dossier "glove" qui contient le fichier précalculé avec les différents vecteurs correspondsant à la représentation d'un mot dans l'espace.  
	* le dossier "admin" contient différent document et dossier pour les documents administratifs du projet. Il contient également les images du notebook.

==Version de python==
* python : 3.7.4

==Guide d'installation==

Pour pouvoir utiliser le projet, il faut avoir Python et pip installé sur la machine : 
  * python (version 3.7.4) : https://www.python.org/downloads/
  * pip (version 19.2.3) : https://pip.pypa.io/en/stable/installing/

===Création d'un environnement virtuel===
* Il faut ensuite créér et lancer l'environnement avec les commandes :  
```
$ pip install virtualenv
$ virtualenv financial_sentiments
$ source financial_sentiments/Scripts/activate
```

Si pour la dernière commande le message d'erreur : "source n'est pas reconnu en tant que commande interne ou externe" survient il faut remplacer la dernière commande par : 
```
financial_sentiments\Scripts\activate
```

===Installation des packages===
Il faut ensuite lancer la commande pour installer les packages:
```
$ pip install -r requirements.txt
```
Où ``requirements.txt`` est le fichier contenant les dépandances se trouvants dans le dossier ``030-Developpement``.

Il faut ensuite lancer cette commande pour installer le dictionnaire *Spacy* :
```
$ python -m spacy download en_core_web_sm
```

===Lancer le notebook===
Il est ensuite possible de lancer le notebook avec la commande :
```
$ jupyter notebook
```
**Il faut bien s'assurer que le dossier contenant les notebooks(030-Developpement) se situe bien dans le dossier contenant l'environnement virtuel. C'est à dire dans le dossier ``financial_sentiments``.**

Il est maintenant possible depuis jupyter d'ouvrir le dossier du projet et d'accèder au différents notebooks.

===Quitter l'environnement===
Pour quitter l'environnement utilisez la commande :
```
$  deactivate
```
