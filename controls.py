import pygame
import sys
def events(gun):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame. KEYDOWN:
            """"Движение вправо"""
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
                """"Движение вправо"""
                if event.key == pygame.K_d:
                    gun.mright = False
                elif event.key == pygame.K_a:
                    gun.mleft = False

def update(bg_color, screen, gun):
    """"Обновление экрана"""
    screen.fill(bg_color)
    gun.output()
    pygame.display.flip()

