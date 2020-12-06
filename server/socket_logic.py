from flask_socketio import emit
from server.route_logic import board
from . import socketio

@socketio.on('game_input')
def game_input(message):
    board.mark_board(message['row'] - 1, message['col'] - 1, message['mark'])
    emit('game_change', {'data': board.to_string().replace("\n", " <br>")}, broadcast=True)

    if board.check_game_over()[0]:
        emit('show_winner', {'data': board.check_game_over()[1]}, broadcast=True)

    print(message)
    print(board.to_string())
    print(board.check_game_over())

@socketio.on('reset')
def reset():
    board.clear_board()
    emit('game_change', {'data': board.to_string().replace("\n", " <br>")}, broadcast=True)
    emit('hide_winner', broadcast=True)
    pass

@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')