# Manage the MySQL Database for image storage

from flask import Flask
from flaskr import db


class Image(db.Model):
    '''Image Object for sqlalchemy
    id: Integer
    image: LONGBLOB
    timestamp: TIMESTAMP
    lat: Float
    lng: Float
    '''

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary(length=(2**32)-1), nullable=True)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return '<Image {}>'.format(id)

