import pygame as pg
pg.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900


FPS = 60

font = pg.font.Font(None, 40)

def text_render(text):
    return font.render(str(text), True, "black")