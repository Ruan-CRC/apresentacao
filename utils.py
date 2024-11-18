import pygame

def draw_button(text, x, y, width, height, font, color, hover_color, screen, action=None):
    """
    Desenha um botão interativo na tela.

    Args:
        text (str): Texto exibido no botão.
        x (int): Posição X do canto superior esquerdo do botão.
        y (int): Posição Y do canto superior esquerdo do botão.
        width (int): Largura do botão.
        height (int): Altura do botão.
        font (pygame.font.Font): Fonte do texto.
        color (tuple): Cor do botão (R, G, B).
        hover_color (tuple): Cor do botão ao passar o mouse (R, G, B).
        screen (pygame.Surface): Superfície onde o botão será desenhado.
        action (callable, optional): Função a ser chamada ao clicar no botão.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Verifica se o mouse está sobre o botão
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    
    # Renderizar texto no botão
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

