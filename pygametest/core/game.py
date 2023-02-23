import pygame
import sys

from .level import Level


class Game:
    def __init__(self, config: dict):
        # ? Запуск
        pygame.init()
        self.config = config

        # ? Настраиваем конфиг
        self.screen = pygame.display
        self.screen.set_caption('Pygame Sample')
        self.update_conf()
        self.clock = pygame.time.Clock()
        self.level = Level()

    def update_conf(self):
        if self.config['GAME']['fullscreen']:
            self.screen.set_mode(flags=pygame.FULLSCREEN)
        else:
            self.screen.set_mode(
                (self.config['GAME']['width'], self.config['GAME']['height']),
            )
            if self.config['GAME']['resizable']:
                self.screen.set_mode(
                    flags=pygame.RESIZABLE,
                )
            if self.config['GAME']['vsync']:
                self.screen.set_mode(
                    vsync=1,
                )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()
