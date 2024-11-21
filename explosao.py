import pygame

class Explosion:
    def __init__(self, x, y, images, duration=100):
        self.x = x
        self.y = y
        self.images = images
        self.image_index = 0
        self.duration = duration
        self.timer = 0
        self.finished = False

    def update(self):
        if self.timer < self.duration:
            self.timer += 1
        else:
            self.finished = True
            self.image_index = len(self.images) - 1  # Última imagem da animação

    def draw(self, screen):
        if not self.finished:
            screen.blit(self.images[self.image_index], (self.x, self.y))

    def next_frame(self):
        if self.image_index < len(self.images) - 1:
            self.image_index += 1
