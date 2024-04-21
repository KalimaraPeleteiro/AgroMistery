import pygame
import sys

def pre_game_transition(screen, screen_width, screen_height):

    note = pygame.image.load("images/Bilhete.png").convert_alpha()
    note_rect = note.get_rect()
    note_rect.centerx = screen_width / 2
    note_rect.centery = screen_height / 2

    first_scene_arrival = pygame.image.load("images/Arrival.jpeg").convert()
    first_scene_arrival = pygame.transform.scale(first_scene_arrival, (screen_width, screen_height))

    pygame.mixer.music.stop()             # Pausa Música
    screen.blit(note, note_rect)          # Trazer bilhete

    start_time = pygame.time.get_ticks()  # Usar pygame.wait iria congelar a tela
        
    # Aguardar 10 segundos (para ler o bilhete)
    while pygame.time.get_ticks() - start_time < 10000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    # Carrega o fundo da próxima cena
    screen.blit(first_scene_arrival, (0, 0)) 
    pygame.mixer.music.load("audio/AudioIntroductionVoice.mp3") # Toca a fala
    pygame.mixer.music.play(0)

    # Espera a fala finalizar para seguir
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()