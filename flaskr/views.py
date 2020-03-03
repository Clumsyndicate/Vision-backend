from flaskr import app, socketio
from flaskr.db import *

@socketio.on('new photo')
def handle_new_photo(data):
    '''Image Object for sqlalchemy
    id: Integer
    image: LONGBLOB
    timestamp: TIMESTAMP
    lat: Float
    lng: Float
    '''
    # Notify that new images arrived
    print("{} images arrived".format(len(data.images)))

    socketio.emit('update', data, namespace='/client-update') 

@app.route('/')
def index():
    return 'INDEX'

@app.route('/images/<int: index>')
def fetch_image(index):
    pass