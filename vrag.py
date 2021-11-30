import pygame


class Vrag(pygame.sprite.Sprite):
    """"1 враг"""

    def __init__(self, screen):
        """"Иницадизация и начальаня позиция"""
        super(Vrag, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод врага на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"Перемещение врагов"""
        self.y += 0.1
        self.rect.y = self.y
