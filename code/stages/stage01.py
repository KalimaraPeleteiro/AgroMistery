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


def stage02_hall(screen, screen_width, screen_height, dialogue_font):
    hall = pygame.image.load("images/Stage01/Hall02.jpeg").convert()
    hall = pygame.transform.scale(hall, (screen_width, screen_height))

    screen.blit(hall, (0, 0))

    hall_first_path = pygame.Rect(235, 310, 60, 120)
    hall_second_path = pygame.Rect(350, 310, 60, 120)
    hall_third_path = pygame.Rect(735, 360, 60, 60)
    mouse_pos = pygame.mouse.get_pos()

    if hall_first_path.collidepoint(mouse_pos):
        highlight_area(hall_first_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    if hall_second_path.collidepoint(mouse_pos):
        highlight_area(hall_second_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir esse caminho?", screen)
    if hall_third_path.collidepoint(mouse_pos):
        highlight_area(hall_third_path, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    
    return hall_first_path, hall_second_path, hall_third_path


def stage01_01(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path01-01.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(350, 180, 250, 250)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, next_step


def stage01_02(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Path01-02.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    symbol = pygame.Rect(400, 260, 150, 150)
    next_step = pygame.Rect(50, 250, 200, 320)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if symbol.collidepoint(mouse_pos):
        highlight_area(symbol, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, symbol, next_step


def stage01_03(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path01-03.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(900, 150, 300, 350)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, next_step


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
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    
    return back_option, symbol


def stage04_01(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path04-01.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(950, 80, 150, 450)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, next_step


def stage04_02(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path04-02.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(510, 300, 80, 80)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Seguir?", screen)
    
    return back_option, next_step


def stage04_03(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Path04-03.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    symbol = pygame.Rect(320, 230, 190, 180)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if symbol.collidepoint(mouse_pos):
        highlight_area(symbol, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    
    return back_option, symbol


def stage05_01(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path05-01.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    next_step = pygame.Rect(750, 100, 180, 450)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, next_step


def stage05_02(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Path05-02.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)
    symbol = pygame.Rect(850, 170, 200, 250)
    next_step = pygame.Rect(750, 210, 100, 250)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if symbol.collidepoint(mouse_pos):
        highlight_area(symbol, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if next_step.collidepoint(mouse_pos):
        highlight_area(next_step, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Continuar?", screen)
    
    return back_option, symbol, next_step


def stage05_03(screen, screen_width, screen_height, dialogue_font):
    passage = pygame.image.load("images/Stage01/Path05-03.jpeg").convert()
    passage = pygame.transform.scale(passage, (screen_width, screen_height))

    screen.blit(passage, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 75, screen_width, 75)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    
    return back_option


def stage06_01(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Path06-01.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(710, 250, 200, 250)
    message_code = pygame.Rect(250, 260, 200, 150)
    message_biblic = pygame.Rect(920, 190, 150, 160)
    door = pygame.Rect(450, 260, 140, 220)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if message_code.collidepoint(mouse_pos):
        highlight_area(message_code, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if message_biblic.collidepoint(mouse_pos):
        highlight_area(message_biblic, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if door.collidepoint(mouse_pos):
        highlight_area(door, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    
    return back_option, message_code, message_biblic, door


def stage01_door(screen, screen_width, screen_height, dialogue_font):
    background = pygame.image.load("images/Stage01/Door.jpeg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    back_option = pygame.Rect(0, screen_height - 50, screen_width, 50)
    try_open = pygame.Rect(780, 500, 70, 140)
    panel = pygame.Rect(520, 180, 250, 280)
    fingerprint = pygame.Rect(520, 460, 250, 100)

    if back_option.collidepoint(mouse_pos):
        highlight_area(back_option, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Voltar?", screen)
    if try_open.collidepoint(mouse_pos):
        highlight_area(try_open, screen)
        display_highlight_text(mouse_pos, dialogue_font, "Tentar Abrir", screen)
    if panel.collidepoint(mouse_pos):
        highlight_area(panel, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    if fingerprint.collidepoint(mouse_pos):
        highlight_area(fingerprint, screen)
        display_highlight_text(mouse_pos, dialogue_font, "O que é isso?", screen)
    
    return back_option, try_open, panel, fingerprint