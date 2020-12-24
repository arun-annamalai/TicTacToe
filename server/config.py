import os

class Config(object):
    SECRET_KEY = 'secret!'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'game.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    NUM_GAMES = 5