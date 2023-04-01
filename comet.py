import pygame
import random

# creer une class pour gerer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir quel image associer a cette comete
        self.image = pygame.image.load("/Users/Thomas/PycharmProjects/game/assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 1150)
        self.rect.y = - random.randint(0, 700)
        self.comet_event = comet_event


    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play("meteorite")

        # verifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la bar a 0
            self.comet_event.reset_percent()
            # apparaitre les deux premier monstre
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # elle ne tombe pas sur le sol
        if self.rect.y >= 400:
            # retirer la boule de feu
            self.remove()

        # si il n'y a plus de boule de feu
        if len(self.comet_event.all_comets) == 0:
            # remettre la jauge au depart
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False



        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # subir des degats
            self.comet_event.game.player.damage(40)