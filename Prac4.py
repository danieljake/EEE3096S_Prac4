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

def GetData(channel): # channel must be an integer 0-7

    adc = spi.xfer2([1,(8+channel)<<4,0]) # sending 3 bytes

    data = ((adc[1]&3) << 8) + adc[2]

    return data

#places=1

def ConvertVolts(data,places):

    volts = ((data * 3.3) / float(1023))/1000

    volts = round(volts,places)

    return volts



def ConvertTemp(volts,places):

    temp= (volts-0.5)/100

    temp= round(temp,places)

    return temp



def ConvertLight(data,places):

    light = (data/float(1023))*100

    # Define sensor channels

    light= round(light,0)

    return light



def Time_display(t):

    set_time=time.localtime(t)

    return(str(set_time.tm_min).zfill(2)+":"+str(set_time.tm_sec).zfill(2)+":"+str(t-int(t))[2:4])



#channel = 0 # Define delay between readings

delay = 0.5

### Interrupt switches

start=time.time()

out=""

space=""

counter=0

stopper=0

stop_start=0

def reset(channel):

    global start

    global space

    global counter

    space=""

    counter=0

    print ("RESET")

    system("clear")

def freq(channel):

    global delay

    print(delay)

    if (delay==0.5):

        print("Test")

        delay= 1

        print(delay)



    elif(delay ==1):

        delay= 2



    elif (delay== 2):

        delay =0.5



def stop(channel):

    global stop_start

    global counter

    if (stop_start==0):

        print("stop")

        stop_start=1



    elif (stop_start==1):

        print("continue")

        stop_start=0

        counter=0

        stopper=0

def display(channel):

    global stop_start

    if(stop_start==1):

        print("Time     Timer    Pot  Temp   Light")

        print(space)





GPIO.add_event_detect(reset_,	GPIO.RISING,	callback=reset,	bouncetime=200)

GPIO.add_event_detect(freq_,	GPIO.RISING,	callback=freq, bouncetime=200)

GPIO.add_event_detect(stop_,	GPIO.RISING,	callback=stop, bouncetime=200)

GPIO.add_event_detect(display_,	GPIO.RISING,	callback=display, bouncetime=200)



while (True and (stopper!=1)): # Read the data

    sensr_data = GetData(2)

    sensor_volt = ConvertVolts(sensr_data,2)

    temp_data = GetData(1)

    temp_val= ConvertTemp(temp_data,2)

    light_data= GetData(0)

    light_val = ConvertLight(light_data,0)

    out=Time_display(time.time())+ " " +Time_display(time.time()-start) + " "+"{}V {}C {}%".format(sensr_data,
