import requests
import json

def get_data():
        
        #print("Connecting to dweet.io")
        try:
                data = requests.get("http://dweet.io/get/latest/dweet/for/m2d2").text
                data = json.loads(data)
                #print("Data is {}".format(data))
                return list(data['with'][0]['content'].keys())
        except Exception as e:
                print("Control Fetch Error: ",str(e))
                return("['0000']")

