import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("/Users/Thomas/PycharmProjects/game/assets/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("/Users/Thomas/PycharmProjects/game/assets/sounds/game_over.ogg"),
            "meteorite": pygame.mixer.Sound("/Users/Thomas/PycharmProjects/game/assets/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("/Users/Thomas/PycharmProjects/game/assets/sounds/tir.ogg")
        }

    def play(self, name):
        self.sounds[name].play()