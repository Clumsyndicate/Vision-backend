from flask import Flask, render_template
from flask_socketio import SocketIO
from config import app_config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'

app.config.from_pyfile('config.py', silent=True)
app.config.from_object(app_config['development'])
socketio = SocketIO(app)

db = SQLAlchemy()
db.init_app(app)


@socketio.on('new photo')
def handle_new_photo(data):
    pass


@app.route('/')
def index():
    return 'INDEX'


@app.route('/images/<int: index>')
def fetch_image(index):
    pass
