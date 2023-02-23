import pygame
import sys

from .level import Level


class Game:
    def __init__(self, config: dict):
        # ? Запуск
        pygame.init()
        self.config = config

        # ? Настраиваем конфиг
        self.screen = pygame.display.set_mode(
            (config['GAME']['width'], config['GAME']['height'])
        )
        pygame.display.set_caption('Pygame Sample')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def update_conf(self):
        if self.config['GAME']['fullscreen']:
            self.screen.set_m

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()
