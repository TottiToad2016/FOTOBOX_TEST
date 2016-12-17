#!/usr/bin/env python

import RPi.GPIO as GPIO 
import time 
import subprocess
import os
import cups # Drucker
from datetime import datetime
from glob import glob
from sys import exit
#from time import sleep, clock

from PIL import Image

from gui import GUI_PyGame as GuiModule
from camera import CameraException, Camera_gPhoto as CameraModule
from slideshow import Slideshow
#from events import Rpi_GPIO as GPIO

pygame.mouse.set_visible(0) # Mousezeiger unsichtbar ?

##################
### GPIO setup ###
##################

GPIO.setmode(GPIO.BCM)
SWITCH = 24
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
RESET = 25
GPIO.setup(RESET, GPIO.IN)
PRINT_LED = 22
POSE_LED = 18
BUTTON_LED = 23
GPIO.setup(POSE_LED, GPIO.OUT)
GPIO.setup(BUTTON_LED, GPIO.OUT)
GPIO.setup(PRINT_LED, GPIO.OUT)
GPIO.output(BUTTON_LED, True)
GPIO.output(PRINT_LED, False)

#####################
### Configuration ###
#####################

# Screen size
display_size = (1920, 1080)

# Maximum size of assembled image
image_size = (2144, 1424)

# Size of pictures in the assembled image
thumb_size = (1072, 712)

# Image basename
picture_basename = datetime.now().strftime("%Y-%m-%d/pic")

# Waiting time in seconds for posing
pose_time = 3

# Display time for assembled picture
display_time = 10

# Show a slideshow of existing pictures when idle
idle_slideshow = True

# Display time of pictures in the slideshow
slideshow_display_time = 5


########################
### Class definieren ###
########################

class Photobooth:
    """The main class.
    It contains all the logic for the photobooth.
    """

    def __init__(self, display_size, picture_basename, picture_size, pose_time, display_time,
                 trigger_channel, shutdown_channel, lamp_channel, idle_slideshow, slideshow_display_time):
        self.display      = GuiModule('Photobooth', display_size)
        self.pictures     = PictureList(picture_basename)
        self.camera       = CameraModule(picture_size)

        self.pic_size     = picture_size
        self.pose_time    = pose_time
        self.display_time = display_time

        self.trigger_channel  = trigger_channel
        self.shutdown_channel = shutdown_channel
        self.lamp_channel     = lamp_channel

        self.idle_slideshow = idle_slideshow
        if self.idle_slideshow:
            self.slideshow_display_time = slideshow_display_time
            self.slideshow = Slideshow(display_size, display_time, 
                                       os.path.dirname(os.path.realpath(picture_basename)))

        input_channels    = [ trigger_channel, shutdown_channel ]
        output_channels   = [ lamp_channel ]
        self.gpio         = GPIO(self.handle_gpio, input_channels, output_channels)
