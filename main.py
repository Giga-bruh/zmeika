import random

import pygame as p
import kletka
import baza_zmei
from nastroiki import *
class Game:
    def __init__(self,kletki,stolbci,promezhytok):
        self.screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.spisok_kletok=[]
        self.kletki=kletki
        self.itap2 = 0
        self.stolbci = stolbci
        self.promezhytok = promezhytok
        self.x = 0

        self.y = 0
        self.sozdanie_kletok()
        self.random=random.randint(0,len(self.spisok_kletok)-1)
        self.zmeika_golova=baza_zmei.Baza_zmeya(self,self.spisok_kletok[self.random].pramoygolnik.x+6,self.spisok_kletok[self.random].pramoygolnik.y,"Snake sprite sheet_1.png","Snake sprite sheet_0.png",SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok)


        self.clock = p.time.Clock()
        self.run()


    def run(self):
        while True:
            self.sozdanie_kletok()
            self.otrisovka()
            self.event()

            for kletko in self.spisok_kletok:
                if kletko.pramoygolnik.colliderect(self.zmeika_golova.pramoygolnik):
                    self.zmeika_golova.ypravlenie(kletko)
            self.clock.tick(FPS)
            self.screen.fill([1,1,1])
    def sozdanie_kletok(self):

        zakoncheno_ili_net=0
        if zakoncheno_ili_net==0 and self.itap2==1:
            self.y+=SCREEN_WIDTH/self.stolbci
            self.itap2=0
            zakoncheno_ili_net=0


        if zakoncheno_ili_net==0:
            while zakoncheno_ili_net!=1:

                if len(self.spisok_kletok) != self.kletki * self.stolbci:
                        self.kletka=kletka.Kletka(self,self.x,self.y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok)

                        self.spisok_kletok.append(self.kletka)

                if self.x!=SCREEN_WIDTH:
                    self.x+=SCREEN_HEIGHT/self.stolbci






                if   self.x>=SCREEN_WIDTH:

                    self.x=0
                    self.itap2=1
                    zakoncheno_ili_net=1














    def event(self):
        for event in p.event.get():
            if event.type == pg.QUIT:
                quit()

    def otrisovka(self):
        for kletka in self.spisok_kletok:
            kletka.otrisovka()
        self.zmeika_golova.otrisovka()

        p.display.flip()
if __name__ == "__main__":
    Game(18,18,10)

