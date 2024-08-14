import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to the server')

@sio.event
def disconnect():
    print('Disconnected from the server')

@sio.event
def game_result(data):
    print('Game result:', data)
    result = data['result']
    if result == 'draw':
        print('It\'s a draw!')
    else:
        print(f'Winner: {result}')

def send_choice():
    choice = input('Enter your choice (rock/paper/scissors): ').strip().lower()
    sio.emit('player_choice', choice)

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    while True:
        send_choice()
