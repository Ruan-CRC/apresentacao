import pygame

class Car:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.width = 50
        self.height = 40

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x -= self.speed

    def reset_position(self):
        if self.x < -50:
            self.x = 600

    def collides_with(self, actor_x, actor_y):
        return self.x < actor_x + 15 < self.x + self.width and self.y < actor_y + 15 < self.y + self.height
