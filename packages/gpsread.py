import serial
import RPi.GPIO as GPIO
import os
import time
import pynmea2
import string

def conv_cords(cordinate):
    first_two_digits = int(cordinate/100)
    next_two_digits = cordinate - float(first_two_digits*100)
    final_answer = float(first_two_digits)  + float(next_two_digits)/60
    #print("final answer is gps {}".format(final_answer))
    return final_answer

def get_cords():
    #for i in range(5):
    try:
        port =serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
        #"/dev/ttyS0" for raspberrypi zero, "/dev/ttyAMA0" for raspberrypi 3
        dataout = pynmea2.NMEAStreamReader()
        newdata = port.readline().decode("utf-8")
        #print(newdata[0:5])
        if newdata[0:5] == 'GPGGA':
            newmsg = pynmea2.parse(newdata)
            lat = float(newmsg.lat)
            lon = float(newmsg.lon)
            #print("Latitude : {} Longitude : {}".format(lat, long))
            if lat != None and lon != None:
                lat = conv_cords(lat)
                lon = conv_cords(lon)
                return {"lat":lat, "lon":lon}
            else:
                return {"lat":27.675064, "lon":85.332715}
    except Exception as e:
        print("get_cords error: {}".format(e))

#get_cords()

