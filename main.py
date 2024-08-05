import random
import golova_zmei
import pygame as p
import telo_zmei
import kletka
import eda
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
        self.chislo=1
        self.y = 0
        self.sozdanie_kletok()
        self.eda=0
        self.spisok_edi=[]
        self.random=random.randint(0,len(self.spisok_kletok)-1)
        self.zmeika_golova=golova_zmei.Golova_zmei(self,self.spisok_kletok[self.random].pramoygolnik.x+6,self.spisok_kletok[self.random].pramoygolnik.y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok)
        self.zmeika_telo = telo_zmei.Telo_zmei(self,self.spisok_kletok[self.random].pramoygolnik.x+6,self.spisok_kletok[self.random].pramoygolnik.y,
                                               SCREEN_WIDTH / self.stolbci - self.promezhytok ,
                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok,1)
        self.spisok_tel = [self.zmeika_telo]
        self.sobitie_sozdania = p.USEREVENT
        p.time.set_timer(self.sobitie_sozdania, 1000)
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

                for telo in self.spisok_tel:
                    if kletko.pramoygolnik.colliderect(telo.pramoygolnik):
                        telo.ypravlenie(kletko)
                    if   self.zmeika_telo.pramoygolnik.x-self.zmeika_golova.pramoygolnik.x>=40   :
                        self.zmeika_telo=telo_zmei.Telo_zmei(self,self.zmeika_golova.pramoygolnik.x+20,self.zmeika_golova.pramoygolnik.y,
                                               SCREEN_WIDTH / self.stolbci - self.promezhytok ,
                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok ,2)
                        self.spisok_tel.append(self.zmeika_telo)
                        if len(self.spisok_tel)>self.eda:
                            self.spisok_tel.pop(0)
                    if self.zmeika_golova.pramoygolnik.y - self.zmeika_telo.pramoygolnik.y >= 40 :
                        self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x,
                                                               self.zmeika_golova.pramoygolnik.y -20,
                                                               SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok, 1)
                        self.spisok_tel.append(self.zmeika_telo)
                        if len(self.spisok_tel) > self.eda:
                            self.spisok_tel.pop(0)
                    if self.zmeika_golova.pramoygolnik.x-self.zmeika_telo.pramoygolnik.x>=40:
                        self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x - 20,
                                                               self.zmeika_golova.pramoygolnik.y,
                                                               SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok, 2)
                        self.spisok_tel.append(self.zmeika_telo)
                        if len(self.spisok_tel) > self.eda:
                            self.spisok_tel.pop(0)
                    if self.zmeika_telo.pramoygolnik.y - self.zmeika_golova.pramoygolnik.y >= 40:
                        self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x,
                                                               self.zmeika_golova.pramoygolnik.y + 20,
                                                               SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok, 1)
                        self.spisok_tel.append(self.zmeika_telo)
                        if len(self.spisok_tel) > self.eda:
                            self.spisok_tel.pop(0)
                for est_ili_net in self.spisok_edi:
                    if est_ili_net.pramoygolnik.colliderect(self.zmeika_golova.pramoygolnik):
                        self.eda+=1
                        self.spisok_edi.remove(est_ili_net)
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
                        self.kletka=kletka.Kletka(self,self.x,self.y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok,self.chislo
                                                  )

                        self.spisok_kletok.append(self.kletka)
                        self.chislo += 1

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
            if event.type==self.sobitie_sozdania:

                self.eda_poyavlenie=eda.Eda(self,self.spisok_kletok[random.randint(0,self.kletki*self.stolbci-1)].pramoygolnik.x+6,self.spisok_kletok[random.randint(0,self.kletki*self.stolbci-1)].pramoygolnik.y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok,"kartinki/yabloko.png")
                self.spisok_edi.append(self.eda_poyavlenie)
    def otrisovka(self):
        for kletka in self.spisok_kletok:
            kletka.otrisovka()
        self.zmeika_golova.otrisovka()
        for telo in self.spisok_tel:
            telo.otrisovka()
        for eda in self.spisok_edi:
            eda.otrisovka()
        p.display.flip()
if __name__ == "__main__":
    Game(SKOLKO_KLETOK,SKOLKO_KLETOK,PROMESHYTOK)

