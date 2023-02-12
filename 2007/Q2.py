

# input 9 characters
debug = True

if debug:
    board = 'EOOOOXXXX'
    board = 'XXEXOOOXO'     # test 1
    board = 'EOOOOXXXX'     # test 2
    board = 'OEXXOOOXX'     # test 3
    board = 'EXXXXOOOO'     # test 4
    board = 'XEOXXXOOO'     # test 5
    #board = 'OOEXOOXXX'     # test 6 - fail
    #board = 'EXOXOXXOO'     # test 7

    board = board.upper()
else:
    input_string = input('Enter valid start posn (e.g. EOOOOXXXX)')
    board = input_string.upper()

# initial condition
player = 'O'
opponent = 'X'
MAX_TRIES = 99
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

def get_available_moves(board, player):
    '''returns a list of board results after move'''
    # only one empty space, so player must move into E
    putahi = board[0]
    kawai = board[1:]
    available_moves = []

    # if putahi is E, then move can be made from any posn except braced by own tiles
    if putahi == 'E':
        # find every instance of player and swap with putahi
        for i in range(8):
            if kawai[i] == player:
                #check that i is not between 2 player markers
                p_left = i -1
                p_right = i +1
                if p_right > 7: p_right = 0
                if not (kawai[p_left] == player and kawai[p_right] == player):
                    valid_move = player + kawai[:i] + 'E' + kawai[i+1:]
                    available_moves.append(valid_move)

                    #print('get_available_moves: putahi was E:',valid_move, len(valid_move))


    # if E is in kawai, then move can be made from posns next to E, and from puthai
    else:
        empty = kawai.find('E') # retuns -1 for no find; index posn otherwise
        # from the left...
        left = empty - 1
        if left < 0: left = 7   # not stricly necessary since index -1 == last char
        if empty > 0 and kawai[left] == player:
            valid_move = putahi + kawai[:left] + 'E' + player + kawai[empty+1:]
            available_moves.append(valid_move)

            #print('get_available_moves: left, empty > 0:',valid_move, len(valid_move))
        elif empty == 0 and kawai[left] == player:
            valid_move = putahi + player + kawai[empty+1:left] + 'E'
            available_moves.append(valid_move)

            #print('get_available_moves: left, empty = 0:',valid_move, len(valid_move))

        # from the right...
        right = empty + 1
        if right > 7: right = 0
        if empty < 7 and kawai[right] == player:
            valid_move = putahi + kawai[:empty] + player + 'E' + kawai[right+1:]
            available_moves.append(valid_move)

            #print('get_available_moves: right, empty > 0:',valid_move, len(valid_move))
        elif empty == 7 and kawai[right] == player:
            valid_move = putahi + 'E' + kawai[right+1:empty] + player
            available_moves.append(valid_move)

            #print('get_available_moves: right, empty = 0:',valid_move, len(valid_move))
        
        # from the centre...
        if putahi == player:
            valid_move = 'E' + kawai[:empty] + player + kawai[empty+1:]
            available_moves.append(valid_move)

            #print('get_available_moves: putahi is player:',valid_move, len(valid_move))
            
    return available_moves



######################main ###########################
print('initial board layout is ', board,'\n')


while count < MAX_TRIES:
    if check_win(board, player):
        break
    else: print(f'\nRound {count}: {player} has {board}')
    # player takes a turn


    options = get_available_moves(board, player)
    print(f'options for {player} are',options)
    if options:
        # keep scoore, and if current option > score then choose this option
        move_score = -1     # -1:lose, 0:draw, 1:win
        #3. If the previous rules do not indicate which move to take, move the leftmost of my markers.
        board = options[0]  # this is the default so we don't leave empty handed
        #1. If there is a move which means my opponent will then lose, this move is played. If several such moves exist,
        #choose the one that uses the leftmost of my markers.
        for try_move in options:
            if check_win(try_move, player) and move_score < 1:
                print(f'options: player {player} found a winner!! chose {try_move}')
                board = try_move
                move_score = 1
            elif move_score < 1:
                #2. If the first rule does not indicate which move to take and there are moves, after which my opponent will be
                #able to make a move meaning that I will then lose, those moves are to be avoided (by moving the leftmost of
                #my markers that avoids these moves). If it is not possible to avoid such a move, move the leftmost of my
                #markers.
                opp_options = get_available_moves(try_move, opponent)
                print(f'\toptions: {try_move} opponent options for {opponent} are',opp_options)
                for try_opp_move in opp_options:
                    if check_win(try_opp_move, opponent):
                        print(f'\t\tWATCH OUT!, {opponent} could win with {try_opp_move}')
                        break
                    if not check_win(try_opp_move, opponent) and move_score < 0:
                        print(f'\t\topp_options: {player} choosing drawing move {try_move} ')
                        board = try_move
                        move_score = 0
                    else:
                        print(f'\thow did we get here? {player} move {try_move}, opponent move {try_opp_move}, move score = {move_score}')

    player, opponent = swap_player(player)

    

    count += 1

    

if count < MAX_TRIES:
    print(f'\n{player} wins in {count} with board {board}\n')
else: print('Its a draw - try again')
