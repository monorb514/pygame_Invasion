import pygame

class Ship():
    def __init__(self, screen, ai_settings) -> None:
        self.screen = screen
        self.settings = ai_settings

        self.image = pygame.image.load('./img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Стартовая позиция корабля
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #Индикаторы движения
        self.move_right = False
        self.move_left = False

    def blitme(self):
        #Рисуем корабль на текущей позиции
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        if self.move_right and self.rect.right < 1200:
            self.center += self.settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        
        self.rect.centerx = self.center




        
