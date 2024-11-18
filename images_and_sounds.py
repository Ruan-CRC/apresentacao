import pygame

def load_images(screen_width, screen_height, car_size = (60, 40)):
    road_image = pygame.image.load('Imagens/estrada.png')
    road_image = pygame.transform.scale(road_image, (screen_width, screen_height))
    actor_image = pygame.image.load('Imagens/ator-1.png')
    actor_image = pygame.transform.scale(actor_image, (40, 40))
    car1_image = pygame.image.load('Imagens/carro-1.png')
    car1_image = pygame.transform.scale(car1_image, car_size)
    car2_image = pygame.image.load('Imagens/carro-2.png')
    car2_image = pygame.transform.scale(car2_image, car_size)
    car3_image = pygame.image.load('Imagens/carro-3.png')
    car3_image = pygame.transform.scale(car3_image, car_size)
    heart_image = pygame.image.load('Imagens/coracao.png')
    return road_image, actor_image, [car1_image, car2_image, car3_image], heart_image
40
def load_sounds():
    collision_sound = pygame.mixer.Sound('sons/explosao.mp3')
    point_sound = pygame.mixer.Sound('sons/pontos.wav')
    scream_sound = pygame.mixer.Sound('sons/grito.mp3')
    return collision_sound, point_sound, scream_sound

# Função para carregar e tocar a música de fundo
def play_background_music():
    pygame.mixer.music.load("sons/trilha2.mp3")  # Substitua com o caminho do seu arquivo de música
    pygame.mixer.music.set_volume(0.1)  # Ajuste o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # -1 significa que a música vai tocar em loop infinito
