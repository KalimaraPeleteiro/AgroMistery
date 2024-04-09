import pygame
import sys
from text import display_text

pygame.init()

# Constantes
text_entry_list = [
    "Em 2022, cinco jovens visionários fundaram uma nova empresa: A AgroConnect.",
    "Valendo-se de suas inovações tecnológicas, a AgroConnect cresceu rapidamente, entrando no palco internacional.",
    "Em 2024, a AgroConnect ultrapassou a Macrosoft, tornando-se a empresa mais valiosa do mundo.",
    "No entanto, em 2026, um processo judicial foi aberto.",
    "Em 2027, a AgroConnect foi forçadamente fechada, seus bens consfiscados, e seus donos, caçados.",
    "Desde então, mais de 30 anos se passaram.",
    "Trinta anos, até então, sem respostas sobre os motivos para o ocorrido.",
    "O que aconteceu com a AgroConnect?"
]

text_entry_font = pygame.font.Font("fonts/ShareTech-Regular.ttf", 24)

# Parâmetros Iniciais
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# == Imagens ==
background = pygame.image.load("images/TitleScreenBg.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

title = pygame.image.load("images/GameTitle.png").convert_alpha()
title_rect = title.get_rect()
title_rect.centerx = screen_width / 2
title_rect.top = 25

studio_logo = pygame.image.load("images/GameStudioLogo.png").convert_alpha()
studio_logo_rect = studio_logo.get_rect()
studio_logo_rect.centerx = screen_width / 2
studio_logo_rect.bottom = screen_height

title_button = pygame.image.load("images/TitleStartButton.png").convert_alpha()
title_button_rect = title_button.get_rect()
title_button_rect.center = (screen_width // 2, screen_height // 2 + 50)

pygame.mixer.music.load("audio/AudioBgTitulo.mp3")
pygame.mixer.music.play(-1)

currentScreen = "TitleScreen"
fade_alpha = 255

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and title_button_rect.collidepoint(event.pos):
            currentScreen = "PreGame"
            pygame.mixer.music.load("audio/AudioTextEntry.mp3")
            pygame.mixer.music.play(-1)

    if fade_alpha > 0:
        fade_surface = pygame.Surface((screen_width, screen_height))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha -= 0.1

    if currentScreen == "TitleScreen": 
        screen.blit(background, (0, 0))
        screen.blit(title, title_rect)
        screen.blit(studio_logo, studio_logo_rect)
        screen.blit(title_button, title_button_rect)
    elif currentScreen == "PreGame":
        display_text(text_entry_list, text_entry_font, screen, screen_width, screen_height)
        currentScreen = "Entry"
        fade_alpha = 255
    elif currentScreen == "Entry":
        pygame.mixer.music.stop()
        screen.blit(background, (0, 0))

    # Update the display
    pygame.display.update()