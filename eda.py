import random
from nastroiki import *
import pygame as p

class Eda:
    def __init__(self,igra,x,y,shirina,visota,kartinka):
        self.igra=igra

        self.pramoygolnik=p.rect.Rect([x,y],[shirina,visota])
        self.kartinka=load_image(kartinka,shirina,visota)

    def otrisovka(self):
        self.igra.screen.blit(self.kartinka,self.pramoygolnik)