import requests
import json

DHT_URL = "https://dweet.io/dweet/for/m2d2-dht?"
def http_post(URL, DATA):
    try:
        requests.post(URL, data=DATA)
    except Exception as e:
        print("Sensor data post error: ", str(e))
    return
