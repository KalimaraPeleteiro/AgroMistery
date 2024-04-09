import pygame


# Função para expor o texto de introdução (História da AgroConnect, o que ocorreu...)
def display_text_entry(text_list, font, screen, width, height):
    text_delay = 60

    for sentence in text_list:
        for i in range(len(sentence) + 1):
            screen.fill((0, 0, 0))
            text = font.render(sentence[:i], True, (255, 255, 255))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            screen.blit(text, text_rect)

            pygame.display.update()
            pygame.time.wait(text_delay)

        pygame.time.wait(1000)


# Função de Diálogo em Cenas.
def display_dialogue(dialogue_text, font, screen_width, screen_height, screen, text_color = (0, 0, 0)):
    dialogue_box_width = screen_width - 100
    dialogue_box_height = 100
    dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA) # SRCALPHA para transparência
    dialogue_box.fill((250, 250, 250, 25))  # Caixa Transparente, possível mudar no futuro.
    dialogue_rect = dialogue_box.get_rect(center=(screen_width // 2, screen_height - dialogue_box_height // 2))
    
    lines = dialogue_text.split('\n')
    y = dialogue_rect.top + 30
    for line in lines:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(dialogue_rect.centerx, y))
        screen.blit(text_surface, text_rect)
        y += 30
    
    screen.blit(dialogue_box, dialogue_rect)
    pygame.display.flip()
    pygame.time.wait(3000)   # 03 Segundos