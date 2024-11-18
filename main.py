import pygame
from actor import Actor
from car import Car
from images_and_sounds import *
from timer import Timer
from utils import draw_button

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()  # Inicialize o mixer para sons

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Freeway")

# Carregar imagens e sons
road_image, actor_image, car_images, heart_image = load_images(SCREEN_WIDTH, SCREEN_HEIGHT)
collision_sound, point_sound, scream_sound = load_sounds()

# Tocar música de fundo
play_background_music()

# Função para reiniciar o jogo
def restart_game():
    global actor, cars, timer, game_active
    actor = Actor(100, SCREEN_HEIGHT - 45, actor_image)
    cars = [Car(800, y, car_images[i % len(car_images)], 2 + i * 0.3) for i, y in enumerate([70, 156, 240, 330, 420, 498])]
    timer = Timer(40 * 1000)
    game_active = True

# Configurações iniciais
actor = Actor(100, SCREEN_HEIGHT - 45, actor_image)
cars = [Car(800, y, car_images[i % len(car_images)], 2 + i * 0.3) for i, y in enumerate([70, 156, 240, 330, 420, 498])]
timer = Timer(40 * 1000)

# Estado do jogo
running = True
game_active = True

# Fonte para a pontuação
score_font = pygame.font.SysFont(None, 40)

# Loop principal do jogo
while running:
    screen.fill((0, 0, 0))  # Limpar a tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_active:
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
            if actor.points > 0:
                actor.points -= 1
            if actor.lives == 0:
                game_active = False

        # Aumentar pontos
        actor.increment_points()
        

        # Exibir a tela de jogo
        screen.blit(road_image, (0, 0))
        actor.draw(screen)
        actor.draw_lives(screen, heart_image)
        for car in cars:
            car.draw(screen)
            
        # Exibir a pontuação
        score_text = score_font.render(f"Pontuação: {actor.points}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Exibir o temporizador
        timer.display(screen)

        # Verificar fim de jogo
        if timer.is_time_up() or actor.lives == 0:
            game_active = False
    else:
        # Tela de fim de jogo
        font = pygame.font.SysFont(None, 60)
        end_text = font.render("Fim de Jogo!", True, (255, 0, 0))
        screen.blit(end_text, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 - 100))

        # Exibir a pontuação final
        final_score_text = score_font.render(f"Sua Pontuação Final: {actor.points}", True, (255, 255, 255))
        screen.blit(final_score_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50))

        # Botão de reiniciar
        button_font = pygame.font.SysFont(None, 40)
        draw_button("Reiniciar", SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2, 200, 50, 
                    button_font, (0, 255, 0), (0, 200, 0), screen, restart_game)


    # Atualizar a tela
    pygame.display.update()

# Finalizar o Pygame
pygame.quit()
