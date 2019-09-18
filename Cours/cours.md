# Cours d'algo PCH

## Objectif :

Réaliser un programme qui affiche dans une fenetre graphique
une balle ayant une vitesse initiale en déplacement sous l'action
de la gravité.

Le tout en python + pygame

## Contenu des cours

5 h de cours reparties comme suit :
- 2h présentation python :
    - variables / tests / boucles
    - fonctions
    - les classes (pour stocker x,y, vx,vy, ax, ay)

- 2h de présentation pygame sur la base de [ce lien](https://elbixos.github.io/L1_OptionInfo/Projets/JeuVideo/Cours/cours.html)

- 1h de présentation du problème physique
    - modélisation du problème : quelles variables 
    - equations : ma = mg - kv (si frottement)
    - intégration numérique :
      définition d'un pas de temps deltaT puis
      vx = vx + ax * deltaT
      x = x+ vx * deltaT

## Contenu des TP

- séance 1 : une balle placée quelque part, quand on appuye sur <space> :
    - la balle se déplace verticalement vers le bas
    et s'arrete en bas de la fenetre.

- séance 2 :
    - amélioration : déplacement diagonal vers le bas
    - amélioration : paramétrage par sa position
    - ajout d'une vitesse prédéfinie.

- séance 3 :
    - ajout de la gravité
    - ajout d'un coefficient de frottement

- séance 4 :
    - ajout d'un réglage graphique de la vitesse initiale

- séance 5 : (si tout s'est bien passé)
    - ajout de la possibilité de lancer autant de balles qu'on veut
    (avec un tableau de balles)


