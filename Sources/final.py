import pygame
import random

# convertit la position de la Balle
# en metres, dans un espace compris entre 0 et 100)
# en pixels (dans la fenetre)
# Attention,
#   (0,0) en metres, est en bas a gauche
#   alors que (0,0) en pixels est le coin sup gauche de la fenetre
def pos2pixels(b,fenetre):
    rect = fenetre.get_rect()

    x = b.x /100 * rect.width
    y = (100 - b.y)/100 * rect.height

    return (x,y)

def gestionExit(touches, events):
    continuer = True

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=False

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for e in events:   # parcours de la liste des evenements recus
        if e.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = False	   # On arrete la boucle

    return continuer

def afficherBalle(b, image, fenetre):
    rect = image.get_rect()
    xpix, ypix = pos2pixels(b,fenetre)

    rect.x = xpix
    rect.y = ypix

    fenetre.blit(image, rect)


# On déplace la Balle
def deplacerBalle(b):
    deltaT = 0.1 # pas de calcul : 0.1 s

    k = 0.1 # Coeff de frottement

    # blocage en cas de sortie
    if (b.x <0 or b.y < 10 or b.x > 92 or b.y > 100 ):
        print("out")
    else :
        b.ay = -9.81 - k * b.vy
        b.ax = - k * b.vx
        b.vx = b.vx + b.ax*deltaT
        b.vy = b.vy + b.ay*deltaT
        b.x = b.x + b.vx *deltaT
        b.y = b.y + b.vy *deltaT

    return b

class Balle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0


# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 480
hauteur = 480

fenetre=pygame.display.set_mode((largeur,hauteur))

# lecture de l'image de la balle
imageBalle = pygame.image.load("balle.png").convert_alpha()
# lecture de l'image du fond
imageFond = pygame.image.load("background.jpg").convert()


# Creation de l'image correspondant au texte
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

imageText = font.render('<Escape> : quitter, <Space> ajout Balle', True, (255, 255, 255))

mesBalles = []

# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
continuer=True
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)


    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();
    # on recupere la liste des evenements (souris, clavier...)
    events = pygame.event.get()

    # Si on appuye sur Space, on cree une balle
    if touches[pygame.K_SPACE]:
        print ("AJOUT")
        b = Balle()
        b.x = 50
        b.y = 10
        b.vx = random.random()*40 -20
        b.vy = random.random()*40
        mesBalles.append(b)

    for b in mesBalles:
        b=deplacerBalle(b)
        #print (b.x,b.y,b.vx,b.vy)

    # On verifie si l'utilisateur a appuyé sur ESC ou cliqué pour quitter
    continuer = gestionExit(touches, events)

    # Affichage du fond
    fenetre.blit(imageFond,(0,0))

    # Affichage Balle
    for b in mesBalles:
        afficherBalle(b,imageBalle, fenetre)

    # Affichage du Texte
    fenetre.blit(imageText, (10,10))

    # rafraichissement
    pygame.display.flip()


# fin du programme principal...
pygame.quit()
