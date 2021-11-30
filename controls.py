import pygame, sys
from bullet import Bullet
from vrag import Vrag


def events(screen, gun, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            """"Движение вправо"""
            if event.key == pygame.K_d:
                gun.mright = True
                """"Движение влево"""
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def uddate(bg_color, screen, gun, vrags, bullets):
    """"Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    vrags.draw(screen)
    pygame.display.flip()


def uddage_bullets(bullets):
    """"Обновляет позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_vrags(vrags):
    """"Обновляет позицию врагов"""
    vrags.update()


def create_vrages(screen, vrags):
    """"Создание армии"""
    vrag = Vrag(screen)
    vrag_width = vrag.rect.width
    number_vrag_x = int((800 - 2 * vrag_width) / vrag_width)
    vrag_height = vrag.rect.height
    number_vrag_y = int((800 - 100 - 2 * vrag_height) / vrag_height)

    for row_number in range(number_vrag_y - 4):

        for vrag_number in range(number_vrag_x):

            vrag = Vrag(screen)
            vrag.x = vrag_width + (vrag_width * vrag_number)
            vrag.y = vrag_height + (vrag_height * row_number)
            vrag.rect.x = vrag.x
            vrag.rect.y = vrag.rect.height + (vrag.rect.height * row_number)
            vrags.add(vrag)
