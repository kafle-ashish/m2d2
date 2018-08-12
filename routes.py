from flask import render_template, jsonify
from sqlalchemy_imageattach.context import store_context
from app import app
from packages.gpsread import get_cords
from packages.dht_data_read import get_data
import threading
from app import db
from models import DHT
from packages.gpio_control import GPIOControl
gpio_control = GPIOControl()

#from requests import get
#from base64 import b64encode


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/dashboard')
@app.route('/dashboard/dht11')
def dht11():
    return render_template("dht11.html")

@app.route('/dashboard/picamera')
def picamera():
    return render_template("pi-cam.html")

@app.route('/left')
def left():
    print("Moving left")
    th = threading.Thread(target=gpio_control.right, daemon=True)
    th.start()
    return "nothing"

@app.route('/forward')
def forward():
    print("Moving forward")
    th = threading.Thread(target=gpio_control.forward, daemon=True)
    th.start()
    return "nothing"

@app.route('/right')
def right():
    print("Moving right")
    th = threading.Thread(target=gpio_control.left, daemon=True)
    th.start()
    return "nothing"

@app.route('/back')
def back():
    print("Moving back")
    th = threading.Thread(target=gpio_control.reverse, daemon=True)
    th.start()
    return "nothing"

@app.route('/wait')
def wait():
    print("Waiting")
    th = threading.Thread(target=gpio_control.wait, daemon=True)
    th.start()
    return "nothing"

@app.route('/gpsdata', methods=['GET', 'POST'])
def gpsdata():
    print("Sending gps data")
    data = get_cords()
    print(data)
    return jsonify(data)
    #return jsonify({"lat":27.675064, "lon":85.332715})

@app.route('/dhtdata', methods=['GET', 'POST'])
def dhtdata():
    print("Sending dht data")
    data = get_data()
    #print(data)
    update = DHT(date = data['Date'], temperature = data['Temperature'], humidity = data['Humidity'])
    db.session.add(update)
    db.session.commit()
    return jsonify(data)

@app.route('/dhtreadings', methods = ['GET', 'POST'])
def dhtreadings():
    data = DHT.query.order_by(DHT.date).all()
    buffer = []
    #i = 0
    for item in data:
        buffer.append({"Date": item.date, "Temperature": item.temperature, "Humidity": item.humidity})
        #i += 1
        #if i == 21:
        #    break
    #print(buffer)
    return jsonify(buffer)
'''       
@app.route('/picam', methods = ['GET', 'POST'])
def picam():
    data = Picam.query.order_by(Picam.date).all()
    images = []
    for blobs in data:
        images.append(b64encode(blobs))
    return images


@app.route('/forcedb')
def forcedb():
    try:
        data = ''
        image_binary = get('http://192.168.0.107:8000/stream.mjpg').content
        with store_context(store):
           Picam.image.from_blob(image_binary)
    except Exception as e:
        print(e)
    db.session.commit()
    '''