import pygame

# Função para destacar áreas de interação.
def highlight_area(area, screen):
    surface = pygame.Surface((area.width, area.height), pygame.SRCALPHA)
    surface.fill((250, 250, 250, 25))
    screen.blit(surface, (area.x, area.y))