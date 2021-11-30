import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Позиция пули"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 224, 224, 224
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """"Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """"Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)


