import pygame

pygame.mixer.init()
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
        # Movimento para cima
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        # Movimento para baixo
        if keys[pygame.K_DOWN] and self.y < 560:  # Evita ultrapassar o limite inferior
            self.y += self.speed
        # Movimento para a esquerda
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        # Movimento para a direita
        if keys[pygame.K_RIGHT] and self.x < 800 - self.image.get_width():  # Evita ultrapassar o limite direito
            self.x += self.speed


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
    
    
