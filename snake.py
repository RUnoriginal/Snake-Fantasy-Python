# coding: utf-8
import pygame
import time
import random

pygame.init()

# definition des couleurs utilisées dans le jeu
YELLOW = (255, 255, 102)
RED = (213, 0, 0)

# ----------------- ecran -------------
# definition de la taille de l'écran
window_width = 600
window_height = 400

#definition des fonts de l'écran
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# creation de l'ecran
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake')
# ---------------- fin ecran ------------

# démarage du ctimer
clock = pygame.time.Clock()

# caractéristiques du snake
snake_size = 20 # taille d'un element du corps
snake_speed = 7 # vitesse de déplacement
dwarf_chief_down = pygame.image.load ("assets/Chef_Nain1.png")
dwarf_chief_right = pygame.image.load ("assets/Chef_Nain2.png")
dwarf_chief_up = pygame.image.load ("assets/Chef_Nain3.png")
dwarf_chief_left = pygame.image.load ("assets/Chef_Nain4.png")
dwarf_down = pygame.image.load ("assets/Nain1.png")
dwarf_right = pygame.image.load ("assets/Nain2.png")
dwarf_up = pygame.image.load ("assets/Nain3.png")
dwarf_left = pygame.image.load ("assets/Nain4.png")
apple_image = pygame.image.load ("assets/Diamant.png")
background_img = pygame.image.load ("assets/Fond.png")
image_x = 0
image_y = 0

def score(score1):
    """
    Affichage du score1
    param :
        score1  (int) :Le score1 à afficher
    """
    value = score_font.render("score: " + str(score1), True, YELLOW)
    window.blit(value, [0, 0])


def snake_render(snake_size, snake_list):
    """
    Affichage du snake
    param :
        snake_size (int) : taille en pixel d un anneau du snake
        snake_liste (list) : liste des anneaux chaque membre de la liste est un tuple
    """
    for x in snake_list:
        if x == snake_list[-1]:
            if x[2] == 'bas':
                window.blit(dwarf_chief_down,(x[0],x[1]))
            if x[2] == 'haut':
                window.blit(dwarf_chief_up,(x[0],x[1]))
            if x[2] == 'droite':
                window.blit(dwarf_chief_right,(x[0],x[1]))
            if x[2] == 'gauche':
                window.blit(dwarf_chief_left,(x[0],x[1]))
        else:
            if x[2] == 'bas':
                window.blit(dwarf_down,(x[0],x[1]))
            if x[2] == 'haut':
                window.blit(dwarf_up,(x[0],x[1]))
            if x[2] == 'droite':
                window.blit(dwarf_right,(x[0],x[1]))
            if x[2] == 'gauche':
                window.blit(dwarf_left,(x[0],x[1]))

def message(msg, color):
    """
    Affichage du message
    """
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width // 2 - mesg.get_width()//2, window_height // 2 - mesg.get_height()//2])

def game_loop():
    """
    Boucle du jeu
    """
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    size = 1
    direction = 'bas'

    apple_x = round(random.randrange(0, window_width - snake_size) / snake_size) * snake_size
    apple_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size

    while not game_over:

        while game_close == True: # si le jeu est terminé
            window.blit (background_img,(image_x,image_y))
            message("Perdu! C pour rejouer ou echap pour quitter", RED)
            score(size - 1)
            pygame.display.update()

            for event in pygame.event.get(): # attente de touches pour continuer ou quitter
                if event.type == pygame.KEYDOWN:
                    print (event.key)
                    if event.key ==27: # esc pour quitter
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # pour continuer
                        game_loop()

        for event in pygame.event.get():# Traitement des touches pour bouger
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change!=snake_size:
                    x1_change = -snake_size
                    y1_change = 0
                    direction= 'gauche'
                elif event.key == pygame.K_d and x1_change!=-snake_size:
                    x1_change = snake_size
                    y1_change = 0
                    direction= 'droite'
                elif event.key == pygame.K_w and y1_change!=snake_size:
                    y1_change = -snake_size
                    x1_change = 0
                    direction= 'haut'
                elif event.key == pygame.K_s and y1_change!=-snake_size:
                    y1_change = snake_size
                    x1_change = 0
                    direction= 'bas'

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.blit (background_img,(image_x,image_y))
        window.blit(apple_image,(apple_x, apple_y))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_head.append(direction)
        snake_list.append(snake_head)
        if len(snake_list) > size:
            del snake_list[0]

        # detectection du snake qui se mort la queue
        for x in snake_list[:-1]:
            if x[0] == snake_head[0] and x[1]==snake_head[1]:
                game_close = True

        snake_render(snake_size, snake_list) # affichage du snake
        score(size - 1)# affichage du score1

        pygame.display.update()# mise à jour affichage

        #traitement snake mange la pomme
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randint(0, window_width - snake_size) / snake_size) * snake_size
            apple_y = round(random.randrange(0, window_height - snake_size) / snake_size) * snake_size
            size += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

#Programme_principal
game_loop()
