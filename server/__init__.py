from flask import Flask
from flask_socketio import SocketIO
from server.config import Config

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.use_reloader = False
    app.config.from_object(Config)

    from server import route_logic
    app.register_blueprint(route_logic.route_blueprint)

    from server.model import init_db, db_session
    init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from server import socket_logic
    socketio.init_app(app)

    return app