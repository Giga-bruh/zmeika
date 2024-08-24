import pygame as pg
pg.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
import kletka

SKOLKO_KLETOK=15

PROMESHYTOK=10
SHRINA_KLETKI=SCREEN_WIDTH/SKOLKO_KLETOK-PROMESHYTOK
FPS = 5

font = pg.font.Font(None, 40)

def text_render(text):
    return font.render(str(text), True, "black")

def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image
def zagryzka_kartinki():

    kartinka_dla_razvorotov_w_s=load_image("kartinki/Snake sprite sheet_0.png",SCREEN_WIDTH/SKOLKO_KLETOK-PROMESHYTOK,SCREEN_HEIGHT/SKOLKO_KLETOK-PROMESHYTOK)
    kartinka_dla_razvorotov_a_d=load_image("kartinki/Snake sprite sheet_1.png",SCREEN_WIDTH/SKOLKO_KLETOK-PROMESHYTOK,SCREEN_HEIGHT/SKOLKO_KLETOK-PROMESHYTOK)

    kartinka=pg.transform.flip(kartinka_dla_razvorotov_w_s, 0, 1)
    kartinka_a=pg.transform.flip(kartinka_dla_razvorotov_a_d,1,0)


    spisok_kartinok_zmei_golovi=[kartinka_dla_razvorotov_a_d,kartinka_dla_razvorotov_w_s,kartinka,kartinka_a]
    return spisok_kartinok_zmei_golovi

def zagryzka_kartinki_hvosta():
    kartinka_dla_razvorotov_hvosta_w_s = load_image("kartinki/Snake sprite sheet_2.png", SCREEN_WIDTH / SKOLKO_KLETOK - PROMESHYTOK,
                                             SCREEN_HEIGHT / SKOLKO_KLETOK - PROMESHYTOK)


    kartinka_hvosta_a =  load_image("kartinki/Snake sprite sheet_3.png", SCREEN_WIDTH / SKOLKO_KLETOK - PROMESHYTOK,
                                             SCREEN_HEIGHT / SKOLKO_KLETOK - PROMESHYTOK)
    spisok_kartinok_zmei_tela=[kartinka_dla_razvorotov_hvosta_w_s,kartinka_hvosta_a]
    return spisok_kartinok_zmei_tela
def zagryzja_kartinki_hvost():
    kartinka_dla_razvorotov_hvosta_w_s = load_image("kartinki/Snake sprite sheet_6.png",
                                                    SCREEN_WIDTH / SKOLKO_KLETOK - PROMESHYTOK,
                                                    SCREEN_HEIGHT / SKOLKO_KLETOK - PROMESHYTOK)
    kartinka_hvosta_a = load_image("kartinki/Snake sprite sheet_7.png", SCREEN_WIDTH / SKOLKO_KLETOK - PROMESHYTOK,
                                   SCREEN_HEIGHT / SKOLKO_KLETOK - PROMESHYTOK)
    spisok_kartinok_zmei_hvosta = [kartinka_dla_razvorotov_hvosta_w_s, kartinka_hvosta_a]
    return spisok_kartinok_zmei_hvosta