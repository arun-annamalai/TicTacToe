from flask import render_template, Blueprint, session, redirect, url_for, request, current_app
from flask_socketio import emit, join_room, leave_room
from server.config import Config
from server.model import Games


route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
@route_blueprint.route('/login')
def login():
    return render_template('login.html')

@route_blueprint.route('/game_select', methods = ['GET', 'POST'])
def game_select():
    if request.method == "POST":
        print(request.form)
        session['game_room_id'] = request.form['game_room_id']
        return redirect(url_for('route_blueprint.game', game_room_id = session['game_room_id']))
    else:
        if 'game_room_id' not in session:
            return render_template('game_select.html', num_games=Config.NUM_GAMES)
        else:
            return redirect(url_for('route_blueprint.game', game_room_id = session['game_room_id']))

@route_blueprint.route('/game<string:game_room_id>', methods = ['GET', 'POST'])
def game(game_room_id=None):
    if request.method == "POST":
        session.pop('game_room_id', None)
        return redirect(url_for('route_blueprint.game_select'))
    else:
        game = Games.query.get(int(game_room_id))
        print(type(game_room_id))
        return render_template('game.html', game_state = game.game.pretty_print().replace("\n", " <br>"), game_room_id = game_room_id)

@route_blueprint.route('/logout')
def logout():
    return render_template('logout.html')