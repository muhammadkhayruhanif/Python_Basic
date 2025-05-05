import pygame

"""
ketika membuat game terdapat 4 step utama:
1. init -> penyebab loading lama
2. user input, database input -> input dari stik, masuk2in menu, dll
3. update asset -> dari input masuk ke sini
4. render ke display -> render ke layar (paling berat)
"""

# init
pygame.init()

# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# posisi/koordinat
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed

    # ambil ke atas
    if keys[pygame.K_UP] and x > 0:
        x -= speed

    # ambil ke bawah
    if keys[pygame.K_DOWN] and x < window_panjang - panjang:
        x += speed

# update asset
window.fill((255,255,255))
pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))

# render ke display
pygame.display.update()

pygame.quit()

# terdapat error ketika di-run, entah karena update library jadi ada syntax baru
# atau karena kesalahan syntax itu sendiri