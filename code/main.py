import pygame
import sys
from text import display_dialogue, display_highlight_text
from surface import highlight_area
from stages.main_menu import main_menu
from stages.chapter_selection import chapter_selection_first_chapter, chapter_selection_second_chapter
import moviepy.editor

pygame.init()



# ===== CONSTANTES =====
chapter_selection_big_font = pygame.font.Font("fonts/ShareTech-Regular.ttf", 48)
chapter_selection_small_font = pygame.font.Font("fonts/ShareTech-Regular.ttf", 24)
text_entry_font = pygame.font.Font("fonts/ShareTech-Regular.ttf", 24)
game_font = pygame.font.Font("fonts/AdventPro-VariableFont_wdth,wght.ttf", 32)
highlight_font = pygame.font.Font("fonts/AdventPro-VariableFont_wdth,wght.ttf", 28)

# Configurações Iniciais de Tela
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AgroMistery")



# ===== IMAGENS =====
# Introdução
note = pygame.image.load("images/Bilhete.png").convert_alpha()
note_rect = note.get_rect()
note_rect.centerx = screen_width / 2
note_rect.centery = screen_height / 2


# Primeira Cenas
first_scene_arrival = pygame.image.load("images/Arrival.jpeg").convert()
first_scene_arrival = pygame.transform.scale(first_scene_arrival, (screen_width, screen_height))
first_scene_right_area = pygame.Rect(700, 50, 400, 550)
first_scene_left_area = pygame.Rect(25, 70, 500, 500)
first_scene_center_area = pygame.Rect(500, 300, 225, 75)


# Segunda Cena
second_scene = pygame.image.load("images/NextScene.jpeg").convert()
second_scene = pygame.transform.scale(second_scene, (screen_width, screen_height))



# ===== MAIN LOOP =====

# Configurações Antes do Loop
pygame.mixer.music.load("audio/AudioBgTitulo.mp3")
pygame.mixer.music.play(-1)

currentScreen = "TitleScreen"
chapterSelection = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and title_start_button_rect.collidepoint(event.pos) and currentScreen == "TitleScreen":
            currentScreen = "ChapterSelection"
            chapter_selection = 1
            pygame.mixer.music.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN and title_exit_button_rect.collidepoint(event.pos) and currentScreen == "TitleScreen":
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and chapter01_button_rect.collidepoint(event.pos) and currentScreen == "ChapterSelection":
            currentScreen = "PreGameTransition"
            video = moviepy.editor.VideoFileClip("video/Intro.mp4")
            video.preview()
            screen.fill((0, 0, 0))
            #pygame.mixer.music.load("audio/AudioTextEntry.mp3")
            #pygame.mixer.music.play(-1)
        elif event.type == pygame.MOUSEBUTTONDOWN and chapter01_set_right_rect.collidepoint(event.pos) and currentScreen == "ChapterSelection":
            chapter_selection = 2
        elif event.type == pygame.MOUSEBUTTONDOWN and chapter02_set_left_rect.collidepoint(event.pos) and currentScreen == "ChapterSelection":
            chapter_selection = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and first_scene_left_area.collidepoint(event.pos) and currentScreen == "Entry":
            display_dialogue("Pelo visto, o único jeito é seguir em frente.", game_font, screen_width, screen_height, screen)
            currentScreen = "Hall"
        elif event.type == pygame.MOUSEBUTTONDOWN and first_scene_right_area.collidepoint(event.pos) and currentScreen == "Entry":
            display_dialogue("Voltar depois de todo o esforço para chegar até aqui me parece\n um desperdício...", game_font, screen_width, screen_height, screen)
        elif event.type == pygame.MOUSEBUTTONDOWN and first_scene_center_area.collidepoint(event.pos) and currentScreen == "Entry":
            display_dialogue("Em estoniano: Aviso! Propriedade privada à frente!\nInvasores serão punidos!", game_font, screen_width, screen_height, screen)

    if currentScreen == "TitleScreen": 
        title_start_button_rect, title_exit_button_rect = main_menu(screen, screen_width, screen_height)
    
    elif currentScreen == "ChapterSelection":
        if chapter_selection == 1:
            chapter01_button_rect, chapter01_set_right_rect = chapter_selection_first_chapter(screen, screen_width, screen_height, 
                                                                                              chapter_selection_big_font, chapter_selection_small_font)
        elif chapter_selection == 2:
            chapter02_set_left_rect = chapter_selection_second_chapter(screen, screen_width, screen_height, 
                                             chapter_selection_big_font, chapter_selection_small_font)
            
    elif currentScreen == "PreGameTransition":
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

        currentScreen = "Entry"         # Sequência

    elif currentScreen == "Entry":
        screen.blit(first_scene_arrival, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        if first_scene_right_area.collidepoint(mouse_pos):
            highlight_area(first_scene_right_area, screen)
            display_highlight_text(mouse_pos, highlight_font, "Ir Embora?", screen)
        if first_scene_left_area.collidepoint(mouse_pos):
            highlight_area(first_scene_left_area, screen)
            display_highlight_text(mouse_pos, highlight_font, "Entrar na Instalação?", screen)
        if first_scene_center_area.collidepoint(mouse_pos):
            highlight_area(first_scene_center_area, screen)
            display_highlight_text(mouse_pos, highlight_font, "O que está escrito?", screen)


    elif currentScreen == "Hall":
        screen.blit(second_scene, (0, 0))

    pygame.display.update()