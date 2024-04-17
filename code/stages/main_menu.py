import pygame

def main_menu(screen, screen_width, screen_height):
    background = pygame.image.load("images/MainTitle/TitleScreenBg.png").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    title = pygame.image.load("images/MainTitle/GameTitle.png").convert_alpha()
    title_rect = title.get_rect()
    title_rect.centerx = screen_width / 2
    title_rect.top = 25

    studio_logo = pygame.image.load("images/MainTitle/GameStudioLogo.png").convert_alpha()
    studio_logo_rect = studio_logo.get_rect()
    studio_logo_rect.centerx = screen_width / 2
    studio_logo_rect.bottom = screen_height

    title_start_button = pygame.image.load("images/MainTitle/TitleStartButton.png").convert_alpha()
    title_start_button_rect = title_start_button.get_rect()
    title_start_button_rect.center = (screen_width // 2, screen_height // 2 + 50)

    title_exit_button = pygame.image.load("images/MainTitle/TitleExitButton.png").convert_alpha()
    title_exit_button_rect = title_exit_button.get_rect()
    title_exit_button_rect.center = (screen_width // 2, screen_height // 2 + 150)

    screen.blit(background, (0, 0))
    screen.blit(title, title_rect)
    screen.blit(studio_logo, studio_logo_rect)
    screen.blit(title_start_button, title_start_button_rect)
    screen.blit(title_exit_button, title_exit_button_rect)

    return title_start_button_rect, title_exit_button_rect
