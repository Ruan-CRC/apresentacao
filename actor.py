import pygame
from images_and_sounds import *


class Actor:
    def __init__(self, x, y, image, speed=3):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.points = 0
        self.lives = 3

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.can_move():
                self.y += self.speed

    def check_collision(self, cars):
        for car in cars:
            if car.collides_with(self.x, self.y):
                self.reset_position()
                return True
        return False

    def reset_position(self):
        self.y = 560

    def can_move(self):
        return self.y < 560

    def increment_points(self):
        if self.y < 15:
            self.points += 1
            self.reset_position()

    def draw_lives(self, screen, heart_image):
        for i in range(self.lives):
            screen.blit(heart_image, (400 + i * 20, 18))
    
    
