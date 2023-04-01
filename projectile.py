import pygame


# definir la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load("/Users/Thomas/PycharmProjects/game/assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 95
        self.rect.y = player.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile est en colision
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters ):
            # supprimer le projectile
            self.remove()
            # infliguer des degats
            monster.damage(self.player.attack)

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1280:
            # supprimer le projectile (hors ecran)
            self.remove()
