import pygame
import time
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
image1 = pygame.image.load("images/image1.jpg")
image2 = pygame.image.load("images/image2.jpg")
image3 = pygame.image.load("images/image3.jpg")
font = pygame.font.SysFont("comicsansms",60)
print(pygame.font.get_fonts())
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(image1,(0,0))
    text = font.render("Happy Birthday Dad",True,"black")
    screen.blit(text,(10,250))
    pygame.display.update()

    time.sleep(2)

    screen.blit(image2,(0,0))
    text = font.render("How old are you now",True,"black")
    screen.blit(text,(10,250))
    pygame.display.update()
    time.sleep(2)



    time.sleep(2)
    
    screen.blit(image3,(0,0))
    text = font.render("i wish you all the good \n in the world",True,"black")
    screen.blit(text,(10,250))
    pygame.display.update()
    time.sleep(2)
