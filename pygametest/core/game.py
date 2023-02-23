import pyglet as pg


class Game(pg.window.Window):
    def __init__(self, config: dict):
        # ? Сохраняем конфиг
        self.conf_d = config

        # ? Применяем конфиг
        super().__init__(resizable=config['GAME']['resizable'])
        self.set_minimum_size(50, 50)
        self.update_conf()

        self.label = pg.text.Label('Hello, world!')

    # ! Програмное
    def update_conf(self):
        if self.conf_d['GAME']['fullscreen']:
            self.set_fullscreen(True)
        else:
            self.set_size(
                self.conf_d['GAME']['width'],
                self.conf_d['GAME']['height']
            )
        self.set_vsync(self.conf_d['GAME']['vsync'])

    def on_draw(self):
        self.clear()
        self.label.draw()

    def run(self):
        pg.app.run()
