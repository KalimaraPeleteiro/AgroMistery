import pygame
import sys
import moviepy.editor

from text import display_dialogue
from sound import play_dirt_walking, play_denied_entry, play_sucess
from input_text import input_box    

from stages.main_menu import main_menu
from stages.chapter_selection import chapter_selection_first_chapter, chapter_selection_second_chapter
from stages.pre_game_transition import pre_game_transition
from stages.entry import entry
from stages.entrance import entrance
from stages.stage01 import *

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

currentScreen = "Stage06-01"
chapterSelection = 0
checkpoint_find_passage = False
checkpoint_find_door = False
stage01_passcode = False
stage01_pass = False

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
                currentScreen = "Stage01-Passage"
        
        elif currentScreen == "Stage01-Passage":
            play_dirt_walking()
            display_dialogue("Andando pela instalação, era claro que ninguém havia passado\npor ali havia anos. Nenhuma instalação possuía energia, e as plantas\n haviam invadido quase todos os cômodos.", game_font, screen_width, screen_height, screen, wait_period=5000)
            display_dialogue("Passeano pelo recinto, chegava-se eventualmente a um hub\nque conectava os caminhos para todas as áreas.", game_font, screen_width, screen_height, screen, wait_period=5000)
            display_dialogue("Se existe mesmo algo escondido, deve estar aqui. É hora de procurar.", game_font, screen_width, screen_height, screen, wait_period=5000)
            play_dirt_walking()
            currentScreen = "Stage01-Hall01"
        
        elif currentScreen == "Stage01-Hall01":
            if event.type == pygame.MOUSEBUTTONDOWN and hall_first_path.collidepoint(event.pos):
                currentScreen = "Stage01-01"
            if event.type == pygame.MOUSEBUTTONDOWN and hall_second_path.collidepoint(event.pos):
                currentScreen = "Stage02-01"
            if event.type == pygame.MOUSEBUTTONDOWN and hall_third_path.collidepoint(event.pos):
                currentScreen = "Stage03-01"
            if event.type == pygame.MOUSEBUTTONDOWN and hall_fourth_path.collidepoint(event.pos):
                currentScreen = "Stage04-01"
        
        elif currentScreen == "Stage01-Hall02":
            if event.type == pygame.MOUSEBUTTONDOWN and hall_first_path.collidepoint(event.pos):
                currentScreen = "Stage01-03"
            if event.type == pygame.MOUSEBUTTONDOWN and hall_second_path.collidepoint(event.pos):
                currentScreen = "Stage05-01"
            if event.type == pygame.MOUSEBUTTONDOWN and hall_third_path.collidepoint(event.pos):
                if not checkpoint_find_passage:
                    display_dialogue("Movendo o entulho para o lado, é possível\ndistinguir uma passagem estreita para uma área secreta.", game_font, screen_width, screen_height, screen, wait_period=4000)
                    display_dialogue("O que é isso?", game_font, screen_width, screen_height, screen, wait_period=4000)
                    checkpoint_find_passage = True
                currentScreen = "Stage06-01"
        
        elif currentScreen == "Stage01-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall01"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage01-02"
        
        elif currentScreen == "Stage01-02":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-01"
            if event.type == pygame.MOUSEBUTTONDOWN and symbol.collidepoint(event.pos):
                display_dialogue("Analisando o estranho símbolo, é possível distinguir\num texto estranho na figura.", game_font, screen_width, screen_height, screen, wait_period=4000)
                display_dialogue("3. dW5jYSBtb3", game_font, screen_width, screen_height, screen, wait_period=7000)
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage01-03"

        elif currentScreen == "Stage01-03":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-02"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage01-Hall02"
        
        elif currentScreen == "Stage02-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall01"
        
        elif currentScreen == "Stage03-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall01"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage03-02"
        
        elif currentScreen == "Stage03-02":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage03-01"
            if event.type == pygame.MOUSEBUTTONDOWN and symbol.collidepoint(event.pos):
                display_dialogue("Analisando o estranho símbolo, é possível distinguir\num texto estranho em meio aos símbolos intelegíveis em estoniano.", game_font, screen_width, screen_height, screen, wait_period=4000)
                display_dialogue("4. JyZXLDoS4=", game_font, screen_width, screen_height, screen, wait_period=7000)

        elif currentScreen == "Stage04-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall01"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage04-02"
        
        elif currentScreen == "Stage04-02":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage04-01"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage04-03"
        
        elif currentScreen == "Stage04-03":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage04-02"
            if event.type == pygame.MOUSEBUTTONDOWN and symbol.collidepoint(event.pos):
                display_dialogue("Analisando o estranho símbolo, é possível distinguir\num texto estranho logo abaixo da figura, em letras pequenas.", game_font, screen_width, screen_height, screen, wait_period=4000)
                display_dialogue("1. QSBBZ3JvQ2", game_font, screen_width, screen_height, screen, wait_period=7000)

        elif currentScreen == "Stage05-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall02"
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage05-02"
        
        elif currentScreen == "Stage05-02":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage05-01"
            if event.type == pygame.MOUSEBUTTONDOWN and symbol.collidepoint(event.pos):
                display_dialogue("Por detrás do ornamento de metal,\num pequeno texto é visível.", game_font, screen_width, screen_height, screen, wait_period=4000)
                display_dialogue("2. 9ubmVjdCBu", game_font, screen_width, screen_height, screen, wait_period=7000)
            if event.type == pygame.MOUSEBUTTONDOWN and next_step.collidepoint(event.pos):
                currentScreen = "Stage05-03"

        elif currentScreen == "Stage05-03":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage05-02"
        
        elif currentScreen == "Stage06-01":
            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage01-Hall02"
            if event.type == pygame.MOUSEBUTTONDOWN and message_code.collidepoint(event.pos):
                display_dialogue("Um slogan que diz: 'AgroConnect: 64 anos mudando o seu futuro.'", game_font, screen_width, screen_height, screen, wait_period=4000)
            if event.type == pygame.MOUSEBUTTONDOWN and message_biblic.collidepoint(event.pos):
                display_dialogue("Ao redor do ornamento, existe uma mensagem.", game_font, screen_width, screen_height, screen, wait_period=4000)
                display_dialogue("Ouve, ó Deus, a minha voz na minha oração; guarda a minha\n vida do temor do inimigo. Esconde-me do secreto conselho dos maus,\n e do tumulto dos que praticam a iniqüidade.", game_font, screen_width, screen_height, screen, wait_period=7000)
                display_dialogue("Que afiaram as suas línguas como espadas; e armaram \n por suas flechas palavras amargas, A fim de atirarem em lugar oculto\nao que é íntegro; disparam sobre ele repentinamente, e não temem.", game_font, screen_width, screen_height, screen, wait_period=7000)
                display_dialogue("Firmam-se em mau intento; falam de armar laços\n secretamente, e dizem: Quem os verá?", game_font, screen_width, screen_height, screen, wait_period=7000)
                display_dialogue("Ao lado, escrito à mão com uma letra grosseira,\n está escrito: 'Aonde estava Deus naquele dia?'", game_font, screen_width, screen_height, screen, wait_period=7000)
            if event.type == pygame.MOUSEBUTTONDOWN and door.collidepoint(event.pos):
                currentScreen = "Stage01-Door"
        
        elif currentScreen == "Stage01-Door":
            if not checkpoint_find_door:
                    display_dialogue("Por detrás da porta encontrada na passagem,\nhavia uma outra porta... diferente e mais robusta. Tecnológica também.", game_font, screen_width, screen_height, screen, wait_period=4000)
                    display_dialogue("Estranho... como a porta ainda possui energia,\nsendo que nenhum outro local tem?", game_font, screen_width, screen_height, screen, wait_period=4000)
                    display_dialogue("Será que era isso que ele queria que eu encontrasse?", game_font, screen_width, screen_height, screen, wait_period=4000)
                    checkpoint_find_door = True

            if event.type == pygame.MOUSEBUTTONDOWN and back_option.collidepoint(event.pos):
                currentScreen = "Stage06-01"

            if event.type == pygame.MOUSEBUTTONDOWN and fingerprint.collidepoint(event.pos):
                if not stage01_passcode:
                    play_denied_entry()
                    display_dialogue("Não parece aceitar digitais por agora.", game_font, screen_width, screen_height, screen, wait_period=1000)
                else:
                    play_sucess()
                    display_dialogue("Seja bem-vindo, Lobão!", game_font, screen_width, screen_height, screen, wait_period=1000)
                    stage01_pass = True

            if event.type == pygame.MOUSEBUTTONDOWN and try_open.collidepoint(event.pos):
                if not stage01_pass:
                    play_denied_entry()
                    display_dialogue("A porta não abre.", game_font, screen_width, screen_height, screen, wait_period=1000)
                else:
                    currentScreen = "Lab"

            if event.type == pygame.MOUSEBUTTONDOWN and panel.collidepoint(event.pos):
                display_dialogue("Assim que alguém se aproxima, o painel brilha,\n oferecendo uma janela para entrada e questionando: 'Qual a senha?'", game_font, screen_width, screen_height, screen, wait_period=7000)
                if not stage01_passcode:
                    screen = pygame.display.set_mode((540, 320))
                    pygame.display.set_caption("Input Box Example")
                    while True:
                        screen.fill((0, 0, 0))

                        input_text = input_box(screen, highlight_font)
                        if input_text:
                            break

                        pygame.display.flip()
                    
                    screen = pygame.display.set_mode((screen_width, screen_height))

                    if input_text == "A AgroConnect nunca morrerá.":
                        stage01_passcode = True
                        play_sucess()
                        display_dialogue("Isso! Essa era a resposta correta.", game_font, screen_width, screen_height, screen, wait_period=1000)
                    else:
                        stage01_passcode = False
                        play_denied_entry()
                        display_dialogue("Resposta errada.", game_font, screen_width, screen_height, screen, wait_period=1000)
            

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

    elif currentScreen == "Stage01-Passage":
        passage = pygame.image.load("images/Stage01/Passage.jpeg").convert()
        passage = pygame.transform.scale(passage, (screen_width, screen_height))

        screen.blit(passage, (0, 0))
    
    elif currentScreen == "Stage01-Hall01":
        hall_first_path, hall_second_path, hall_third_path, hall_fourth_path = stage01_hall(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage01-01":
        back_option, next_step = stage01_01(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage01-02":
        back_option, symbol, next_step = stage01_02(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage01-03":
        back_option, next_step = stage01_03(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage02-01":
        back_option = stage02_01(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage03-01":
        back_option, next_step = stage03_01(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage03-02":
        back_option, symbol = stage03_02(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage04-01":
        back_option, next_step = stage04_01(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage04-02":
        back_option, next_step = stage04_02(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage04-03":
        back_option, symbol = stage04_03(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage01-Hall02":
        hall_first_path, hall_second_path, hall_third_path = stage02_hall(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage05-01":
        back_option, next_step = stage05_01(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage05-02":
        back_option, symbol, next_step = stage05_02(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage05-03":
        back_option = stage05_03(screen, screen_width, screen_height, highlight_font)
    
    elif currentScreen == "Stage06-01":
        back_option, message_code, message_biblic, door = stage06_01(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Stage01-Door":
        back_option, try_open, panel, fingerprint = stage01_door(screen, screen_width, screen_height, highlight_font)

    elif currentScreen == "Lab":
        lab = pygame.image.load("images/Lab.jpeg").convert()
        lab = pygame.transform.scale(lab, (screen_width, screen_height))

        screen.blit(lab, (0, 0))

    pygame.display.update()