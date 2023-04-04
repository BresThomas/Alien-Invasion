import pygame
import random
import animation

# definir le monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 200)
        self.rect.y = 400 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(5, 6)

    def set_loop_amount(self, amount):
        self.loot_amount = amount


    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # verifier si nouveau nombre inferieur a 0
        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 200)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter nombre de points a score
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est chargée a son max
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la methode pour essayer de declancher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si il est en collision avec le joueur
        else:
            # infliguer degats
            self.game.player.damage(self.attack)

# definir class pour la mommy
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loop_amount(20)


# definir class pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)
        self.set_speed(1)
        self.health = 250
        self.attack = 0.8
        self.max_health = 250
        self.set_loop_amount(80)
