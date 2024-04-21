import pygame
from text import display_highlight_text
from surface import highlight_area


def entrance(screen, screen_width, screen_height, dialogue_font):

    entry_point = pygame.image.load("images/Entrance/EntryPoint.jpeg").convert()
    entry_point = pygame.transform.scale(entry_point, (screen_width, screen_height))

    entry_return_area = pygame.Rect(0, screen_height - 75, screen_width, 75)
    entry_left_area = pygame.Rect(115, 250, 110, 135)
    entry_top_area = pygame.Rect(400, 220, 80, 25)
    entry_right_area = pygame.Rect(650, 250, 150, 150)
    entry_center_area = pygame.Rect(300, 250, 300, 275)

    screen.blit(entry_point, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    if entry_return_area.collidepoint(mouse_pos):
        highlight_area(entry_return_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if entry_left_area.collidepoint(mouse_pos):
        highlight_area(entry_left_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if entry_top_area.collidepoint(mouse_pos):
        highlight_area(entry_top_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que está escrito?", screen)
    if entry_right_area.collidepoint(mouse_pos):
        highlight_area(entry_right_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if entry_center_area.collidepoint(mouse_pos):
        highlight_area(entry_center_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir em frente?", screen)


    return entry_return_area, entry_left_area, entry_right_area, entry_top_area, entry_center_area
