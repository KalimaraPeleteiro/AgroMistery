import pygame
import sys

def input_box(screen, font):
    input_text = ""
    input_rect = pygame.Rect(20, 100, 500, 60)
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()

    return input_text