import pygame

def chapter_selection_first_chapter(screen, screen_width, screen_height, font_big, font_small):
    chapter01 = pygame.image.load("images/Chapter01Bg.jpeg").convert()
    chapter01 = pygame.transform.scale(chapter01, (screen_width, screen_height))

    chapter01_title = font_big.render("Capítulo 01", True, (255, 255, 255))
    chapter01_title_rect = chapter01_title.get_rect(top = 25, left = 25)

    chapter01_description = font_small.render("Mais de 10 anos após o fim da AgroConnect, um de seus", True, (255, 255, 255))
    chapter01_description_rect = chapter01_description.get_rect(top = 300, left = 25)

    chapter01_description02 = font_small.render("antigos funcionários retorna a uma de suas instalações.", True, (255, 255, 255))
    chapter01_description02_rect = chapter01_description02.get_rect(top = 325, left = 25)

    chapter01_button = pygame.image.load("images/ChapterSelection01Button.png").convert_alpha()
    chapter01_button_rect = chapter01_button.get_rect()
    chapter01_button_rect.top = 500
    chapter01_button_rect.left = 25

    chapter01_set_right = pygame.image.load("images/ChapterSelectionSetRight.png").convert_alpha()
    chapter01_set_right_rect = chapter01_set_right.get_rect()
    chapter01_set_right_rect.left = screen_width - 125
    chapter01_set_right_rect.top = screen_height / 2 - 50

    screen.blit(chapter01, (0, 0))
    screen.blit(chapter01_title, chapter01_title_rect)
    screen.blit(chapter01_description, chapter01_description_rect)
    screen.blit(chapter01_description02, chapter01_description02_rect)
    screen.blit(chapter01_button, chapter01_button_rect)
    screen.blit(chapter01_set_right, chapter01_set_right_rect)

    return chapter01_button_rect, chapter01_set_right_rect


def chapter_selection_second_chapter(screen, screen_width, screen_height, font_big, font_small):
    chapter02 = pygame.image.load("images/Chapter02Bg.png").convert()
    chapter02 = pygame.transform.scale(chapter02, (screen_width, screen_height))

    chapter02_title = font_big.render("Capítulo 02", True, (255, 255, 255))
    chapter02_title_rect = chapter02_title.get_rect(top = 25, left = screen_width - 250)

    chapter02_description = font_small.render("Em breve...", True, (255, 255, 255))
    chapter02_description_rect = chapter02_description.get_rect(top = 300, left = screen_width - 125)

    chapter02_set_left = pygame.image.load("images/ChapterSelectionSetLeft.png").convert_alpha()
    chapter02_set_left_rect = chapter02_set_left.get_rect()
    chapter02_set_left_rect.left = 25
    chapter02_set_left_rect.top = screen_height / 2 - 50

    screen.blit(chapter02, (0, 0))
    screen.blit(chapter02_title, chapter02_title_rect)
    screen.blit(chapter02_description, chapter02_description_rect)
    screen.blit(chapter02_set_left, chapter02_set_left_rect)

    return chapter02_set_left_rect