import urllib.request
from datetime import datetime

def get_image(ip='192.168.0.107', port='8000'):

    url = 'http://{}:{}/stream.mjpg'.format(ip, port)
    try:
        urllib.request.urlretrieve(url, '/home/pi/m2d2/m2d2-images/{}.mjpg'.format(datetime.now()))
        
    except IOError as e:
        print("get_image error : {}".format(e))
        