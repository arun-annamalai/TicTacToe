from flask import render_template, Blueprint
from server import tictactoegame
from server import board

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
@route_blueprint.route('/login')
def login():
    return render_template('login.html')

@route_blueprint.route('/game')
def game():
    print(board.to_string())
    return render_template('game.html', game_state = board.to_string().replace("\n", " <br>"))

@route_blueprint.route('/logout')
def logout():
    return render_template('logout.html')