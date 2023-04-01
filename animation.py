import pygame

# definir une classe qui va  s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la creation de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load("/Users/Thomas/PycharmProjects/game/assets/" + sprite_name + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # pour commencer l'animation de l'image a 0
        self.images = animation.get(sprite_name)
        self.animation = False

    # definir methode pour demarer
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:
            # passer a l'image suivante'
            self.current_image += 1

            # verifier si la fin de l'animation est  atteinte
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0
                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image de precedentepar la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger des 24 images dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier
    path = "/Users/Thomas/PycharmProjects/game/assets/" + sprite_name + "/" + sprite_name

    # boucler sur chaque images dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer liste d'image
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque personnages
# mummy -> [...mummy1.png, ...mummy2.png, ...]
# player -> [...player1.png, ...player2.png, ...]
animation = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
}