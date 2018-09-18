Python 2.7.13 (default, Nov 24 2017, 17:33:09)

[GCC 6.3.0 20170516] on linux2

Type "copyright", "credits" or "license()" for more information.

import spidev

import RPi.GPIO as GPIO

#spi= spidev.SpiDev()

#import spidev

import time

import datetime

from os import system

import os

import sys # Open SPI bus

GPIO.setmode(GPIO.BOARD)

spi = spidev.SpiDev() # create spi object

spi.open(0,0)

spi.max_speed_hz=1000000



reset_ =3

freq_=5

stop_=13

display_=11

#setup for switches

GPIO.setup(reset_, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(freq_, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(stop_, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(display_, GPIO.IN, pull_up_down=GPIO.PUD_UP)



GPIO.setwarnings(False)

#GPIO.setup(SPIMOSI,GPIO.OUT)

#GPIO.setup(SPIMISO,GPIO.IN)

#GPIO.setup(SPICLK,GPIO.OUT)

#GPIO.setup(SPICS,GPIO.OUT)
