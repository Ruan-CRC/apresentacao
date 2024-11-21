import pygame

def load_images(screen_width, screen_height):
    
    road_image = pygame.image.load('Imagens/rua-1.jpg')
    road_image = pygame.transform.scale(road_image, (screen_width, screen_height))
    
    actor_image = pygame.image.load('Imagens/gali.png')
    actor_image = pygame.transform.scale(actor_image, (60, 60))
    
    car_images = [pygame.image.load(f"Imagens/car-{i}.png").convert_alpha() for i in range(1, 4)]
    car_images = [pygame.transform.scale(car_image, (60, 40)) for car_image in car_images]
    
    exp_images = [pygame.image.load(f"Imagens/exp2_0{i}.png").convert_alpha() for i in range(1, 5)]
    
    heart_image = pygame.image.load('Imagens/coracao.png')
    return road_image, actor_image, car_images, exp_images, heart_image
