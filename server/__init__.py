from flask import Flask
from flask_socketio import SocketIO
from server import tictactoegame

socketio = SocketIO()
board = tictactoegame.tttgame()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from server import route_logic
    app.register_blueprint(route_logic.route_blueprint)

    from server import socket_logic
    socketio.init_app(app)

    return app