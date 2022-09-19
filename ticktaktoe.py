import random

boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
HUMAN = 'X'
COMPUTER = '0'
first_player = HUMAN
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]


def print_board(initial=False):
    # Printing the game board.
    print(('''
{} | {} | {}
-------------
{} | {} | {}
-------------
{} | {} | {}
        ''').format(*boxes))


def take_turn(player, turn):
    # keeps asking the current player for their input until a valid choice is made.
    while True:
        if player is COMPUTER:
            box = get_computer_move()
        else:
            box = int(input('Player %s, type a number from 1-9 to select a box: ' % player))
            box = int(box) - 1  # subtract 1 to get same as boxes[] index numbers

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            continue

        if boxes[box] == ' ':  # initial value
            boxes[box] = player  # set to value of current player
            break
        else:
            print('That box is already marked, try again.\n')


def get_computer_move():
    return random.randint(0, 8)


def switch_player(turn):
    """ Switch the player based on how many moves have been made.
        X starts the game so if this turn # is even, it's 0's turn.
    """
    current_player = COMPUTER if turn % 2 == 0 else HUMAN
    return current_player


def check_for_win(player, turn):
    # check for win or tie
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'


def play(player, turn):
    # Create a loop that keeps the game in play until it ends in a win or tie

    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print('Game over. %s wins!\n' % player)
            break
        elif result == 'tie':
            print('Game over. It\'s a tie.\n')
            break
        turn += 1
        player = switch_player(turn)


# Begin the game:
print('\n\nWelcome to Tic Tac Toe Game for Player vs Computer')
print_board()
play(first_player, turn)