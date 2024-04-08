import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the background image
background = pygame.image.load("images/MainScreenBg.jpg").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

title = pygame.image.load("images/GameTitle.png").convert_alpha()
title_rect = title.get_rect()
title_rect.centerx = screen_width / 2
title_rect.top = 75

studio_logo = pygame.image.load("images/GameStudioLogo.png").convert_alpha()
studio_logo_rect = studio_logo.get_rect()
studio_logo_rect.centerx = screen_width / 2
studio_logo_rect.bottom = screen_height

title_button = pygame.image.load("images/TitleStartButton.png").convert_alpha()
title_button_rect = title_button.get_rect()
title_button_rect.center = (screen_width // 2, screen_height // 2 + 50)

cutscene_bg = pygame.image.load("images/Cutscene01.jpg").convert()
cutscene_bg = pygame.transform.scale(cutscene_bg, (screen_width, screen_height))

pygame.mixer.music.load("audio/AudioBgTitulo.mp3")
pygame.mixer.music.play(-1)

currentScreen = "TitleScreen"

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and title_button_rect.collidepoint(event.pos):
            currentScreen = "Cutscene01"
            pygame.mixer.music.load("audio/AudioEntryCutsceneSection.mp3")
            pygame.mixer.music.play(-1)

    # Blit the background image onto the screen
    if currentScreen == "TitleScreen":
        screen.blit(background, (0, 0))
        screen.blit(title, title_rect)
        screen.blit(studio_logo, studio_logo_rect)
        screen.blit(title_button, title_button_rect)
    elif currentScreen == "Cutscene01":
        screen.blit(cutscene_bg, (0, 0))



    # Update the display
    pygame.display.update()