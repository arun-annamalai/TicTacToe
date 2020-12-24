from flask import session
from flask_socketio import emit, join_room, leave_room, rooms
from . import socketio
from server.model import db_session, Games

@socketio.on('game_input')
def game_input(message):
    game = Games.query.get(session['game_room_id'])
    game.game.mark_board(message['row'] - 1, message['col'] - 1, message['mark'])
    db_session.commit()

    # Emit only to this room
    emit('game_change', {'data': game.game.pretty_print().replace("\n", " <br>")}, room = session['game_room_id'])

    if game.game.check_game_over()[0]:
        # Emit only to this room
        emit('show_winner', {'data': game.game.check_game_over()[1]}, room = session['game_room_id'])

    print(message)
    print(game.game.pretty_print())
    print(game.game.check_game_over())

@socketio.on('reset')
def reset():
    game = Games.query.get(session['game_room_id'])
    game.game.clear_board()
    db_session.commit()
    print("game room", session['game_room_id'])
    print("rooms", rooms())
    #Emit only to this room
    emit('game_change', {'data': game.game.pretty_print().replace("\n", " <br>")}, room = session['game_room_id'])
    emit('hide_winner', room = session['game_room_id'])
    pass

@socketio.on('join')
def join(message):
    print(type(message['game_room_id']))
    join_room(message['game_room_id'])
    print(rooms())


@socketio.on('leave')
def leave(message):
    leave_room(message['game_room_id'])
    print(rooms())

@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')