import pygame as pg


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((960, 720))
        self.menu = Menu(self.screen)
        self.stage = "menu"
        self.run = True

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def mainloop(self):
        while self.run:
            self.check_events()
            self.screen.fill((0, 0, 0))
            if self.stage == "menu":
                self.menu.update()
            pg.display.flip()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.menu_bg = pg.image.load("images/logo.png")

    def update(self):
        rect = self.menu_bg.get_rect()
        rect.topleft = (0, 0)
        self.screen.blit(self.menu_bg, rect)
game = Game()
game.mainloop()