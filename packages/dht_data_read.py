import sys
import Adafruit_DHT
import datetime
import json

DATA_PIN = 4

def get_data():
    DATA = {}
    try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DATA_PIN)
        #print(humidity,temperature)
        DATA.update({"Date":"{}".format(datetime.datetime.now())})
        DATA.update({"Humidity":humidity})
        DATA.update({"Temperature":temperature})
        return DATA

    except Exception as e:
        print("DHT sensor data read error: {}".format(str(e)))
        return {"Date":"{}".format(datetime.datetime.now()), "Humidity":0, "Temperature":0}
