# __<u>SHELDON TOURNAMENT</u>__



**Sommaire**
* I - Présentation du projet
* II - Règles
* III - Installation et explications
* IV - Lancement de l'application
* V - Crédits



## <u>I - Présentation du projet</u>

Ce projet est une variante du jeu 'Pierre-Feuille-Ciseaux' vue dans la série 'The Big Bang Theory' (Pierre-Feuille-Ciseaux-Lezard-Spock) où, dans un avenir parallèle proche, des tournois de cette variante sont organisés.

Dans ce projet, 3 tournois se sont déroulés. Le but est, avec la liste des coups de chaque joueur et celle des matchs du premier tour, de déterminer le vainqueur tournois.

Le résultat de chaque match devra être archivé dans un fichier 'matches.csv' et le nom du vainqueur stocké dans un fichier 'result.txt'.


## <u>II - Règles</u>

Dans cette variante, le résultat entre chaque coups est le suivant:
* Les ciseaux coupent la feuille
* La feuille couvre la pierre
* La pierre écrase le lézard
* Le lézard empoisonne Spock
* Spock casse les ciseaux
* Les ciseaux décapitent le lézard
* Le lézard mange la feuille
* La feuille réfute Spock
* Spock vaporise la pierre
* La pierre écrase les ciseaux

En cas d'égalité, le vainqueur sera le joueur dont le nom sera en premier dans l'ordre alphabétique


## <u>III - Installation et explications</u>

Décrompressez le fichier .zip à l'endroit de votre choix que nous appellerons [Adresse].

L'arborescence du dossier décompressé est la suivante :
```jsx
sheldon-tournament (répertoire principal [main_folder])
    archives
    img
    tournament_1
    tournament_2
    tournament_3
    tournament_functions
    aps_main.py
    README.md
```

La liste des coups de chaque joueurs (players_infos.csv) ainsi que celle des matchs prévus pour le premier tour (round_0.csv) sont enregistrées dans le dossier de chaque tournois ([tournament_num] *).

Le fichier contenant les archives de matchs ainsi que celui contenant le nom du vainqueur du tournois sont stockées dans le dossier [archives].

Ces fichiers sont enregistrés avec la nomenclature suivante :
* matches_[num]_[timestamp].csv * **
* result_[num]_[timestamp].txt * **


## <u>IV - Lancement de l'application</u>

Ouvrez une invite de commande puis rendez-vous dans le répertoire principal du projet :
```jsx
"cd [Adresse]\[main_folder]"
```

puis lancez l'application avec la commande suivante :
```jsx
python aps_main.py
```
Le pojet va se lancer et vous demander de choisir l'un des 3 tournois disponibles ou de quitter l'application.


## <u>V - Credits</u>

Projet scolaire effectué en avril 2022 dans le cadre d'un formation reskilling (module Python) avec l'EFREI.

Projet réalisé en binôme par:
* BREVIA Maria Carmen
* ROGER Aurélien




*[num] est à remplacer par le numéro du tournois (1, 2 ou 3)
**[timestamp] au fromat suivant YYYYMMDDhhmmss





