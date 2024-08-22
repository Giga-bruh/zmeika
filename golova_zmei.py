import pygame as p
import baza_zmei
import telo_zmei
from nastroiki import *

class Golova_zmei(baza_zmei.Baza_zmeya):
    def __init__(self,igra,x,y,shirina,visota):
        super().__init__(igra,x,y,shirina,visota)
        self.kletko = 0

        self.kakaya_kartinka = zagryzka_kartinki()
        self.kartinka = self.kakaya_kartinka[0]

    def otrisovka(self):
        super().otrisovka()

    def ypravlenie(self,kletko,kakaoi_stolbec):
        self.stolbe=kakaoi_stolbec
        self.kletko = kletko
        self.kakaya_kletka=self.kletko.kakaya_kletka
        klavishi = p.key.get_pressed()
        if klavishi[p.K_a] == True and self.igra.zmeika_telo.kyda_dvigaetsa!=3:
            if self.kyda_dvigatsa!=3:
                self.kyda_dvigatsa = 1

                self.kartinka = self.kakaya_kartinka[3]

        elif klavishi[p.K_s] == True and self.igra.zmeika_telo.kyda_dvigaetsa!=2:
            if self.kyda_dvigatsa!=4:
                self.kyda_dvigatsa = 2

                self.kartinka = self.kakaya_kartinka[1]

        elif klavishi[p.K_d] == True and self.igra.zmeika_telo.kyda_dvigaetsa!=4:
            if self.kyda_dvigatsa!=1:
                self.kyda_dvigatsa = 3

                self.kartinka = self.kakaya_kartinka[0]

        elif klavishi[p.K_w] == True and self.igra.zmeika_telo.kyda_dvigaetsa!=1:
            if self.kyda_dvigatsa!=2:
                self.kyda_dvigatsa = 4

                self.kartinka = self.kakaya_kartinka[2]
        if self.kyda_dvigatsa != 0:
            if self.kyda_dvigatsa == 1:
                self.pramoygolnik.centerx -= 1
                self.pramoygolnik.centery = kletko.pramoygolnik.centery
            if self.kyda_dvigatsa == 2:
                self.pramoygolnik.centery += 1
                self.pramoygolnik.centerx = kletko.pramoygolnik.centerx
            if self.kyda_dvigatsa == 3:
                self.pramoygolnik.centerx += 1
                self.pramoygolnik.centery = kletko.pramoygolnik.centery
            if self.kyda_dvigatsa == 4:
                self.pramoygolnik.centery -= 1
                self.pramoygolnik.centerx = kletko.pramoygolnik.centerx
