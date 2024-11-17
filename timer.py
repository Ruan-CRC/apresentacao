import pygame
from pygame.locals import *

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def get_remaining_time(self):
        return max(0, self.duration - (pygame.time.get_ticks() - self.start_time))

    def display(self, screen):
        remaining_time = self.get_remaining_time() // 1000
        font = pygame.font.SysFont(None, 25)
        time_text = font.render(f'Tempo: {remaining_time}s', True, (255, 240, 60))
        screen.blit(time_text, (250, 27))

    def is_time_up(self):
        return self.get_remaining_time() == 0
