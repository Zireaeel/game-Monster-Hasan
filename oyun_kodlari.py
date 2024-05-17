import pygame
import random

pygame.init()
GENISLIK, YUKSEKLIK = 640,360
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Monster Hasan")

HIZ = 5
FPS = 50
saat = pygame.time.Clock()

#karakter veya görüntü atama
hasan = pygame.image.load("veri/monster.png")
hasan_koordinat = hasan.get_rect()
hasan_koordinat.topleft = (GENISLIK/2, YUKSEKLIK/2)

yem = pygame.image.load("veri/hamburger.png")
yem_koordinat = yem.get_rect()
yem_koordinat.topleft = (150, 150)

arka_plan = pygame.image.load("veri/arka_plan_monster_hasan.jpg")

oyun_bitti_goruntusu = pygame.image.load("veri/game_over_yazisi_640x360.jpg")

#sesler
arka_plan_sesi = pygame.mixer.Sound("veri/arka_plan_music.mp3")
arka_plan_sesi.set_volume(0.09)
arka_plan_sesi.play(-1,0)
#arka_plan_sesi = pygame.mixer.music.load("arka_plan_music.mp3")
#pygame.mixer.music.play(-1,0.0)
level_yukselme_sesi = pygame.mixer.Sound("veri/level_up_music.mp3")
level_yukselme_sesi.set_volume(20)
yem_ses = pygame.mixer.Sound("veri/yeme_sesi.mp3")
yem_ses.set_volume(0.15)
son_level_yukselme_sesi = pygame.mixer.Sound("veri/son_seviye_yukselme_sesi.mp3")
son_level_yukselme_sesi.set_volume(0.15)
kazanma_ses = pygame.mixer.Sound("veri/kazanma_sesi.mp3")
kazanma_ses.set_volume(1)

#Font ayarı
FONT1 = pygame.font.SysFont("calibri", 40)
FONT2 = pygame.font.SysFont("terminal", 40)
FONT3 = pygame.font.SysFont("calibri", 40)

#renkler
MAVI = (0,0,255)
YESIL = (0,255,0)
KIRMIZI = (255,0,0)
MOR = (255,0,255)
SARI = (255,255,0)
SIYAH = (0,0,0)
BEYAZ = (200,200,200)

#değişen değişken
A = 0
level = 0
skor = 0

#fonskiyon tanımlama
def restart_the_game():
    global skor, level, hasan_koordinat, yem_koordinat, A, hasan
    A = 0
    skor = 0
    level = 0
    hasan = pygame.image.load("veri/monster.png")
    hasan_koordinat = hasan.get_rect()
    hasan_koordinat.topleft = (192, 90)
    yem_koordinat.topleft = (150,150)

#Oyun döngüsü
durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False
        elif event.type == pygame.KEYDOWN:
            if skor == 150 and level == 4:
                if event.key == pygame.K_r:
                    restart_the_game()
                elif event.key == pygame.K_ESCAPE:
                    durum = False    
            if event.key == pygame.K_ESCAPE:
                durum = False

    pencere.blit(arka_plan,(0,0))
    pencere.blit(hasan, hasan_koordinat)
    pencere.blit(yem, yem_koordinat)

    skor_yazi = FONT1.render("Score: " + str(skor) + " ", True, SARI)
    skor_yazi_koordinat = skor_yazi.get_rect()
    skor_yazi_koordinat.topleft = (10,10)

    oyun_ismi_yazisi = FONT2.render(" Monster Hasan ",True,YESIL, )
    oyun_ismi_yazisi_koordinat = oyun_ismi_yazisi.get_rect()
    oyun_ismi_yazisi_koordinat.topleft = (210,10)

    level_yazisi = FONT3.render("Level: " + str(level) + " ", True, MOR)
    level_yazisi_koordinat = level_yazisi.get_rect()
    level_yazisi_koordinat.topleft = (500,10)

    pygame.draw.line(pencere,KIRMIZI,(0,55),(640,55),2)
    pencere.blit(oyun_ismi_yazisi,oyun_ismi_yazisi_koordinat)
    pencere.blit(skor_yazi, skor_yazi_koordinat)
    pencere.blit(level_yazisi,level_yazisi_koordinat)

    if skor == 10 and level == 0:
        hasan = pygame.image.load("veri/monster(1).png")
        if A == 0:
            level_yukselme_sesi.play()
            hasan_koordinat = hasan.get_rect()
            hasan_koordinat.topleft = (192, 90)
            A += 1
            level += 1

    if skor == 20 and level == 1:
        hasan = pygame.image.load("veri/monster(2).png")
        if A == 1:
            level_yukselme_sesi.play()
            hasan_koordinat = hasan.get_rect()
            hasan_koordinat.topleft = (192, 90)
            A += 1
            level += 1

    if skor == 50 and level == 2:
        hasan = pygame.image.load("veri/monster(3).png")
        if A == 2:
            level_yukselme_sesi.play()
            hasan_koordinat = hasan.get_rect()
            hasan_koordinat.topleft = (192, 90)
            A += 1
            level += 1

    if skor == 100 and level == 3:
        hasan = pygame.image.load("veri/monster(4).png")
        if A == 3:
            son_level_yukselme_sesi.play()
            hasan_koordinat = hasan.get_rect()
            hasan_koordinat.topleft = (192,90)
            A += 1
            level += 1

    if skor == 150 and level == 4:
        kazanma_ses.play()
        if A == 4:
            yem_koordinat.topleft = (0,0)
            pencere.blit(yem, yem_koordinat)
            pencere.blit(oyun_bitti_goruntusu,(0,0))

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and hasan_koordinat.left > 0:
        hasan_koordinat.x -= HIZ
    elif tus[pygame.K_RIGHT] and hasan_koordinat.right < GENISLIK:
        hasan_koordinat.x += HIZ
    elif tus[pygame.K_UP] and hasan_koordinat.top > 55 :
        hasan_koordinat.y -= HIZ
    elif tus[pygame.K_DOWN] and hasan_koordinat.bottom < YUKSEKLIK:
        hasan_koordinat.y += HIZ

    elif tus[pygame.K_a] and hasan_koordinat.left > 0:
        hasan_koordinat.x -= HIZ
    elif tus[pygame.K_d] and hasan_koordinat.right < GENISLIK:
        hasan_koordinat.x += HIZ
    elif tus[pygame.K_w] and hasan_koordinat.top > 55:
        hasan_koordinat.y -= HIZ
    elif tus[pygame.K_s] and hasan_koordinat.bottom < YUKSEKLIK:
        hasan_koordinat.y += HIZ

    if hasan_koordinat.colliderect(yem_koordinat):
        yem_ses.play()
        yem_koordinat.x = random.randint(0,GENISLIK-32)
        yem_koordinat.y = random.randint(55,YUKSEKLIK-32)
        skor += 1

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
