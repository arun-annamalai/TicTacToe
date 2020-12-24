#!/bin/env python
from server import create_app, socketio
from server.model import Base, db_session, Games, engine
from server.config import Config
from server.tictactoegame import TicTacToe
import numpy as np

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        server_restart = True
        if server_restart:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            for idx in range(Config.NUM_GAMES):
                g = Games(game = TicTacToe())
                db_session.add(g)
            db_session.commit()
        else:
            Base.metadata.create_all(engine)

    socketio.run(app, use_reloader=False)