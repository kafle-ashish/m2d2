from app import db

class DHT(db.Model):
    #__bind_key__ = 'comments'
    date = db.Column(db.String(20),primary_key=True)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
'''
class Picam(db.Model):
    #__bind_key__ = 'picam'
    #date = db.Column(db.String(20),primary_key=True)
    #image = db.Column(db.Blob())
    pass
    '''