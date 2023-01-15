# TEE PELI TÄHÄN
import pygame
import math 
import random
import time

def piirra_kivi_seina(x, y):
    if x>-blokki_koko and x<640+blokki_koko and y>-blokki_koko and y<480+blokki_koko:
        eta = 1-math.sqrt((x-320)**2+(y-240)**2)/600
        a =[(195, 199, 196), (195, 199, 196), (195, 199, 196), (195, 199, 196), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (65, 67, 65), (195, 199, 196), (195, 199, 196), (195, 199, 196), (133, 134, 133), (65, 67, 65), (195, 199, 196), (133, 134, 133), (195, 199, 196), (195, 199, 196), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (65, 67, 65), (133, 134, 133), (133, 134, 133), (98, 98, 98), (99, 99, 99), (0, 0, 0), (133, 134, 133), (133, 134, 133), (65, 67, 65), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (133, 134, 133), (0, 0, 0), (0, 0, 0), (133, 134, 133), (86, 86, 86), (0, 0, 0), (65, 67, 65), (65, 67, 65), (133, 134, 133), (65, 67, 65), (0, 0, 0), (0, 0, 0), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (0, 0, 0), (0, 0, 0), (65, 67, 65), (182, 184, 182), (182, 184, 182), (65, 67, 65), (195, 199, 196), (195, 199, 196), (65, 67, 65), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (194, 198, 194), (65, 67, 65), (133, 134, 133), (133, 134, 133), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (65, 67, 65), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (195, 199, 196), (195, 199, 196), (133, 134, 133), (127, 127, 127), (133, 134, 133), (133, 134, 133), (0, 0, 0), (0, 0, 0), (133, 134, 133), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (0, 0, 0), (0, 0, 0), (65, 67, 65), (65, 67, 65), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (65, 67, 65), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (65, 67, 65), (65, 67, 65), (65, 67, 65), (65, 67, 65), (0, 0, 0), (133, 134, 133), (133, 134, 133), (0, 0, 0), (133, 134, 133), (195, 199, 196), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (133, 134, 133), (65, 67, 65), (194, 198, 194), (195, 199, 196), (133, 134, 133), (65, 67, 65), (0, 0, 0), (0, 0, 0), (0, 0, 0), (195, 199, 196), (195, 199, 196), (133, 134, 133), (65, 67, 65), (195, 199, 196), (195, 199, 196), (133, 134, 133), (0, 0, 0), (194, 198, 194), (133, 134, 133), (195, 199, 196), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (194, 198, 194), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (65, 67, 65), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (86, 86, 86), (133, 134, 133), (133, 134, 133), (0, 0, 0), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (65, 67, 65), (195, 199, 196), (65, 67, 65), (65, 67, 65), (0, 0, 0), (195, 199, 196), (195, 199, 196), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (65, 67, 65), (133, 134, 133), (0, 0, 0), (0, 0, 0), (195, 199, 196), (195, 199, 196), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (195, 199, 196), (166, 166, 166), (65, 67, 65), (195, 199, 196), (195, 199, 196), (195, 199, 196), (65, 67, 65), (0, 0, 0), (65, 67, 65), (195, 199, 196), (195, 199, 196), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (133, 134, 133), (133, 134, 133), (65, 67, 65), (195, 199, 196), (133, 134, 133), (133, 134, 133), (133, 134, 133), (65, 67, 65), (65, 67, 65), (65, 67, 65), (133, 134, 133), (133, 134, 133), (133, 134, 133), (133, 134, 133), (0, 0, 0), (0, 0, 0), (133, 134, 133), (133, 134, 133), (133, 134, 133), (65, 67, 65), (0, 0, 0), (0, 0, 0), (0, 0, 0), (65, 67, 65), (195, 199, 196), (133, 134, 133), (65, 67, 65), (65, 67, 65), (0, 0, 0), (0, 0, 0), (65, 67, 65), (65, 67, 65)]
        for i in range(16):
            for j in range(16):
                vari = (round(a[i*16+j][0]*eta),round(a[i*16+j][1]*eta),round(a[i*16+j][2]*eta))
                pygame.draw.rect(naytto, vari, (x+(blokki_koko//16)*i, y+(blokki_koko//16)*j, blokki_koko//16, blokki_koko//16))


def piirra_ovi(x, y):
    if x>-blokki_koko and x<640+blokki_koko and y>-blokki_koko and y<480+blokki_koko:
        eta = 1-math.sqrt((x-320)**2+(y-240)**2)/600
        a =[(0, 0, 0), (0, 0, 0), (8, 5, 5), (71, 35, 27), (71, 35, 27), (135, 84, 84), (71, 35, 27), (8, 5, 5), (71, 35, 27), (71, 35, 27), (71, 35, 27), (135, 84, 84), (8, 5, 5), (71, 35, 27), (71, 35, 27), (71, 35, 27), (0, 0, 0), (0, 0, 0), (71, 35, 27), (71, 35, 27), (71, 35, 27), (71, 35, 27), (8, 5, 5), (71, 35, 27), (71, 35, 27), (71, 35, 27), (71, 35, 27), (8, 5, 5), (135, 84, 84), (71, 35, 27), (71, 35, 27), (71, 35, 27), (0, 0, 0), (8, 5, 5), (8, 5, 5), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (0, 0, 0), (135, 84, 84), (110, 65, 20), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (3, 2, 2), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (0, 0, 0), (71, 35, 27), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (3, 2, 2), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (8, 5, 5), (8, 5, 5), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (3, 2, 2), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (8, 5, 5), (8, 5, 5), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (71, 35, 27), (8, 5, 5), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (71, 35, 27), (8, 5, 5), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (8, 5, 5), (8, 5, 5), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (8, 5, 5), (8, 5, 5), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (0, 0, 0), (71, 35, 27), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (0, 0, 0), (71, 35, 27), (110, 65, 20), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (181, 107, 33), (110, 65, 20), (0, 0, 0), (8, 5, 5), (8, 5, 5), (110, 65, 20), (110, 65, 20), (3, 2, 2), (3, 2, 2), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (110, 65, 20), (3, 2, 2), (110, 65, 20), (110, 65, 20), (110, 65, 20), (0, 0, 0), (0, 0, 0), (71, 35, 27), (71, 35, 27), (71, 35, 27), (8, 5, 5), (8, 5, 5), (71, 35, 27), (71, 35, 27), (71, 35, 27), (8, 5, 5), (8, 5, 5), (8, 5, 5), (71, 35, 27), (71, 35, 27), (71, 35, 27), (0, 0, 0), (0, 0, 0), (8, 5, 5), (135, 84, 84), (71, 35, 27), (89, 60, 60), (71, 35, 27), (71, 35, 27), (135, 84, 84), (71, 35, 27), (71, 35, 27), (71, 35, 27), (135, 84, 84), (71, 35, 27), (135, 84, 84), (8, 5, 5)]
        for i in range(16):
            for j in range(16):
                vari = (round(a[i*16+j][0]*eta),round(a[i*16+j][1]*eta),round(a[i*16+j][2]*eta))
                pygame.draw.rect(naytto, vari, (x+(blokki_koko//16)*i, y+(blokki_koko//16)*j, blokki_koko//16, blokki_koko//16))


def piirra_lattia(x, y):
    if x>-blokki_koko and x<640+blokki_koko and y>-blokki_koko and y<480+blokki_koko:
        eta = 1-math.sqrt((x-320)**2+(y-240)**2)/600
        pygame.draw.rect(naytto, (70*eta, 46*eta, 8*eta), (x, y, blokki_koko, blokki_koko))
  

def saako_kolikon(x, y, kolikkon:int):

    if haamuvairobo == 0 or x<0 or x>blokki_koko*mappi_koko-hirvio.get_width() or  y<0 or y>blokki_koko*mappi_koko-hirvio.get_height():
        return 
    blokki_kordinaatit =  (x//blokki_koko, y//blokki_koko) 
    blokki_kordinaatit1 = ((x+robo.get_width())//blokki_koko, (y+robo.get_height())//blokki_koko)
    kx=blokki_koko//2
    ky=blokki_koko//2
    etaisyys = math.sqrt((blokki_kordinaatit[0]*blokki_koko+kx-x)**2+(blokki_kordinaatit[1]*blokki_koko+ky-y)**2)
    global tausta
    global rahan_maara
    if tausta[((blokki_kordinaatit[0]))+ ((blokki_kordinaatit[1])*mappi_koko)]==2 and etaisyys<50: 
        tausta[((blokki_kordinaatit[0]))+ ((blokki_kordinaatit[1])*mappi_koko)]=0
        rahan_maara+=1

    if tausta[((blokki_kordinaatit1[0]))+ ((blokki_kordinaatit1[1])*mappi_koko)]==2 and etaisyys<50:
    
        tausta[((blokki_kordinaatit1[0]))+ ((blokki_kordinaatit1[1])*mappi_koko)]=0
        rahan_maara+=1

    
def luo_tausta(x_pelaaja, y_pelaaja):
    for i in range(len(tausta)):
        x_sijainti = (i%mappi_koko)*blokki_koko-round(x_pelaaja*kerroin)-vakio_x
        y_sijainti = (i//mappi_koko)*blokki_koko-round(y_pelaaja*kerroin)-vakio_y
        if tausta[i]==1: 
            piirra_kivi_seina(x_sijainti, y_sijainti)
        if tausta[i]==0:
            piirra_lattia(x_sijainti, y_sijainti)
        if tausta[i]==2:
            piirra_lattia(x_sijainti, y_sijainti)
            naytto.blit(kolikko, (x_sijainti+blokki_koko//2, y_sijainti+blokki_koko//2))
        if tausta[i]==3:
            piirra_ovi(x_sijainti, y_sijainti)
        if tausta[i]==4:
            naytto.blit(robo, (x_sijainti, y_sijainti))
        if haamuvairobo == 0:
            naytto.blit(robo, (robotti_odottaa_x-round(x_pelaaja*kerroin)-vakio_x, robotti_odottaa_y-round(y_pelaaja*kerroin)-vakio_y) )
        if tausta[i]==5: 
            naytto.blit(ovi, (x_sijainti, y_sijainti))

    
def osuuko_seinaan(blokki_kordinaatit1, rahan_maar,tausta ):
    global rahan_maara
    if tausta[((blokki_kordinaatit1[0]))+((blokki_kordinaatit1[1])*mappi_koko)]==3:
        if rahan_maara!=0:
            rahan_maara-=1
            tausta[((blokki_kordinaatit1[0]))+((blokki_kordinaatit1[1])*mappi_koko)]=0
            return True
        else:
            return False
    if tausta[((blokki_kordinaatit1[0]))+((blokki_kordinaatit1[1])*mappi_koko)]==5 and haamuvairobo:
        teksti3 = fontti.render("Ronin ja Hannun pako", True, (255, 255,255))
        for i in range(1, 255):
            pygame.draw.rect(naytto, (255-i,255-i,255-i), (0,0,640,480))
            pygame.display.flip()
            time.sleep(0.01)
        time.sleep(2)
        naytto.blit(teksti3, (50, 200))
        pygame.display.flip()
        time.sleep(2)
        exit()


    if tausta[((blokki_kordinaatit1[0]))+((blokki_kordinaatit1[1])*mappi_koko)]==1:
        return False
    return True
    

def ei_tormaa(x, y,t):
    blokki_kordinaatit =  ((x+3)//blokki_koko, (y)//blokki_koko)
    blokki_kordinaatit1 = ((x+robo.get_width())//blokki_koko, (y+robo.get_height())//blokki_koko)
    blokki_kordinaatit2 = ((x+3)//blokki_koko, (y+robo.get_height())//blokki_koko)
    blokki_kordinaatit3 = ((x+robo.get_width())//blokki_koko, (y)//blokki_koko)

    if x<0 or blokki_koko*mappi_koko-robo.get_width()<x:
       return False
    if y<0 or blokki_koko*mappi_koko-1.2*robo.get_height()<y:
       return False
    return osuuko_seinaan(blokki_kordinaatit, rahan_maara, tausta) and osuuko_seinaan(blokki_kordinaatit1, rahan_maara, tausta) and osuuko_seinaan(blokki_kordinaatit2, rahan_maara,tausta) and osuuko_seinaan(blokki_kordinaatit3, rahan_maara,tausta)


def nayta_ohjeet():
        #pygame.draw.rect(naytto, (255,255,255, 50), (0, 100, 640, 200))
        otsikko = fontti.render("OHJE", False, (255,255,255))
        leipa1= fontti1.render("Olet haamu joka voi ohjata robottikehoa. Molemmissa olotiloissa on etunsa", True, (255,255,255))
        leipa2 = fontti1.render(" Tavoiteenasi on löytää uloskäynti ennen kuin on liian myöhäistä. Mieti ", True, (255,255,255))
        leipa3 = fontti1.render("tarkkaan  mihin menet. Muista myös aina maksaa ovimaksu.", True, (255,255,255))
        ohje  = fontti.render("ESC=poistu SPACE=vaihda", True, (255,255,255))
        naytto.blit(otsikko, (300, 50))
        naytto.blit(leipa1, (0, 100))
        naytto.blit(leipa2, (0,130 ))
        naytto.blit(leipa3, (0, 160))
        naytto.blit(ohje, (0,200 ))


def hahmon_vaihto():
        global robotti_odottaa_x
        global robotti_odottaa_y

          


tausta = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          1, 0, 0, 0, 3, 0, 0, 3, 0, 2, 0, 1, 1, 0, 0, 1,
          1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 1, 0, 0, 0, 1,
          1, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1,
          1, 0, 0, 0, 3, 0, 0, 1, 2, 1, 0, 3, 0, 1, 0, 1,
          1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
          1, 0, 0, 0, 0, 1, 0, 5, 1, 1, 3, 1, 1, 1, 0, 1,
          1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 1, 2, 1,
          1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
          1, 0, 0, 0, 0, 3, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
          1, 0, 0, 0, 1, 1, 0, 0,0, 0, 0, 1, 0, 0, 0, 1,
          1, 1, 3, 1, 1, 1, 1, 1,1, 1, 0, 0, 0, 0, 0, 1,
          1, 0, 2, 2, 1, 0, 0, 0,1, 1, 1, 1, 1, 1, 0, 1,
          1, 0, 0, 0, 1, 1, 1, 0,0, 0, 0, 0, 1, 1, 0, 1,
          1, 0, 0, 0, 1, 2, 0, 0, 1, 1, 0, 0, 0, 0, 2, 1,
          1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1]

pygame.init() 
blokki_koko=120
pygame.display.set_caption("Ronin ja Hannun pako")
rahan_maara=0
naytto = pygame.display.set_mode((640, 480))
hirvio = pygame.image.load("hirvio.png").convert_alpha()
hirvio.set_alpha(255)
ovi = pygame.image.load("ovi.png")
robo = pygame.image.load("robo.png")
kolikko = pygame.image.load("kolikko.png")
fontti = pygame.font.SysFont("copperplategothic", 35)
fontti1 = pygame.font.SysFont("copperplategothic", 15)

ovi= pygame.transform.scale(ovi, (blokki_koko, blokki_koko))    
x_pelaaja = 77
y_pelaaja = 50
vakio_x=-300
vakio_y=0
mappi_koko=int(math.sqrt(len(tausta)))
vasemmalle = False
oikealle = False
ylos = False
alas = False
haamuvairobo=1
robotti_odottaa_x =200
robotti_odottaa_y =200
robo_x=200
robo_y=200
nayta_ohje =0
kerroin=mappi_koko*blokki_koko/(480-hirvio.get_width()*3)-1

kello = pygame.time.Clock()

             


while True: 
    
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d:
                oikealle = True
            if tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_w:
                ylos = True
            if tapahtuma.key == pygame.K_DOWN or tapahtuma.key == pygame.K_s :
                alas= True
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()
            if tapahtuma.key == pygame.K_SPACE:
                haamuvairobo1 = (haamuvairobo+1)%2
                if haamuvairobo1:
                    
                    old_x=robo_x-x_pelaaja
                    old_y=robo_y-y_pelaaja
                    a = x_pelaaja
                    b = y_pelaaja
                    for i in range(1,100):
                        x_pelaaja = round(a+(old_x)*i/99)
                        y_pelaaja = round(b+(old_y)*i/99)
                        
                        luo_tausta(x_pelaaja, y_pelaaja)
                        naytto.blit(hirvio, (x_pelaaja, y_pelaaja))
                        pygame.display.flip()
                        kello.tick(60)
                else:
                    robotti_odottaa_x=delta_x
                    robotti_odottaa_y=delta_y
                    robo_x=x_pelaaja
                    robo_y = y_pelaaja
                haamuvairobo = (haamuvairobo+1)%2
    
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a :
                vasemmalle = False
                
            if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d :
                oikealle = False
            if tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_w :
                ylos = False
            if tapahtuma.key == pygame.K_DOWN or tapahtuma.key == pygame.K_s :
                alas= False
        if tapahtuma.type == pygame.MOUSEBUTTONUP:
            if tapahtuma.pos[0]>525 and tapahtuma.pos[1]<50:
                nayta_ohje=(nayta_ohje+1)%2
        if tapahtuma.type == pygame.QUIT:
            exit()
        
    delta_x=math.floor(x_pelaaja*(kerroin+1))+vakio_x
    delta_y=math.floor(y_pelaaja*(kerroin+1))+vakio_y
    hirvio.set_alpha(255)
    temp_v=vasemmalle
    temp_o=oikealle
    temp_a = alas
    temp_y = ylos
    
    if not ei_tormaa(delta_x-3, delta_y, "v"):
        if haamuvairobo:
            vasemmalle=False
        hirvio.set_alpha(100)
    if vasemmalle and delta_x-3>0: 
        x_pelaaja-=1

    if not ei_tormaa(delta_x,delta_y-4, "y"):
        if haamuvairobo:
            ylos=False
        hirvio.set_alpha(100)
    if ylos and delta_y-3>0:
        y_pelaaja-=1
   
    if not ei_tormaa(delta_x, delta_y+3, "a"):
        if haamuvairobo:
            alas=False
        hirvio.set_alpha(100)
    if alas  and delta_y+2<blokki_koko*mappi_koko-hirvio.get_height():
        y_pelaaja+=1


    if not ei_tormaa(delta_x+3, delta_y, "o"):
        if haamuvairobo:
            oikealle=False
        hirvio.set_alpha(100)
    if oikealle and delta_x+2<blokki_koko*mappi_koko-hirvio.get_width():
        x_pelaaja+=1

    vasemmalle = temp_v
    oikealle = temp_o
    ylos = temp_y
    alas = temp_a

    naytto.fill((0, 0, 0))
    luo_tausta(x_pelaaja, y_pelaaja)
    if haamuvairobo:
        naytto.blit(robo, (x_pelaaja, y_pelaaja))
    else:
       naytto.blit(hirvio, (x_pelaaja, y_pelaaja))

    saako_kolikon(delta_x, delta_y, rahan_maara)
    teksti1 = fontti.render(f"{rahan_maara} X", True, (212, 175, 55))
    teksti2 = fontti.render("OHJE", False, (255,255,255))
    naytto.blit(teksti2, (500, 10))
    naytto.blit(teksti1, (500, 50))
    naytto.blit(kolikko, (565,50))
    if nayta_ohje:
        nayta_ohjeet()
    pygame.display.flip()
    kello.tick(60)
        