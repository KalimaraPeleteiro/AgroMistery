import pygame
from text import display_highlight_text
from surface import highlight_area

def entry(screen, screen_width, screen_height, dialogue_font):

    first_scene_arrival = pygame.image.load("images/Entry/Arrival.jpeg").convert()
    first_scene_arrival = pygame.transform.scale(first_scene_arrival, (screen_width, screen_height))
    first_scene_right_area = pygame.Rect(700, 50, 400, 550)
    first_scene_left_area = pygame.Rect(25, 70, 500, 500)
    first_scene_center_area = pygame.Rect(500, 300, 225, 75)

    screen.blit(first_scene_arrival, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    if first_scene_right_area.collidepoint(mouse_pos):
        highlight_area(first_scene_right_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Ir Embora?", screen)
    if first_scene_left_area.collidepoint(mouse_pos):
        highlight_area(first_scene_left_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir em frente?", screen)
    if first_scene_center_area.collidepoint(mouse_pos):
        highlight_area(first_scene_center_area, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que está escrito?", screen)
    
    return first_scene_left_area, first_scene_center_area, first_scene_right_area