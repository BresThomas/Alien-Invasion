import pygame
from projectile import Projectile
import animation


# creer une 1ere classe Joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 7
        self.all_projectiles = pygame.sprite.Group()
        #self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 350

    def damage(self, amount):
        if self.health - amount > amount:
           self.health -= amount
        else:
            # si le joueur na plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()


    def update_health_bar(self, surface):
        # barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):
        # creer une nouvelle instance de classe Projectile
        self.all_projectiles.add(Projectile(self))
        # demarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play("tir")

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
