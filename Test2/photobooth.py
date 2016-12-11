#! /etc/python
 
import pygame
import pygame, sys
import time
from pygame.locals import*
import datetime as dt
import os
 
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("comicsansms", 600)
n1 = font.render("1",1,(255,0,0))
n2 = font.render("2",1,(255,0,0))
n3 = font.render("3",1,(255,0,0))
n4 = font.render("4",1,(255,0,0))
n5 = font.render("5",1,(255,0,0))
smile = font .render("SMILE!",1,(255,0,0))
please = font .render("Please",1,(255,0,0))
wait = font .render("Wait",1,(255,0,0))
 
w = pygame.display.Info().current_w
h = pygame.display.Info().current_h
size = w, h
 
screen = pygame.display.set_mode(size)
 
'''This code works for camera control'''
#from subprocess import call
#call(["gphoto2", "--auto-detect"])
#call(["gphoto2", "--capture-image-and-download"])
 
#Initial setup
background = pygame.image.load("Background 2.jpg")
background = pygame.transform.scale(background, (1428,952))
start = pygame.image.load("Start.jpg")
start = pygame.transform.scale(start, (1428,952))
screen.blit(start, (174,0))
pygame.display.flip()
 
 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_f:
            pygame.display.toggle_fullscreen()
        if event.type == KEYDOWN and event.key == K_RETURN:
             
             
            #Countdown
            blackColor = pygame.Color(0,0,0)
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            pygame.display.flip()
            blackColor = pygame.Color(0,0,0)
            screen.blit(n5, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n4, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n3, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n2, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n1, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(smile, ((w-smile.get_width())//2, (h-smile.get_height())//2))
            pygame.display.flip()
             
            #Image 1
            from subprocess import call
            call(["gphoto2", "--auto-detect"])
            start = dt.datetime.now()
            timestamp1 = "/home/pi/Desktop/Capture-" + start.strftime("%y%m%d%H%M%S") + ".jpg"
            print timestamp1
            call(["gphoto2", "--capture-image-and-download","--filename",timestamp1])
            #check file exists
            while os.path.exists(timestamp1) == False:
                time.sleep(.1)
            image1 = pygame.image.load(timestamp1)
            image1 = pygame.transform.scale(image1, (size))
            screen.blit(image1, (0,0))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n3, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n2, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n1, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(smile, ((w-smile.get_width())//2, (h-smile.get_height())//2))
            pygame.display.flip()
         
            #Image 2
            from subprocess import call
            call(["gphoto2", "--auto-detect"])
            start = dt.datetime.now()
            timestamp2 = "/home/pi/Desktop/Capture-" + start.strftime("%y%m%d%H%M%S") + ".jpg"
            print timestamp2
            call(["gphoto2", "--capture-image-and-download","--filename",timestamp2])
            #check file exists
            while os.path.exists(timestamp2) == False:
                time.sleep(.1)
            image2 = pygame.image.load(timestamp2)
            image2 = pygame.transform.scale(image2, (size))
            screen.blit(image2, (0,0))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n3, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n2, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n1, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(smile, ((w-smile.get_width())//2, (h-smile.get_height())//2))
            pygame.display.flip()
         
            #Image 3
            from subprocess import call
            call(["gphoto2", "--auto-detect"])
            start = dt.datetime.now()
            timestamp3 = "/home/pi/Desktop/Capture-" + start.strftime("%y%m%d%H%M%S") + ".jpg"
            print timestamp3
            call(["gphoto2", "--capture-image-and-download","--filename",timestamp3])
            #check file exists
            while os.path.exists(timestamp3) == False:
                time.sleep(.1)
            image3 = pygame.image.load(timestamp3)
            image3 = pygame.transform.scale(image3, (size))
            screen.blit(image3, (0,0))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n3, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n2, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(n1, ((w-n5.get_width())//2, (h-n5.get_height())//2))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(smile, ((w-smile.get_width())//2, (h-smile.get_height())//2))
            pygame.display.flip()
         
            #Image 4
            from subprocess import call
            call(["gphoto2", "--auto-detect"])
            start = dt.datetime.now()
            timestamp4 = "/home/pi/Desktop/Capture-" + start.strftime("%y%m%d%H%M%S") + ".jpg"
            print timestamp4
            call(["gphoto2", "--capture-image-and-download","--filename",timestamp4])
            #check file exists
            while os.path.exists(timestamp4) == False:
                time.sleep(.1)
            image4 = pygame.image.load(timestamp4)
            image4 = pygame.transform.scale(image4, (size))
            screen.blit(image4, (0,0))
            pygame.display.flip()
            time.sleep(1)
             
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            screen.blit(please, ((w-please.get_width())//2, 50))
            screen.blit(wait, ((w-wait.get_width())//2,500))
            pygame.display.flip()
             
            #Create composite image
            blackColor = pygame.Color(0,0,0)
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            #background = pygame.image.load("Background 2.jpg")
            #background = pygame.transform.scale(background, (1428,952))
             
            pbimage1 = pygame.image.load(timestamp1)
            pbimage1 = pygame.transform.scale(pbimage1, (522,348))
             
            pbimage2 = pygame.image.load(timestamp2)
            pbimage2 = pygame.transform.scale(pbimage2, (522,348))
             
            pbimage3 = pygame.image.load(timestamp3)
            pbimage3 = pygame.transform.scale(pbimage3, (522,348))
             
            pbimage4 = pygame.image.load(timestamp4)
            pbimage4 = pygame.transform.scale(pbimage4, (522,348))
             
            screen.blit(background, (174, 0))
            screen.blit(pbimage1, (253.33,79.33))
            screen.blit(pbimage2, (998.67,79.33))
            screen.blit(pbimage3, (253.33,443.86))
            screen.blit(pbimage4, (998.67,443.86))
            pygame.display.flip()
             
            pygame.image.save(screen, "Photo" + start.strftime("%y%m%d%H%M%S") + ".jpg")
            time.sleep(10)
            blackColor = pygame.Color(0,0,0)
            pygame.draw.rect(screen,blackColor,Rect(0,0,w,h))
            start = pygame.image.load("Start.jpg")
            start = pygame.transform.scale(start, (1428,952))
            screen.blit(start, (174,0))
            pygame.display.flip()
        pygame.display.flip()
   
