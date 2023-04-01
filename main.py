import pygame
from game import Game
import math
from player import Player
pygame.init()

# definir une clock
#clock = pygame.time.Clock()
#FPS = 60

# fenetre
pygame.display.set_caption("Mon jeu")
screen = pygame.display.set_mode((1280, 612))

# bg
background = pygame.image.load('/Users/Thomas/PycharmProjects/game/assets/bg.jpg').convert()
background = pygame.transform.scale(background, (1280, 612))

# appliquer la fenetre du jeu
screen.blit(background, (0, 0))

# importer banniere
banner = pygame.image.load("/Users/Thomas/PycharmProjects/game/assets/banner.png")
banner = pygame.transform.scale(banner, (350, 350))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2.75)
banner_rect.y = 65

# charger bouton pour lancer la partie
play_button = pygame.image.load("/Users/Thomas/PycharmProjects/game/assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.95)
play_button_rect.y = math.ceil(screen.get_height() / 1.85)

# charger notre jeu
game = Game()

running = True


# boucle infinit
while running:

    screen.blit(background, (0, 0))

    # verifier si jeu a commencer ou non
    if game.is_playing:
        # declancher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencer
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            # detecter si joueur lache une touche au clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play("click")


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris touche le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # jouer le son
                game.sound_manager.play("click")

    # fixer le nombre de FPS dans ma clock
    #clock.tick(FPS)


