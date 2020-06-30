import random

EMPTY_SLOT = "-"
X_PLAYER = "X"
AI_PLAYER = "0"
TIE = "tie"

valid_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

WIN_COMBO = [
    # Complete row
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Complete column
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Complete diagonal
    [0, 4, 8],
    [2, 4, 6]
]


def initialize_board():
    board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
             EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
             EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
    return board


def display_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player, board):
    print(f"{player}, it's your turn.")

    if player == X_PLAYER:
        position = (input('Enter a position (1-9): '))
        while not valid_position(position, board):
            position = (input('Invalid position, enter a position (1-9): '))
        valid_positions.remove(int(position) - 1)

        board[int(position) - 1] = player

        print(valid_positions)

    elif player == AI_PLAYER:

        AI_Turn(player, board)
        # position = random.choice(valid_positions)
        # valid_positions.remove(position)
        # board[(position)-1] = player

    # valid_positions.remove(int(position))

    return board


def valid_position(position, board):
    if int(position) in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board[int(position) - 1] == EMPTY_SLOT:
        valid = True

    else:
        valid = False

    return valid


def switch_player(player):
    if player == X_PLAYER:
        player = AI_PLAYER

    elif player == AI_PLAYER:
        player = X_PLAYER

    return player


def check_for_winner(board):
    winner = None
    # filled_slots = 0

    # TODO Check if any of the players got a win combo
    # Hint: loop over WIN_COMBO to check if one of the combo is X-X-X or O-O-O
    for combo in WIN_COMBO:

        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != EMPTY_SLOT:

            winner = board[combo[0]]

        elif EMPTY_SLOT not in board:
            winner = TIE

    return winner


def AI_Turn(player, board):
    print('whats happening')
    position = None

    for combo in WIN_COMBO:
        # print (combo)
        # print (position)

        # 1st - 3rd if statements check if AI_PLAYER can win next move
        if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == EMPTY_SLOT:
            position = combo[2]
            print('1st if')
            print(position)

        elif board[combo[0]] == board[combo[2]] == player and board[combo[1]] == EMPTY_SLOT:
            position = combo[1]
            print('2nd if')
            print(position)

        elif board[combo[1]] == board[combo[2]] == player and board[combo[0]] == EMPTY_SLOT:
            position = combo[0]
            print('3rd if')
            print(position)

        # 4th - 6th if statements check if player can win next move and blocks
        elif board[combo[0]] == board[combo[1]] == X_PLAYER and board[combo[2]] == EMPTY_SLOT:
            position = combo[2]
            print('4th if')
            print(position)

        elif board[combo[0]] == board[combo[2]] == X_PLAYER and board[combo[1]] == EMPTY_SLOT:
            position = combo[1]
            print('5th if')
            print(position)

        elif board[combo[1]] == board[combo[2]] == X_PLAYER and board[combo[0]] == EMPTY_SLOT:
            position = combo[0]
            print('6th if')
            print(position)

    if not position:
        edges_move = []

        for i in [0, 2, 4, 6, 8]:  # The ForLoop checks if the corner and center positions are free.
            if i in valid_positions:
                # print (i)
                edges_move.append(i)  # Free slots are added to the empty list above
        print(edges_move)

        if len(edges_move) != 0:
            # checks if any of the centre and edges are available and picks one randomly
            position = random.choice(edges_move)
            print('edge centre called')

        else:
            # if non of conditions above are satisfied, any random position available is picked
            position = random.choice(valid_positions)
            print('random activated')

    print(position)
    valid_positions.remove(position)
    board[(position)] = player
    print(valid_positions)


def start_player():  # Tosses a coin to determine who starts game

    if random.choice([0, 1]) == 1:
        player = X_PLAYER
    else:
        player = AI_PLAYER

    return player


def tic_tac_toe():
    winner = None
    game_still_going = True
    player = start_player()  # selects who starts randomly

    print('WELCOME TO THE GAME OF TICTACTOE\n')
    # Initialize board
    board = initialize_board()

    # TODO run this while the game is still going
    while game_still_going:

        # Display board
        display_board(board)

        # Ask the player for a valid position and write it on the board
        board = handle_turn(player, board)

        player = switch_player(player)

        # Check if there is a winner already
        winner = check_for_winner(board)
        if winner == None:
            game_still_going = True
        else:
            game_still_going = False

    print("THE END")
    if winner == TIE:
        print("No winner, the game is a Tie")
    else:
        print(f"Congratulations player {winner}!! You won the game!")
    display_board(board)


# Start game
tic_tac_toe()
