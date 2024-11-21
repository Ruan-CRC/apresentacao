import pygame
from ator import Actor
from carro import Car
from public import load_images
from timer import Timer
from utils import draw_button
from explosao import Explosion

# Inicialização do Pygame
def init_pygame():
    pygame.init()
    pygame.mixer.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Constantes de Configuração
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FPS = 60

# Classe Principal do Jogo
class Game:
    def __init__(self):
        self.screen = init_pygame()
        pygame.display.set_caption("Jogo Freeway")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_active = True
        self.score_font = pygame.font.SysFont(None, 40)

        # Recursos do jogo
        self.road_image, self.actor_image, self.car_images, self.exp_images, self.heart_image = load_images(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Configuração inicial do jogo
        self.restart_game()

    def restart_game(self):
        self.actor = Actor(100, SCREEN_HEIGHT - 45, self.actor_image)
        car_positions = [100, 186, 270, 360, 450, 528]
        self.cars = [Car(800, y, self.car_images[i % len(self.car_images)], 2 + i * 0.3) for i, y in enumerate(car_positions)]
        self.timer = Timer(40 * 1000)
        self.explosions = []
        self.game_active = True  # Reinicia o estado ativo do jogo


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_game(self):
        self.actor.move()
        for car in self.cars:
            car.move()
            car.reset_position()

        if self.actor.check_collision(self.cars):
            self.actor.lives -= 1
            self.create_explosions()
            self.actor.points = max(0, self.actor.points - 1)
            if self.actor.lives == 0:
                self.game_active = False

        self.actor.increment_points()
        self.update_explosions()

    def create_explosions(self):
        for car in self.cars:
            if car.collides_with(self.actor.x, self.actor.y):
                self.explosions.append(Explosion(car.x, car.y, self.exp_images))

    def update_explosions(self):
        for explosion in self.explosions:
            explosion.update(pygame.time.get_ticks() / 1000)

    def draw_game(self):
        self.screen.blit(self.road_image, (0, 0))
        self.actor.draw(self.screen)
        self.actor.draw_lives(self.screen, self.heart_image)
        for car in self.cars:
            car.draw(self.screen)
        for explosion in self.explosions:
            explosion.draw(self.screen)
        self.draw_ui()

    def draw_ui(self):
        score_text = self.score_font.render(f"Pontuação: {self.actor.points}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.timer.display(self.screen)

    def draw_game_over(self):
        font = pygame.font.SysFont(None, 60)
        end_text = font.render("Fim de Jogo!", True, (255, 0, 0))
        self.screen.blit(end_text, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 - 100))

        final_score_text = self.score_font.render(f"Sua Pontuação Final: {self.actor.points}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50))

        button_font = pygame.font.SysFont(None, 40)
        draw_button("Reiniciar", SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2, 200, 50,
                    button_font, (0, 255, 0), (0, 200, 0), self.screen, self.restart_game)

    def run(self):
        while self.running:
            self.handle_events()
            if self.game_active:
                self.update_game()
                self.draw_game()
                if self.timer.is_time_up() or self.actor.lives == 0:
                    self.game_active = False
            else:
                self.draw_game_over()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

# Execução do jogo
if __name__ == "__main__":
    game = Game()
    game.run()
