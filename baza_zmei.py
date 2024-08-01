import pygame as p

from nastroiki import *
class Baza_zmeya:
    def __init__(self,igra,x,y,kartinka,kartinka_dla_provorotov,shirina,visota):
        self.igra=igra
        self.x=x
        self.shirina=shirina
        self.visota=visota
        self.kakaya_kartinka=kartinka
        self.kyda_dvigatsa=0
        self.y=y
        self.kartinka_dla_razvorotov_a_d=load_image(self.kakaya_kartinka, shirina, visota)
        self.kartinka_dla_povorotov_w_s=load_image(kartinka_dla_provorotov, shirina, visota)
        self.kartinka=load_image(self.kakaya_kartinka, shirina, visota)
        self.pramoygolnik=p.rect.Rect([self.x,self.y],[self.shirina,self.visota])
    def otrisovka(self):
        self.igra.screen.blit(self.kartinka,self.pramoygolnik)
    def ypravlenie(self,kletka):
        klavishi = p.key.get_pressed()
        if klavishi[p.K_a] == True:
            self.kyda_dvigatsa=1
            self.kakaya_kartinka=self.kartinka_dla_razvorotov_a_d
            self.kartinka=p.transform.flip(self.kakaya_kartinka, 1, 0)

        if klavishi[p.K_s]==True:
            self.kyda_dvigatsa=2
            self.kakaya_kartinka=self.kartinka_dla_povorotov_w_s
            self.kartinka = p.transform.flip(self.kakaya_kartinka, 0, 0)

        if klavishi[p.K_d]==True:
            self.kyda_dvigatsa=3
            self.kakaya_kartinka=self.kartinka_dla_razvorotov_a_d
            self.kartinka = p.transform.flip(self.kakaya_kartinka, 0, 0)

        if klavishi[p.K_w] == True:
            self.kyda_dvigatsa=4
            self.kakaya_kartinka=self.kartinka_dla_povorotov_w_s
            self.kartinka = p.transform.flip(self.kartinka_dla_povorotov_w_s, 0, 1)

        if self.kyda_dvigatsa!=0:
            if self.kyda_dvigatsa==1:
                self.pramoygolnik.centerx -= 1
                self.pramoygolnik.centery = kletka.pramoygolnik.centery
            if self.kyda_dvigatsa==2:
                self.pramoygolnik.centery += 1
                self.pramoygolnik.centerx = kletka.pramoygolnik.centerx
            if self.kyda_dvigatsa==3:
                self.pramoygolnik.centerx += 1
                self.pramoygolnik.centery = kletka.pramoygolnik.centery
            if self.kyda_dvigatsa == 4:
                self.pramoygolnik.centery -= 1
                self.pramoygolnik.centerx = kletka.pramoygolnik.centerx
