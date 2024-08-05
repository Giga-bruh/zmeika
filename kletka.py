import pygame as p

class Kletka:
    def __init__(self,igra,x,y,razmer_shirina,razmer_visota,kakaya_kletka):
        self.x = x

        self.y = y
        self.kakaya_kletka=kakaya_kletka
        self.razmer_shirina=razmer_shirina
        self.razmer_visota=razmer_visota

        self.igra = igra

        self.pramoygolnik = p.rect.Rect([self.x, self.y],[self.razmer_shirina,self.razmer_visota])

    def otrisovka(self):
        p.draw.rect(self.igra.screen,[255,255,255],self.pramoygolnik)
