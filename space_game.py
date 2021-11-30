import pygame
import controls
from gun import Gun
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    vrags = Group()
    controls.create_vrages(screen, vrags)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.uddate(bg_color, screen, gun, vrags, bullets)
        controls.uddage_bullets(bullets)
        controls.update_vrags(vrags)


run()
