import pygame

def load_images():
    road_image = pygame.image.load('Imagens/estrada.png')
    actor_image = pygame.image.load('Imagens/ator-1.png')
    car1_image = pygame.image.load('Imagens/carro-1.png')
    car2_image = pygame.image.load('Imagens/carro-2.png')
    car3_image = pygame.image.load('Imagens/carro-3.png')
    heart_image = pygame.image.load('Imagens/coracao.png')
    return road_image, actor_image, [car1_image, car2_image, car3_image], heart_image

def load_sounds():
    collision_sound = pygame.mixer.Sound('sons/explosao.mp3')
    point_sound = pygame.mixer.Sound('sons/pontos.wav')
    scream_sound = pygame.mixer.Sound('sons/grito.mp3')
    return collision_sound, point_sound, scream_sound

