import pygame
import sys

def play_dirt_walking():
    pygame.mixer.music.load("audio/SoundEffect/Walking (Dirt).mp3") # Toca a fala
    pygame.mixer.music.play(0)

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def play_denied_entry():
    pygame.mixer.music.load("audio/SoundEffect/DeniedEntry.mp3") # Toca a fala
    pygame.mixer.music.play(0)

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()   

def play_sucess():
    pygame.mixer.music.load("audio/SoundEffect/Sucess.mp3") # Toca a fala
    pygame.mixer.music.play(0)

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()   