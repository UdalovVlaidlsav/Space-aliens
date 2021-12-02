import pygame, sys
from bullet import Bullet
from vrag import Vrag
import time


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


def uddate(bg_color, screen, stats, sc, gun, vrags, bullets):
    """"Обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    vrags.draw(screen)
    pygame.display.flip()


def uddage_bullets(screen, stats, sc,vrags, bullets):
    """"Обновляет позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, vrags, True, True)
    if collections:
        for vrags in collections.values():
            stats.score += 10 * len(vrags)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(vrags) == 0:
        bullets.empty()
        create_vrages(screen, vrags)


def gun_kill(stats, screen, sc, guns, vrags, bullets):
    """"Столкновение пушки и врагов"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        vrags.empty()
        bullets.empty()
        create_vrages(screen, vrags)
        guns.create_gun()
        time.sleep(1)
    else:
        stats.lose_game = False
        sys.exit()


def update_vrags(stats, screen, sc,gun, vrags, bullets):
    """"Обновляет позицию врагов"""
    vrags.update()
    if pygame.sprite.spritecollideany(gun, vrags):
        gun_kill(stats, screen, sc, gun, vrags, bullets)
    vtarg_check(stats, screen, sc, gun, vrags, bullets)


def vtarg_check(stats, screen, sc, gun, vrags, bullets):
    """"Дошли ли пришелцьы до пушки"""
    screen_rect = screen.get_rect()
    for vrag in vrags.sprites():
        if vrag.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, vrags, bullets)
            break


def create_vrages(screen, vrags):
    """"Создание армии"""
    vrag = Vrag(screen)
    vrag_width = vrag.rect.width
    number_vrag_x = int((800 - 2 * vrag_width) / vrag_width)
    vrag_height = vrag.rect.height
    number_vrag_y = int((800 - 100 - 2 * vrag_height) / vrag_height)

    for row_number in range(number_vrag_y - 2):

        for vrag_number in range(number_vrag_x):
            vrag = Vrag(screen)
            vrag.x = vrag_width + (vrag_width * vrag_number)
            vrag.y = vrag_height + (vrag_height * row_number)
            vrag.rect.x = vrag.x
            vrag.rect.y = vrag.rect.height + (vrag.rect.height * row_number)
            vrags.add(vrag)

def check_high_score(stats, sc):
    """"Проверка на новые рекорды"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.imgage_high_score()
        with open ('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

