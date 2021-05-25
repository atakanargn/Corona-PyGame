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
# Karakterin resim dosyasını çekiyoruz
karakter_sprite = pygame.image.load("imgs/karakter.png")
karakter_sprite.convert()

# pencereyi temizliyoruz
pencere.fill(0)
pygame.display.update()

# 4 virüsüde rastgele 4 köşeye atıyoruz
virus1_xy = [randint(40,200),randint(40,200)]
virus2_xy = [randint(300,460),randint(40,200)]
virus3_xy = [randint(40,200),randint(300,460)]
virus4_xy = [randint(300,460),randint(300,460)]
# Virüsleri rijit hale getiriyoruz ki "collide" yani çarpışma olayına
# girebilsinler
virus1_rect = pygame.Rect(virus1_xy[0]-26,virus1_xy[1]-26,52,52)
virus2_rect = pygame.Rect(virus2_xy[0]-26,virus2_xy[1]-26,52,52)
virus3_rect = pygame.Rect(virus3_xy[0]-26,virus3_xy[1]-26,52,52)
virus4_rect = pygame.Rect(virus4_xy[0]-26,virus4_xy[1]-26,52,52)

# Virüs resmimizi çekiyoruz
virus_sprite = pygame.image.load("imgs/virus.png")
virus_sprite.convert()

# Virüslerin hareket etme fonksiyonları, 4 virüs için de ayrıdır
def virus1_Hareket():
    global karakter_x,karakter_y,virus1_xy

    # Karakter hangi yönde ise o yöne doğru rastgele -6 ile 8 pixel hareket yaparlar
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

    # Karakter
    pencere.blit(karakter_sprite,(karakter_x-25,karakter_y-25))
    # VIRUS_1
    pencere.blit(virus_sprite,(virus1_xy[0]-30,virus1_xy[1]-30))
    # VIRUS_2
    pencere.blit(virus_sprite,(virus2_xy[0]-30,virus2_xy[1]-30))
    # VIRUS_3
    pencere.blit(virus_sprite,(virus3_xy[0]-30,virus3_xy[1]-30))
    # VIRUS_4
    pencere.blit(virus_sprite,(virus4_xy[0]-30,virus4_xy[1]-30))

    # Başkangıç yazıları
    TEXT_ORTA.render_to(pencere, (20, 20), "BAŞLAMAK İÇİN", (255,255,255))
    TEXT_ORTA.render_to(pencere, (20, 20+54), "OK TUŞLARINI KULLANIN", (255,255,255))
    pygame.display.update()

    # Escape tuşuna basılır ise oyun kapanır
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Yön tuşlarından herhangi birinde ise oyun başlar
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT] or key_input[pygame.K_UP] or key_input[pygame.K_RIGHT] or key_input[pygame.K_DOWN]:
        break

# Oyun döngüsü
while True:
    # Karakterimizin adım sayısı 8 ile 16 arasında sürekli değişmektedir
    # bu da bazen yavaş bazen hızlı hareketi sağlar
    adim_sayisi=randint(8,16)
    # süreyi saymak için anlık süreyi tuttuk
    start=time.time()
    # pencere temizlendi
    pencere.fill(0)

    # Karakter rijit şekilde, resmi ile beraber çizdirildi
    karakter = pygame.Rect((karakter_x-25, karakter_y-25, 25, 25))
    pencere.blit(karakter_sprite,(karakter_x-25,karakter_y-25))

    # Her karede virüslerin hareket etmesi sağlanıyor
    virus1_Hareket()
    virus2_Hareket()
    virus3_Hareket()
    virus4_Hareket()

    # Virüslerin rijit şekillerinin konumları güncelleniyor
    virus1_rect = pygame.Rect(virus1_xy[0]-26,virus1_xy[1]-26,52,52)
    virus2_rect = pygame.Rect(virus2_xy[0]-26,virus2_xy[1]-26,52,52)
    virus3_rect = pygame.Rect(virus3_xy[0]-26,virus3_xy[1]-26,52,52)
    virus4_rect = pygame.Rect(virus4_xy[0]-26,virus4_xy[1]-26,52,52)

    # Virüs resimleri çizdiriliyor
    # VIRUS_1
    pencere.blit(virus_sprite,(virus1_xy[0]-30,virus1_xy[1]-30))
    # VIRUS_2
    pencere.blit(virus_sprite,(virus2_xy[0]-30,virus2_xy[1]-30))
    # VIRUS_3
    pencere.blit(virus_sprite,(virus3_xy[0]-30,virus3_xy[1]-30))
    # VIRUS_4
    pencere.blit(virus_sprite,(virus4_xy[0]-30,virus4_xy[1]-30))

    # collide() fonksiyonu ile çarpışma durumu var mı? kontrol ediliyor
    # karakter.collid(virus1_rect) : karakter nesnesine, virus1_rect nesnesi çarptı mı? değiyor mu? demek
    # 4 virüs için de bunu kontrol ettik ve 'or' ile yazdık ki
    # herhangi birine temas ederse, collide değişkeni True döndürsün
    collide = karakter.colliderect(virus1_rect) or karakter.colliderect(virus2_rect) or karakter.colliderect(virus3_rect) or karakter.colliderect(virus4_rect)
    
    # Eğer karakter virüslerden herhangi birine değdiyse
    if collide:
        # Oyun müziği durdu
        pygame.mixer.music.stop()
        # Kazandın müziği yüklendi ama çaldırılmadı
        pygame.mixer.music.load('./sesler/kazandin.mp3')
        # Oyuncudan tepki beklemek için sonsuz döngüde bitiş ekranında kaldık
        while True:
            # Pencereyi temizle
            pencere.fill(0)
            # Yazıları yazdır
            TEXT_ORTA.render_to(pencere, (20, 20), "ÇIKIŞ İÇİN", (255,255,255))
            TEXT_ORTA.render_to(pencere, (20, 20+54), "ESC TUŞUNA BASIN.", (255,255,255))
            TEXT_BUYUK.render_to(pencere, (30, 200), "SÜRE : %0.2f"%sure, (255,255,255))
            # ölçülen süre 15ten büyükse
            # Kazanma müziği başlar ve yazı yazar
            if(sure>15):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Bağışıklık Kazandın", (0, 255, 0))
                pygame.mixer.music.play()
            # ölçülen süre 10dan büyükse
            # Kazanma müziği başlar ve yazı yazar
            elif(sure>10):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Aşı Kazandın", (0, 255, 255))
                pygame.mixer.music.play()
            # ölçülen süre 5den büyükse
            # Kazanma müziği başlar ve yazı yazar
            elif(sure>5):
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Dezenfektan kazandın", (255, 255, 0))
                pygame.mixer.music.play()
            # ölçülen süre 5den küçük ise
            # Kaybetme müziği yüklenir, başlar ve yazı yazar
            else:
                TEXT_ORTA.render_to(pencere, (30, 200+54), "- Kaybettin!", (0, 255, 0))
                pygame.mixer.music.load('./sesler/kaybettin.mp3')
                pygame.mixer.music.play()

            # ekran güncellenir
            pygame.display.update()
            while True:
                # Escape tuşuna basılırsa oyun biter
                for eve in pygame.event.get():
                    if eve.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                # Escape tuşuna basılırsa oyun biter
                key_input = pygame.key.get_pressed()
                if key_input[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
    
    # collide=False ise yani virüse değme durumu yok ise
    # oyun devam eder
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Klavyede basılan tuş çekilir
    key_input = pygame.key.get_pressed()

    # Basılan tuşa göre o yönde karakterin hareketi sağlanır
    # aynı zamanda hareket sağlanmadan önce oyun alanından çıkıyor mu diye kontrol edilir
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
    
    # Süre sürekli olacak güncellenir ve yukarıda yazar
    TEXT_KUCUK.render_to(pencere, (20, 20), "SURE : %0.2f"%sure, (255,255,255))
    pygame.display.update()
    fpsclock.tick(fps)
    # Her döngü tamamlandığında geçen zaman çekilir
    # ve geçen zamandan döngünün başındaki zaman çıkartılır ise
    # döngünün ne kadar sürdüğü hesaplanır
    # ve bu döngü süresi 'sure' değişkenine eklenince, sürekli olacak yukarıdaki oyun süresi elde edilir
    sure += time.time()-start