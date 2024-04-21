import pygame
import sys
from text import display_dialogue
from sound import play_dirt_walking
import moviepy.editor

from stages.main_menu import main_menu
from stages.chapter_selection import chapter_selection_first_chapter, chapter_selection_second_chapter
from stages.pre_game_transition import pre_game_transition
from stages.entry import entry
from stages.entrance import entrance

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



# ===== MAIN LOOP =====

# Configurações Antes do Loop
#pygame.mixer.music.load("audio/AudioBgTitulo.mp3")
#pygame.mixer.music.play(-1)

currentScreen = "Entrance"
chapterSelection = 0
while True:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if currentScreen == "TitleScreen":
            if event.type == pygame.MOUSEBUTTONDOWN and title_start_button_rect.collidepoint(event.pos):
                currentScreen = "ChapterSelection"
                chapter_selection = 1
                pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN and title_exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        elif currentScreen == "ChapterSelection":
            if event.type == pygame.MOUSEBUTTONDOWN and chapter01_button_rect.collidepoint(event.pos):
                currentScreen = "PreGameTransition"
                video = moviepy.editor.VideoFileClip("video/Intro.mp4")
                video.preview()
                screen.fill((0, 0, 0))
            elif event.type == pygame.MOUSEBUTTONDOWN and chapter01_set_right_rect.collidepoint(event.pos):
                chapter_selection = 2
            elif event.type == pygame.MOUSEBUTTONDOWN and chapter02_set_left_rect.collidepoint(event.pos):
                chapter_selection = 1

        elif currentScreen == "Entry":
            if event.type == pygame.MOUSEBUTTONDOWN and first_scene_left_area.collidepoint(event.pos):
                display_dialogue("Pelo visto, o único jeito é seguir em frente.", game_font, screen_width, screen_height, screen)
                currentScreen = "Entrance"
                play_dirt_walking()

            elif event.type == pygame.MOUSEBUTTONDOWN and first_scene_right_area.collidepoint(event.pos):
                display_dialogue("Voltar depois de todo o esforço para chegar até aqui me parece\n um desperdício...", game_font, screen_width, screen_height, screen)
            elif event.type == pygame.MOUSEBUTTONDOWN and first_scene_center_area.collidepoint(event.pos):
                display_dialogue("Em estoniano: Aviso! Propriedade privada à frente!\nInvasores serão punidos!", game_font, screen_width, screen_height, screen)

        elif currentScreen == "Entrance":
            if event.type == pygame.MOUSEBUTTONDOWN and entry_return_area.collidepoint(event.pos):
                currentScreen = "Entry"
            if event.type == pygame.MOUSEBUTTONDOWN and entry_left_area.collidepoint(event.pos):
                display_dialogue("O dispositivo de reconhecimento facial que usávamos\npara autenticação. Agora, sem energia, é impossível usá-lo.", game_font, screen_width, screen_height, screen)
            if event.type == pygame.MOUSEBUTTONDOWN and entry_top_area.collidepoint(event.pos):
                display_dialogue("Em estoniano: 'Entrada 64B'", game_font, screen_width, screen_height, screen)
            if event.type == pygame.MOUSEBUTTONDOWN and entry_right_area.collidepoint(event.pos):
                display_dialogue("Em estoniano: 'Amigos, não podemos nos render a essa opressão! Lutaremos\npelos nossos direitos. Compareçam todos ao local de reunião em Tállin!\nPor melhores reinvidicações!'", game_font, screen_width, screen_height, screen, wait_period=5000)
                display_dialogue("O primeiro sinal de crise de uma empresa sempre serão as greves.\nLembro como se fosse hoje. Parecia um pesadelo.", game_font, screen_width, screen_height, screen)
                display_dialogue("Se não me engano, a greve durou por volta de 64 dias...", game_font, screen_width, screen_height, screen)
            if event.type == pygame.MOUSEBUTTONDOWN and entry_center_area.collidepoint(event.pos):
                display_dialogue("Sem energia, eu posso simplesmente seguir em frente,\npelo visto.", game_font, screen_width, screen_height, screen)
                play_dirt_walking()
                currentScreen = "Next"

    # Loops de Tela
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
        pre_game_transition(screen, screen_width, screen_height)
        currentScreen = "Entry"         # Sequência

    elif currentScreen == "Entry":
        first_scene_left_area, first_scene_center_area, first_scene_right_area = entry(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Entrance":
        entry_return_area, entry_left_area, entry_right_area, entry_top_area, entry_center_area = entrance(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Next":
        next_image = pygame.image.load("images/Pathways02.jpeg").convert()
        next_image = pygame.transform.scale(next_image, (screen_width, screen_height))

        screen.blit(next_image, (0, 0))

    pygame.display.update()