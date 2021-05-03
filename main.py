# Python oyun kütüphanesi
import pygame
# Yazı yazdırmak için
import pygame.freetype
import sys

# Rastgele sayı kütüphanesi
from random import randint
# Süre hesaplamak için kullanılan kütüphane
import time

# pygame kütüphanesini başlattık
pygame.init()

# Müziği yüklüyoruz, sesini biraz düşürüyoruz ve başlatıyoruz
pygame.mixer.init()
pygame.mixer.music.load('./sesler/arkaplan.mp3')
pygame.mixer.music.play(-1)

# oyun fps'i 60'a sabitledik
fps=60
fpsclock=pygame.time.Clock()

# pencereyi 500x500 boyutlarına ayarlıyoruz
pencere=pygame.display.set_mode((500,500))
# Oyun penceresi başlığı
pygame.display.set_caption("It's Corona Time!")

# Yazı stilini yükledik, yazı boyutunu ayarladık
TEXT_KUCUK = pygame.freetype.Font('./fonts/Piacevoli.ttf', 36)
TEXT_ORTA  = pygame.freetype.Font('./fonts/Piacevoli.ttf', 48)
TEXT_BUYUK = pygame.freetype.Font('./fonts/Piacevoli.ttf', 72)

# Karakterin başlangıc koordinatlarını pencerenin ortasına sabitliyoruz
karakter_x=pencere.get_rect().center[0]
karakter_y=pencere.get_rect().center[1]

# Adım sayısını 10 olarak ayarladık
adim_sayisi=randint(8,16)

# Karakterimizin şeklini belirliyoruz
karakter = pygame.Rect((karakter_x-25, karakter_y-25, 25, 25))
# Karakteri çizdiriyoruz
pencere.fill(0)
pygame.display.update()

virus1_xy = [randint(40,200),randint(40,200)]
virus2_xy = [randint(300,460),randint(40,200)]
virus3_xy = [randint(40,200),randint(300,460)]
virus4_xy = [randint(300,460),randint(300,460)]

virus1_rect = pygame.Rect(virus1_xy[0]-26,virus1_xy[1]-26,52,52)
virus2_rect = pygame.Rect(virus2_xy[0]-26,virus2_xy[1]-26,52,52)
virus3_rect = pygame.Rect(virus3_xy[0]-26,virus3_xy[1]-26,52,52)
virus4_rect = pygame.Rect(virus4_xy[0]-26,virus4_xy[1]-26,52,52)

def virus1_Hareket():
    global karakter_x,karakter_y,virus1_xy
    if karakter_x<virus1_xy[0]:
        virus1_xy[0]-=randint(-6,8)
    else:
        virus1_xy[0]+=randint(-6,8)
    if karakter_y<virus1_xy[1]:
        virus1_xy[1]-=randint(-6,8)
    else:
        virus1_xy[1]+=randint(-6,8)

def virus2_Hareket():
    global karakter_x,karakter_y,virus2_xy
    if karakter_x<virus2_xy[0]:
        virus2_xy[0]-=randint(-6,8)
    else:
        virus2_xy[0]+=randint(-6,8)
    if karakter_y<virus2_xy[1]:
        virus2_xy[1]-=randint(-6,8)
    else:
        virus2_xy[1]+=randint(-6,8)

def virus3_Hareket():
    global karakter_x,karakter_y,virus3_xy
    if karakter_x<virus3_xy[0]:
        virus3_xy[0]-=randint(-6,8)
    else:
        virus3_xy[0]+=randint(-6,8)
    if karakter_y<virus3_xy[1]:
        virus3_xy[1]-=randint(-6,8)
    else:
        virus3_xy[1]+=randint(-6,8)

def virus4_Hareket():
    global karakter_x,karakter_y,virus4_xy
    if karakter_x<virus4_xy[0]:
        virus4_xy[0]-=randint(-6,8)
    else:
        virus4_xy[0]+=randint(-6,8)
    if karakter_y<virus4_xy[1]:
        virus4_xy[1]-=randint(-6,8)
    else:
        virus4_xy[1]+=randint(-6,8)

sure = 0.0
while True:
    pencere.fill(0)

    pygame.draw.rect(pencere, (255,0,0), karakter)

    # VIRUS_1
    pygame.draw.rect(pencere, (50,150,50), virus1_rect)
    pygame.draw.circle(pencere,(0,255,0),virus1_xy,30.0)
    # VIRUS_2
    pygame.draw.rect(pencere, (50,150,50), virus2_rect)
    pygame.draw.circle(pencere,(0,255,0),virus2_xy,30.0)
    # VIRUS_3
    pygame.draw.rect(pencere, (50,150,50), virus3_rect)
    pygame.draw.circle(pencere,(0,255,0),virus3_xy,30.0)
    # VIRUS_4
    pygame.draw.rect(pencere, (50,150,50), virus4_rect)
    pygame.draw.circle(pencere,(0,255,0),virus4_xy,30.0)

    TEXT_ORTA.render_to(pencere, (20, 20), "BAŞLAMAK İÇİN", (255,255,255))
    TEXT_ORTA.render_to(pencere, (20, 20+54), "OK TUŞLARINI KULLANIN", (255,255,255))
    pygame.display.update()

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT] or key_input[pygame.K_UP] or key_input[pygame.K_RIGHT] or key_input[pygame.K_DOWN]:
        break
    
while True:
    adim_sayisi=randint(8,16)
    start=time.time()
    pencere.fill(0)

    karakter = pygame.Rect((karakter_x-25, karakter_y-25, 25, 25))
    pygame.draw.rect(pencere, (255,0,0), karakter)

    virus1_Hareket()
    virus2_Hareket()
    virus3_Hareket()
    virus4_Hareket()

    virus1_rect = pygame.Rect(virus1_xy[0]-26,virus1_xy[1]-26,52,52)
    virus2_rect = pygame.Rect(virus2_xy[0]-26,virus2_xy[1]-26,52,52)
    virus3_rect = pygame.Rect(virus3_xy[0]-26,virus3_xy[1]-26,52,52)
    virus4_rect = pygame.Rect(virus4_xy[0]-26,virus4_xy[1]-26,52,52)

    # VIRUS_1
    pygame.draw.rect(pencere, (50,150,50), virus1_rect)
    pygame.draw.circle(pencere,(0,255,0),virus1_xy,30.0)
    # VIRUS_2
    pygame.draw.rect(pencere, (50,150,50), virus2_rect)
    pygame.draw.circle(pencere,(0,255,0),virus2_xy,30.0)
    # VIRUS_3
    pygame.draw.rect(pencere, (50,150,50), virus3_rect)
    pygame.draw.circle(pencere,(0,255,0),virus3_xy,30.0)
    # VIRUS_4
    pygame.draw.rect(pencere, (50,150,50), virus4_rect)
    pygame.draw.circle(pencere,(0,255,0),virus4_xy,30.0)

    collide = karakter.colliderect(virus1_rect) or karakter.colliderect(virus2_rect) or karakter.colliderect(virus3_rect) or karakter.colliderect(virus4_rect)
    
    if collide:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('./sesler/kazandin.mp3')
        while True:
            pencere.fill(0)
            TEXT_ORTA.render_to(pencere, (20, 20), "ÇIKIŞ İÇİN", (255,255,255))
            TEXT_ORTA.render_to(pencere, (20, 20+54), "ESC TUŞUNA BASIN.", (255,255,255))
            TEXT_BUYUK.render_to(pencere, (30, 200), "SÜRE : %0.2f"%sure, (255,255,255))
            if(sure>15):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Bağışıklık Kazandın", (0, 255, 0))
                pygame.mixer.music.play()
            elif(sure>10):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Aşı Kazandın", (0, 255, 255))
                pygame.mixer.music.play()
            elif(sure>5):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Dezenfektan kazandın", (255, 255, 0))
                pygame.mixer.music.play()
            else:
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Kaybettin!", (0, 255, 0))
                pygame.mixer.music.load('./sesler/kaybettin.mp3')
                pygame.mixer.music.play()

            pygame.display.update()
            while True:
                for eve in pygame.event.get():
                    if eve.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                key_input = pygame.key.get_pressed()
                if key_input[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        karakter_x -= adim_sayisi
        if(karakter_x<=25):
            karakter_x=25
    if key_input[pygame.K_UP]:
        karakter_y -= adim_sayisi
        if(karakter_y<=25):
            karakter_y=25
    if key_input[pygame.K_RIGHT]:
        karakter_x += adim_sayisi
        if(karakter_x>=500):
            karakter_x=500
    if key_input[pygame.K_DOWN]:
        karakter_y += adim_sayisi
        if(karakter_y>=500):
            karakter_y=500
    
    TEXT_KUCUK.render_to(pencere, (20, 20), "SURE : %0.2f"%sure, (255,255,255))
    pygame.display.update()
    fpsclock.tick(fps)
    sure += time.time()-start