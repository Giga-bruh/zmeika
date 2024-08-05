import pygame as p

from nastroiki import *
class Baza_zmeya:
    def __init__(self,igra,x,y,shirina,visota):
        super().__init__()
        self.igra=igra
        self.x=x

        self.shirina=shirina
        self.visota=visota

        self.kyda_dvigatsa=0
        self.y=y


        self.pramoygolnik=p.rect.Rect([self.x,self.y],[self.shirina,self.visota])
    def otrisovka(self):
        self.igra.screen.blit(self.kartinka,self.pramoygolnik)

