#!/usr/bin/python

import RPi.GPIO as GPIO, time, os, subprocess

# GPIO setup
GPIO.setmode (GPIO.BCM)
SWITCH = 24 	#Button
READY_LED = 17  #green LED
POSE_LED = 18	#yellow LED
BUSY_LED = 24	#red LED
GPIO.setup(SWITCH, GPIO.IN)
GPIO.setup(READY_LED, GPIO.OUT)
GPIO.setup(POSE_LED, GPIO.OUT)
GPIO.setup(BUSY_LED, GPIO.OUT)

GPIO.output(READY_LED, False)
GPIO.output(BUSY_LED, 0)
GPIO.output(POSE_LED, 0)

while True:
	if (GPIO.input(SWITCH)):
	snap = 0
	while snap < 4:
		print("POSE")
		GPIO.output(READY_LED, 0)
		GPIO.output(PSE_LED, 1)
		time.sleep(1.5)
		for i in range(5)
			GPIO.output(POSE_LED, 0)
			time.sleep(0.2)
			GPIO.output(POSE_LED, 1)
		for i in range(5)
			GPIO.output(POSE_LED, 0)
			time.sleep(0.1)
			GPIO.output(POSE_LED, 1)
			time.sleep(0.1)
		print("CLICK")
		gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/fotobox/fotobox_bilder/Fotobox%H%M.jpg", stderr=subprocess.STDOUT, shell=True)
		print(gpout)
    if "ERROR" not in gpout:
      snap += 1
     GPIO.output(POSE_LED,0)
     time.sleep(0.5)
    GPIO.output(BUSY_LED, 1)
    print("BITTE WARTEN - FOTO WIRD GEDRUCKT")
    #Bild zusammenstellen und an Drucker senden
    subprocess.call("sudo /home/pi/fotobox/scripts/collage_drucken", shell=True)
    time.sleep(30)
    GPIO.output(BUSY_LED, 0)
    GPIO.output(READY_LED, 1)
    GPIO.output(POSE_LED, 0)
    print("Fertig für die nächste Runde !!!")
finally:
  GPIO.cleanup()
