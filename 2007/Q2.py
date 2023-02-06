

# input 9 characters
debug = True

if debug:
    #board = 'EOOOOXXXX'
    #board = 'oeooxxxxo'    # O wins
    board = 'xxexooxxx'    # X wins
    board = board.upper()
else:
    input_string = input('Enter valid start posn (e.g. EOOOOXXXX)')
    board = input_string.upper()

# initial condition
player = 'O'
opponent = 'X'
MAX_TRIES = 19
count = 0

def swap_player(player):
    if player == 'O':
        return 'X', 'O'
    else: 
        return 'O', 'X'


def check_win(board, player):
    # to win player must occupy putahi (centre) and sequence P-E-P in kawai
    putahi = board[0]
    kawai = board[1:]
    pad_kawai = kawai[-1] + kawai + kawai[0]
    #check player occupies puthai and check for P-E-P sequence 
    # (find returns position of string, or -1 if not found)
    return (putahi == player) and (pad_kawai.find(player + 'E' + player) > -1)
    

######################main ###########################
print(f'initial board layout is ', board)


while count < MAX_TRIES:
    if check_win(board, player):
        break
    else: print(f'No winner: {player} has {board}')

    player, opponent = swap_player(player)
    count += 1

    # player takes a turn

if count < MAX_TRIES:
    print(f'{player} wins with board {board}')
else: print('Its a draw - try again')