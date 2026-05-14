## Fiches comprehensions sur les modules, packages et imports

### 1) les modules

Les modules sont simplement des fichier. py

Les modules = une partie de code. Une fonctionnalité

### 2) Les packages

-> Un dossier qui contient de fichiers.

Un groupe de fichier dans un dossier

Mais attention un dossier N'est pas un package sans : 

#### __init__.py (très important)
Rôle

C’est le fichier qui transforme un dossier en package Python.

Exemple :
alchemy/
    __init__.py
    spells.py

-> Sans __init__.py :

Python peut ignorer le dossier (selon version / contexte)

-> Avec __init__.py :

le dossier devient un package importable