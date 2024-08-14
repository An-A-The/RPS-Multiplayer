import socketio
import eventlet
from random import choice

sio = socketio.Server()
app = socketio.WSGIApp(sio)
players_choices = {}
@sio.event
def connect(sid, environ):
    print(f'Player {sid} connected')
    players_choices[sid] = None

@sio.event
def disconnect(sid):
    print(f'Player {sid} disconnected')
    if sid in players_choices:
        del players_choices[sid]

@sio.event
def player_choice(sid, data):
    print(f'Player {sid} chose {data}')
    players_choices[sid] = data

    if len(players_choices) == 2 and None not in players_choices.values():
        resolve_game()

def resolve_game():
    sids = list(players_choices.keys())
    p1, p2 = sids[0], sids[1]
    p1_choice, p2_choice = players_choices[p1], players_choices[p2]

    result = determine_winner(p1_choice, p2_choice)

    sio.emit('game_result', {'result': result, 'choices': {p1: p1_choice, p2: p2_choice}})

    players_choices[p1] = None
    players_choices[p2] = None

def determine_winner(choice1, choice2):
    outcomes = {
        ('rock', 'scissors'): 'rock',
        ('scissors', 'paper'): 'scissors',
        ('paper', 'rock'): 'paper',
    }

    if choice1 == choice2:
        return 'draw'
    return outcomes.get((choice1, choice2), outcomes.get((choice2, choice1), ''))

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
