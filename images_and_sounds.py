import pygame

def load_images(screen_width, screen_height):
    
    road_image = pygame.image.load('Imagens/estrada.png')
    road_image = pygame.transform.scale(road_image, (screen_width, screen_height))
    
    actor_image = pygame.image.load('Imagens/ator-1.png')
    actor_image = pygame.transform.scale(actor_image, (40, 40))
    
    car_images = [pygame.image.load(f"Imagens/carro-{i}.png").convert_alpha() for i in range(1, 4)]
    car_images = [pygame.transform.scale(car_image, (60, 40)) for car_image in car_images]
    
    exp_images = [pygame.image.load(f"Imagens/exp2_0{i}.png").convert_alpha() for i in range(1, 5)]
    
    heart_image = pygame.image.load('Imagens/coracao.png')
    return road_image, actor_image, car_images, exp_images, heart_image

def load_sounds():
    collision_sound = pygame.mixer.Sound('sons/explosao.mp3')
    point_sound = pygame.mixer.Sound('sons/pontos.wav')
    scream_sound = pygame.mixer.Sound('sons/grito.mp3')
    
    # Ajustar o volume dos sons (valor entre 0.0 e 1.0)
    collision_sound.set_volume(0.1)  
    point_sound.set_volume(0.1)      
    scream_sound.set_volume(0.1)     
    
    return collision_sound, point_sound, scream_sound


# Função para carregar e tocar a música de fundo
def play_background_music():
    pygame.mixer.music.load("sons/trilha2.mp3")  # Substitua com o caminho do seu arquivo de música
    pygame.mixer.music.set_volume(0.1)  # Ajuste o volume (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # -1 significa que a música vai tocar em loop infinito
