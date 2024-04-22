import pygame
from text import display_highlight_text
from surface import highlight_area


def stage01_hall(screen, screen_width, screen_height, dialogue_font):
    hall = pygame.image.load("images/Stage01/Hall01.jpeg").convert()
    hall = pygame.transform.scale(hall, (screen_width, screen_height))

    screen.blit(hall, (0, 0))

    hall_first_path = pygame.Rect(350, 375, 35, 70)
    hall_second_path = pygame.Rect(380, 375, 35, 70)
    hall_third_path = pygame.Rect(605, 375, 35, 70)
    hall_fourth_path = pygame.Rect(640, 375, 35, 70)
    mouse_pos = pygame.mouse.get_pos()

    if hall_first_path.collidepoint(mouse_pos):
        highlight_area(hall_first_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    if hall_second_path.collidepoint(mouse_pos):
        highlight_area(hall_second_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    if hall_third_path.collidepoint(mouse_pos):
        highlight_area(hall_third_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    if hall_fourth_path.collidepoint(mouse_pos):
        highlight_area(hall_fourth_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    
    return hall_first_path, hall_second_path, hall_third_path, hall_fourth_path


def stage02_01(screen, screen_width, screen_height, dialogue_font):
    dead_end = pygame.image.load("images/Stage01/Path02-01.jpeg").convert()
    dead_end = pygame.transform.scale(dead_end, (screen_width, screen_height))

    screen.blit(dead_end, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    dead_end_back = pygame.Rect(0, screen_height - 75, screen_width, 75)

    if dead_end_back.collidepoint(mouse_pos):
        highlight_area(dead_end_back, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    
    return dead_end_back


def stage03_01(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path03-01.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(800, 150, 200, 350)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, next_step


def stage03_02(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Path03-02.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    symbol = pygame.Rect(400, 250, 190, 200)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if symbol.collidepoint(mouse_pos):
        highlight_area(symbol, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    
    return back_option, symbol
