import pygame as p
import baza_zmei
from nastroiki import *

class Telo_zmei(baza_zmei.Baza_zmeya):
    def __init__(self,igra,x,y,shirina,visota,kakaya_stororna,kyda_dvigaetsa,kletko,kakpi_stolbec):

        super().__init__(igra,x,y,shirina,visota,)

        self.stolbec = kakpi_stolbec
        self.kletko = kletko
        self.kakaya_kletka = self.kletko.kakaya_kletka
        self.kyda_dvigaetsa=kyda_dvigaetsa
        self.kakaya_storona=kakaya_stororna
        self.kakaya_kartinka = zagryzka_kartinki_hvosta()
        self.kartinka = self.kakaya_kartinka[0]


        self.pramoygolnik_proverka = p.rect.Rect([self.x, self.y], [self.shirina/2 , self.visota/2 ])

    def otrisovka(self):
        super().otrisovka()
        p.draw.rect(self.igra.screen,[0,0,0],self.pramoygolnik_proverka)

    def ypravlenie(self):





        
        # TODO
        self.kartinka = self.kakaya_kartinka[self.kakaya_storona - 1]
        # весь нижний код, можно замениь одной строкой

        # if self.kakaya_storona==1:
        #     self.kartinka = self.kakaya_kartinka[0]

        # if self.kakaya_storona == 2:

        #     self.kartinka = self.kakaya_kartinka[1]

        # if self.kakaya_storona==3:
        #     self.kartinka=self.kakaya_kartinka[2]
        # if self.kakaya_storona == 4:
        #     self.kartinka = self.kakaya_kartinka[3]
        # if self.kakaya_storona == 5:
        #     self.kartinka = self.kakaya_kartinka[4]
        # if self.kakaya_storona == 6:
        #     self.kartinka = self.kakaya_kartinka[5]




