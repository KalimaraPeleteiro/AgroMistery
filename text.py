import pygame

def display_text(text_list, font, screen, width, height):
    text_surface = None
    text_index = 0
    text_delay = 60

    for sentence in text_list:
        for i in range(len(sentence) + 1):
            screen.fill((0, 0, 0))
            text = font.render(sentence[:i], True, (255, 255, 255))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            screen.blit(text, text_rect)

            pygame.display.update()
            pygame.time.wait(text_delay)

        pygame.time.wait(1000)  # Wait for a brief moment between sentences