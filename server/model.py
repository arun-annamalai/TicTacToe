import numpy as np
from sqlalchemy import create_engine, Column, Integer, PickleType
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from server.config import Config
from server.tictactoegame import TicTacToe

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    game = Column(TicTacToe.as_mutable(PickleType), nullable=False, unique=False)

    def __repr__(self):
        return f'<Game {self.id}>\n{self.game.pretty_print()}'

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)

