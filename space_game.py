import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    vrags = Group()
    controls.create_vrages(screen, vrags)
    stats = Stats()
    sc = Scores(screen, stats)



    while True:
        controls.events(screen, gun, bullets)
        if stats.lose_game:
            gun.update_gun()
            bullets.update()
            controls.uddate(bg_color, screen, stats, sc, gun, vrags, bullets)
            controls.uddage_bullets(screen, stats, sc, vrags, bullets)
            controls.update_vrags(stats, screen, sc, gun, vrags, bullets)

run()
