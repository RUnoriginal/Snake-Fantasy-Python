import pygame
import time
import random

pygame.init()

# definition des couleurs utilisées dans le jeu
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 0, 0)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# ----------------- ecran -------------
# definition de la taille de l'écran
largeur_frenetre = 600
hauteur_fenetre = 400

#definition des fonts de l'écran
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# creation de l'ecran
fenetre = pygame.display.set_mode((largeur_frenetre, hauteur_fenetre))
pygame.display.set_caption('DS Snake')
# ---------------- fin ecran ------------

# démarage du ctimer
clock = pygame.time.Clock()

# caractéristiques du snake
snake_taille = 20 # taille d'un element du corps
snake_vitesse = 7 # vitesse de déplacement
chef_nain_bas = pygame.image.load ("Chef_Nain1.png")
chef_nain_droite = pygame.image.load ("Chef_Nain2.png")
chef_nain_haut = pygame.image.load ("Chef_Nain3.png")
chef_nain_gauche = pygame.image.load ("Chef_Nain4.png")
nain_bas = pygame.image.load ("Nain1.png")
nain_droite = pygame.image.load ("Nain2.png")
nain_haut = pygame.image.load ("Nain3.png")
nain_gauche = pygame.image.load ("Nain4.png")
image_pomme = pygame.image.load ("Diamant.png")
image_fond = pygame.image.load ("Fond.png")
image_x = 0
image_y = 0

def Le_score(score):
    """
    Affichage du score
    param :
        score  (int) :Le score à afficher
    """
    value = score_font.render("Score: " + str(score), True, jaune)
    fenetre.blit(value, [0, 0])


def Affichage_snake(snake_taille, snake_list):
    """
    Affichage du snake
    param :
        snake_taille (int) : taille en pixel d un anneau du snake
        snake_liste (list) : liste des anneaux chaque membre de la liste est un tuple
    """
    for x in snake_list:
        if x == snake_list[-1]:
            if x[2] == 'bas':
                fenetre.blit(chef_nain_bas,(x[0],x[1]))
            if x[2] == 'haut':
                fenetre.blit(chef_nain_haut,(x[0],x[1]))
            if x[2] == 'droite':
                fenetre.blit(chef_nain_droite,(x[0],x[1]))
            if x[2] == 'gauche':
                fenetre.blit(chef_nain_gauche,(x[0],x[1]))
        else:
            if x[2] == 'bas':
                fenetre.blit(nain_bas,(x[0],x[1]))
            if x[2] == 'haut':
                fenetre.blit(nain_haut,(x[0],x[1]))
            if x[2] == 'droite':
                fenetre.blit(nain_droite,(x[0],x[1]))
            if x[2] == 'gauche':
                fenetre.blit(nain_gauche,(x[0],x[1]))

def message(msg, color):
    """
    Affichage du message
    """
    mesg = font_style.render(msg, True, color)
    fenetre.blit(mesg, [largeur_frenetre // 2 - mesg.get_width()//2, hauteur_fenetre // 2 - mesg.get_height()//2])

def Boucle_jeu():
    """
    Boucle du jeu
    """
    game_over = False
    game_close = False

    x1 = largeur_frenetre / 2
    y1 = hauteur_fenetre / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    taille_snake = 1
    sens = 'bas'

    pomme_x = round(random.randrange(0, largeur_frenetre - snake_taille) / snake_taille) * snake_taille
    pomme_y = round(random.randrange(0, hauteur_fenetre - snake_taille) / snake_taille) * snake_taille

    while not game_over:

        while game_close == True: # si le jeu est terminé
            fenetre.blit (image_fond,(image_x,image_y))
            message("Perdu! C pour rejouer ou echap pour quitter", rouge)
            Le_score(taille_snake - 1)
            pygame.display.update()

            for event in pygame.event.get(): # attente de touches pour continuer ou quitter
                if event.type == pygame.KEYDOWN:
                    print (event.key)
                    if event.key ==27: # esc pour quitter
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # pour continuer
                        Boucle_jeu()

        for event in pygame.event.get():# Traitement des touches pour bouger
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change!=snake_taille:
                    x1_change = -snake_taille
                    y1_change = 0
                    sens= 'gauche'
                elif event.key == pygame.K_d and x1_change!=-snake_taille:
                    x1_change = snake_taille
                    y1_change = 0
                    sens= 'droite'
                elif event.key == pygame.K_w and y1_change!=snake_taille:
                    y1_change = -snake_taille
                    x1_change = 0
                    sens= 'haut'
                elif event.key == pygame.K_s and y1_change!=-snake_taille:
                    y1_change = snake_taille
                    x1_change = 0
                    sens= 'bas'

        if x1 >= largeur_frenetre or x1 < 0 or y1 >= hauteur_fenetre or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.blit (image_fond,(image_x,image_y))
        fenetre.blit(image_pomme,(pomme_x, pomme_y))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_Head.append(sens)
        snake_List.append(snake_Head)
        if len(snake_List) > taille_snake:
            del snake_List[0]

        # detectection du snake qui se mort la queue
        for x in snake_List[:-1]:
            if x[0] == snake_Head[0] and x[1]==snake_Head[1]:
                game_close = True

        Affichage_snake(snake_taille, snake_List) # affichage du snake
        Le_score(taille_snake - 1)# affichage du score

        pygame.display.update()# mise à jour affichage

        #traitement snake mange la pomme
        if x1 == pomme_x and y1 == pomme_y:
            pomme_x = round(random.randint(0, largeur_frenetre - snake_taille) / snake_taille) * snake_taille
            pomme_y = round(random.randrange(0, hauteur_fenetre - snake_taille) / snake_taille) * snake_taille
            taille_snake += 1

        clock.tick(snake_vitesse)

    pygame.quit()
    quit()

#Programme_principal
Boucle_jeu()