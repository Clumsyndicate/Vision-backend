from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'

app.config.from_pyfile('secrets/config.py', silent=True)
socketio = SocketIO(app)

@socketio.on('new photo')
def handle_new_photo(data):
    pass

if __name__ == "__main__":
    socketio.run(app)