import pygame as p
import baza_zmei
from nastroiki import *

class Telo_zmei(baza_zmei.Baza_zmeya):
    def __init__(self,igra,x,y,shirina,visota,kakaya_stororna):

        super().__init__(igra,x,y,shirina,visota)
        self.kletko =0
        self.kakaya_storona=kakaya_stororna
        self.kakaya_kartinka = zagryzka_kartinki_hvosta()
        self.kartinka = self.kakaya_kartinka[0]
        self.pramoygolnik_proverka = p.rect.Rect([self.x, self.y], [self.shirina / 4, self.visota / 4])

    def otrisovka(self):
        super().otrisovka()

    def ypravlenie(self):








        if self.kakaya_storona==1:
            self.kartinka = self.kakaya_kartinka[0]

        if self.kakaya_storona == 2:

            self.kartinka = self.kakaya_kartinka[1]