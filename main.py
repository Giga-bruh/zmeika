import random
import golova_zmei
import pygame as p
import pygame.freetype
import telo_zmei
import kletka
import eda
from nastroiki import *
class Game:
    def __init__(self,kletki,stolbci,promezhytok):
        self.screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.spisok_kletok=[]
        self.kletki=kletki
        self.tekst = p.freetype.Font("kartinki/comic-sans-ms.ttf", 80)
        self.itap2 = 0
        self.stolbci = stolbci
        self.promezhytok = promezhytok
        self.x = 0
        self.chislo=0
        self.kakaya_strorona=0
        self.y = 0
        self.zastypil_ili_net=0
        self.proigral_ili_net=0
        self.sozdanie()
        self.eda=3

        self.kakoe_telo=0

        self.spisok_edi=[]
        self.random=0
        self.naskolko_kletok=0

        self.test = self.sozdanie_2()
        self.zmeika_golova=golova_zmei.Golova_zmei(self,self.spisok_kletok[self.random].pramoygolnik.x+6,self.spisok_kletok[self.random].pramoygolnik.y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok)
        self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x,
                                               self.zmeika_golova.pramoygolnik.y,
                                               SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                               SCREEN_HEIGHT / self.stolbci - self.promezhytok, 1,1,self.test[0][1],self.test[0])
        self.spisok_tel = [self.zmeika_telo]
        self.sobitie_sozdania = p.USEREVENT


        p.time.set_timer(self.sobitie_sozdania, 1000)
        self.clock = p.time.Clock()
        self.run()


    def run(self):

            while True:
                if self.proigral_ili_net==0:



                    self.mehaniki_zmie()

                self.event()
                self.otrisovka()
                self.clock.tick(FPS)



    def sozdanie(self):

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



                if self.x!=SCREEN_WIDTH:
                    self.x+=SCREEN_HEIGHT/self.stolbci
                if   self.x>=SCREEN_WIDTH:
                    self.x=0
                    self.itap2=1
                    zakoncheno_ili_net=1
    def sozdanie_2(self):
        spisok_strok=[]
        for stroka in range(0,SKOLKO_KLETOK):
            stolbec=[]

            for stolbci in range(0,SKOLKO_KLETOK):
                kletkj=kletka.Kletka(self,stolbci*(SHRINA_KLETKI+10),stroka*(SHRINA_KLETKI+10),SHRINA_KLETKI,SHRINA_KLETKI,self.chislo)
                stolbec.append(kletkj)
                if self.chislo==SKOLKO_KLETOK-1:
                    self.chislo=0
                else:
                    self.chislo+=1


            spisok_strok.append(stolbec)
        return spisok_strok
    def event(self):
        for event in p.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type==self.sobitie_sozdania and self.proigral_ili_net==0 and len(self.spisok_edi)<=0:

                 self.eda_poyavlenie=eda.Eda(self,self.test[random.randint(0,SKOLKO_KLETOK-1)][random.randint(0,SKOLKO_KLETOK-1)].x+6,self.test[random.randint(0,SKOLKO_KLETOK-1)][random.randint(0,SKOLKO_KLETOK-1)].y,SCREEN_WIDTH/self.stolbci-self.promezhytok,SCREEN_HEIGHT/self.stolbci-self.promezhytok,"kartinki/yabloko.png")

                 self.spisok_edi.append(self.eda_poyavlenie)


    def mehaniki_zmie(self):
        if self.proigral_ili_net==0:
            self.pribovlnie=1

            self.zmeika_golova.ypravlenie()
            if len(self.spisok_tel) == self.eda:

                for telo in self.spisok_tel:

                    if self.kakoe_telo + 1 == len(self.spisok_tel):
                        self.kakoe_telo = 0

                    if telo.pramoygolnik.centery < self.spisok_tel[
                        self.kakoe_telo + 1].pramoygolnik.centery and telo.pramoygolnik.centerx==self.spisok_tel[self.kakoe_telo-1].pramoygolnik.centerx and self.zmeika_golova.kyda_dvigatsa %2!=0:
                        telo.kakaya_storona = 4

                    if telo.pramoygolnik.centery == self.spisok_tel[
                        self.kakoe_telo + 1].pramoygolnik.centery and telo.pramoygolnik.centerx>self.spisok_tel[self.kakoe_telo-1].pramoygolnik.centerx and self.zmeika_golova.kyda_dvigatsa %2==0:

                        telo.kakaya_storona = 5
                    if telo.pramoygolnik.centery == self.spisok_tel[
                        self.kakoe_telo + 1].pramoygolnik.centery and telo.pramoygolnik.centerx<self.spisok_tel[self.kakoe_telo-1].pramoygolnik.centerx and self.zmeika_golova.kyda_dvigatsa %2==0:
                        telo.kakaya_storona = 3

                    if telo.pramoygolnik.centery > self.spisok_tel[
                        self.kakoe_telo + 1].pramoygolnik.centery and telo.pramoygolnik.centerx==self.spisok_tel[self.kakoe_telo-1].pramoygolnik.centerx and self.zmeika_golova.kyda_dvigatsa %2!=0:
                        telo.kakaya_storona = 6
                        pass
                    self.kakoe_telo += 1
                    telo.ypravlenie()

            if self.zmeika_golova.kyda_dvigatsa == 1 or self.zmeika_golova.kyda_dvigatsa == 3:


                self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x,
                                                   self.zmeika_golova.pramoygolnik.y,
                                                   SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                                   SCREEN_HEIGHT / self.stolbci - self.promezhytok, 2, 0,
                                                   self.test[0][1], self.test[0])

                self.spisok_tel.append(self.zmeika_telo)
                if self.eda < len(self.spisok_tel):
                    self.spisok_tel.pop(0)
            elif self.zmeika_golova.kyda_dvigatsa == 2 or self.zmeika_golova.kyda_dvigatsa == 4:

                self.zmeika_telo = telo_zmei.Telo_zmei(self, self.zmeika_golova.pramoygolnik.x,
                                                       self.zmeika_golova.pramoygolnik.y,
                                                       SCREEN_WIDTH / self.stolbci - self.promezhytok,
                                                       SCREEN_HEIGHT / self.stolbci - self.promezhytok, 1, 0,
                                                       self.test[0][1], self.test[0])
                self.spisok_tel.append(self.zmeika_telo)
                if self.eda<len(self.spisok_tel):
                    self.spisok_tel.pop(0)









        if self.zmeika_golova.pramoygolnik.centery > SCREEN_HEIGHT:
            self.zmeika_golova.pramoygolnik.centery = 0

        if self.zmeika_golova.pramoygolnik.centery < 0:
            self.zmeika_golova.pramoygolnik.centery = SCREEN_HEIGHT
        if self.zmeika_golova.pramoygolnik.centerx > SCREEN_WIDTH:
            self.zmeika_golova.pramoygolnik.centerx = 0

        if self.zmeika_golova.pramoygolnik.centerx < 0:
            self.zmeika_golova.pramoygolnik.centerx = SCREEN_WIDTH
        for eda in self.spisok_edi:
            if eda.pramoygolnik.colliderect(self.zmeika_golova.pramoygolnik):
                self.spisok_edi.remove(eda)
                self.eda+=1


    def otrisovka(self):
            self.screen.fill([1, 1, 1])
            # for kletka in self.spisok_kletok:
            #     kletka.otrisovka()
            for stroka in self.test:
                for kletka in stroka:
                    kletka.otrisovka()
            for telo in self.spisok_tel[0:-1]:

                telo.otrisovka()
            self.zmeika_golova.otrisovka()

            for eda in self.spisok_edi:
                eda.otrisovka()
            if self.proigral_ili_net==1:
                self.tekst.render_to(self.screen, [100, 19], "вы проиграли", [1, 1, 1])
            p.display.flip()


if __name__ == "__main__":
    Game(SKOLKO_KLETOK,SKOLKO_KLETOK,PROMESHYTOK)

