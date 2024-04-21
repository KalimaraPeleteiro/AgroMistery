import pygame


# Função de Diálogo em Cenas.
def display_dialogue(dialogue_text, font, screen_width, screen_height, screen, text_color = (255, 255, 255)):
    dialogue_box = pygame.image.load("images/DialogueBox.png").convert_alpha()
    dialogue_box_rect = dialogue_box.get_rect()
    dialogue_box_rect.centerx = screen_width / 2
    dialogue_box_rect.bottom = screen_height
    dialogue_rect = dialogue_box.get_rect(center=(screen_width // 2, screen_height - 100 // 2))

    lines = dialogue_text.split('\n')
    y = dialogue_rect.top + 30
    screen.blit(dialogue_box, dialogue_rect)
    for line in lines:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(dialogue_rect.centerx, y))
        screen.blit(text_surface, text_rect)
        y += 30
    
    pygame.display.flip()
    pygame.time.wait(3000)   # 03 Segundos


def display_highlight_text(mouse_pos, font, text, screen):
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = (mouse_pos[0] - 50, mouse_pos[1] - 50)  # Posição do texto ao lado do mouse
    screen.blit(text, text_rect)  # Renderiza o texto