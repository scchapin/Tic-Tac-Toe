# This is a simple Tic Tac Toe game that uses just the console and basic python scripting

# Global variables for the Tic Tac Toe game
player1 = ''
player2 = ''
game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
win_conditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7,]]


# main Program all functions run in this
def run_program():
    global game_board
    print('Lets play Tic Tac Toe!')
    print('Make moves by selecting the correct number from your ten key pad')
    print('moves are mapped in the following oder')
    game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board()
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    play = True
    get_player()
    while play:
        play = play_game()

    print('Thanks for Playing!')


# Clear the screen
def clear_board():
    print('\n' * 100)


# Get player order
def get_player():
    global player1
    global player2

    # Get player
    while player1 != 'X' and player1 != 'O':
        player1 = input("Please pick a marker 'X' or 'O'")
        player1 = player1.upper()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print("Player 1 is " + player1)
    print("Player 2 is " + player2)


# Get player 1 move and display
def get_player1_move():
    global game_board
    move = 0
    valid_move = True
    while move < 1 or move > 9 and valid_move:
        move = int(input("Player "+player1+" please input your move 1-9"))
        if game_board[move] == ' ':
            valid_move = True
        else:
            valid_move = False
            move = 0
            print('That was an invalid move, please try again')
    # Make move
    game_board[move] = player1
    clear_board()
    display_board()


# Get player 2 move and display
def get_player2_move():
    global game_board
    move = 0
    valid_move = True
    while move < 1 or move > 9 and valid_move:
        move = int(input("Player "+player2+" please input your move 1-9"))
        print(game_board[move])
        if game_board[move] == ' ':
            valid_move = True
        else:
            valid_move = False
            move = 0
            print('That was an invalid move, please try again')
    # Make move
    game_board[move] = player2
    clear_board()
    display_board()


# Display the game board
def display_board():
    print('   |   |   ')
    print(' {} | {} | {} '.format(game_board[7],game_board[8],game_board[9]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(game_board[4],game_board[5],game_board[6]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(game_board[1],game_board[2],game_board[3]))
    print('   |   |   ')


# Play tic tac toe!
def play_game():
    # Default values
    winner = False
    play_again = ''
    tie = False
    # Get player moves and check for a winner
    while not winner:
        get_player1_move()
        winner = check_score()
        if winner:
            print(player1 + ' is the winner!')
            break
        else:
            tie = check_for_tie()
            if tie:
                print("No moves left! It's a tie!")
                winner = True
                break
            get_player2_move()
            winner = check_score()
            if winner:
                print(player2 + ' is the winner!')
                break
            else:
                tie = check_for_tie()
                if tie:
                    print("No moves left! It's a tie!")
                    winner = True
                    break

    # If a winner is found check to see if they want to play again
    while play_again != 'Y' and play_again != 'N' and winner:
        play_again = input("Do you want to play again? Y/N")
        play_again = play_again.upper()
        # Break out and finish the app
        if play_again == 'N':
            global game_board
            return False
        # Keep playing but refresh the board
        if play_again == 'Y':
            global game_board
            game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            return True

    # Keep returning true to keep getting new moves
    return True


# Check for a tie
def check_for_tie():
    tie = True
    global game_board
    for score in game_board:
        if score == ' ':
            tie = False
    return tie


# Check the boards moves for a winner
def check_score():
    x = 0
    more_moves = False
    winner = False
    tie = False
    player1moves = []
    player2moves = []

    for move in game_board:
        if move == player1:
            player1moves.append(x)
        if move == player2:
            player2moves.append(x)

        if move == ' ':
            more_moves = True

        x += 1

        player2moves.sort()
        player1moves.sort()

    winner = check_winner(player1moves)
    if winner:
        return True

    winner = check_winner(player2moves)
    if winner:
        return True

    return winner


# Search for a winning set of moves
def check_winner(player_moves):
    winner = False
    move_hit = 0
    for win_set in win_conditions:
        for move in win_set:
            for player_move in player_moves:
                if player_move == move:
                    move_hit += 1
        if move_hit == 3:
            winner = True
            break
        else:
            move_hit = 0

    return winner


# Run the program
run_program()
