import pygame
from actor import Actor
from car import Car
from images_and_sounds import load_images, load_sounds
from timer import Timer

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Freeway")

# Carregar imagens e sons
road_image, actor_image, car_images, heart_image = load_images()
collision_sound, point_sound, scream_sound = load_sounds()

# Configurações do ator e carros
actor = Actor(100, 366, actor_image)
cars = [Car(600, y, car_images[i], 2 + i * 0.3) for i, y in enumerate([40, 96, 150, 210, 270, 318])]

# Timer do jogo
timer = Timer(40 * 1000)

# Loop principal do jogo
running = True
while running:
    screen.fill((0, 0, 0))  # Limpar a tela

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar o estado do jogo
    actor.move()
    for car in cars:
        car.move()
        car.reset_position()

    # Verificar colisão
    if actor.check_collision(cars):
        collision_sound.play()
        scream_sound.play()
        actor.lives -= 1
        if actor.lives == 0:
            running = False

    # Aumentar pontos
    actor.increment_points()

    # Exibir a tela de jogo
    screen.blit(road_image, (0, 0))
    actor.draw(screen)
    actor.draw_lives(screen, heart_image)
    for car in cars:
        car.draw(screen)

    # Exibir o temporizador
    timer.display(screen)

    # Verificar fim de jogo
    if timer.is_time_up() or actor.lives == 0:
        font = pygame.font.SysFont(None, 40)
        end_text = font.render("Fim de Jogo!", True, (255, 0, 0))
        screen.blit(end_text, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 20))

    # Atualizar a tela
    pygame.display.update()

# Finalizar o Pygame
pygame.quit()
