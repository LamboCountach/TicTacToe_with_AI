import math

tictactoe_board = [['-', '-', '-'],
                   ['-', '-', '-'],
                   ['-', '-', '-']]



def placeX(board, x_coordinate, y_coordinate):
    board[x_coordinate][y_coordinate] = 'X'
    return board


def placeO(board, x_coordinate, y_coordinate):
    board[x_coordinate][y_coordinate] = 'O'
    return board



def is_full(board):
    full = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                full = False
                break
        if not full:
            break
    return full



def check_winning(board):
    result = -1
    if is_full(board):
        result = 0
    for i in range(3):
        if board[0][i] != '-' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == 'O':
                result = 1
                break
            else:
                result = 2
                break

    for j in range(3):
        if board[j][0] != '-' and board[j][0] == board[j][1] and board[j][0] == board[j][2]:
            if board[j][0] == 'O':
                result = 1
                break
            else:
                result = 2
                break

    if board[0][0] != '-' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            result = 1

        else:
            result = 2

    if board[0][2] != '-' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            result = 1

        else:
            result = 2


    return result



def match(board):
    start = True
    total_move = 0
    while True:
        if start:
            print("The game starts!")
            start = False
        print("Now it's player X's turn")
        x_proper_place = False
        while not x_proper_place:
            x1 = int(input("Enter your x coordinate: "))
            y1 = int(input("enter your y coordinate: "))
            if x1 > 2 or x1 < 0 or y1 > 2 or y1 < 0:
                print('Please enter an integer between 0 and 2 for x and y coordinate respectively')
            elif board[x1][y1] == '-':
                print(placeX(board, x1, y1))
                total_move += 1
                x_proper_place = True
            else:
                print("This grid is not empty! Please enter another x,y coordinate!")
        if check_winning(board) == 2:
            print('Player X wins')
            break
        elif total_move == 9:
            print("It's a tie game")
            break
        else:
            print("Now it's player O's turn")
            o_proper_place = False
            while not o_proper_place:
                x2 = int(input("Enter your x coordinate: "))
                y2 = int(input("enter your y coordinate: "))
                if x2 > 2 or x2 < 0 or y2 > 2 or y2 < 0:
                    print('Please enter an integer between 0 and 2 for x and y coordinate respectively')
                elif board[x2][y2] == '-':
                    print(placeO(board, x2, y2))
                    total_move += 1
                    o_proper_place = True
                else:
                    print("This grid is not empty! Please enter another x,y coordinate!")
            if check_winning(board) == 1:
                print('Player O wins')
                break





def is_terminal(board):
    return check_winning(board) == 0 or check_winning(board) == 1 or check_winning(board) == 2



# Consider our AI plays X
def minimax(ai_turn, board):
    if is_terminal(board):
        if check_winning(board) == 2:
            return 1
        elif check_winning(board) == 1:
            return -1
        else:
            return 0

    else:

        scores = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    if ai_turn:
                        placeX(board,i,j)
                    else:
                        placeO(board,i,j)
                    scores.append(minimax(not ai_turn, board))
                    board[i][j] = '-'

        return max(scores) if ai_turn else min(scores)



def generate(board):
    best_score = -math.inf
    bestMove_x = None
    bestMove_y = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                placeX(board,i,j)
                score = minimax(False,board)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    bestMove_x = i
                    bestMove_y = j
    return (bestMove_x,bestMove_y)

match(tictactoe_board)


def match_with_ai(board):
    start = True
    total_move = 0
    while True:
        if start:
            print("The game starts!")
            start = False
        print("Now it's player X's turn")
        (best_move_x, best_move_y) = generate(board)
        print(placeX(board, best_move_x, best_move_y))
        if check_winning(board) == 2:
            print('AI wins')
            break
        elif is_terminal(board):
            print("Draw game")
            break

        print("Now it's player O's turn")
        o_proper_place = False
        while not o_proper_place:
            x2 = int(input("Enter your x coordinate: "))
            y2 = int(input("enter your y coordinate: "))
            if x2 > 2 or x2 < 0 or y2 > 2 or y2 < 0:
                print('Please enter an integer between 0 and 2 for x and y coordinate respectively')
            elif board[x2][y2] == '-':
                print(placeO(board, x2, y2))
                total_move += 1
                o_proper_place = True
            else:
                print("This grid is not empty! Please enter another x,y coordinate!")
        if check_winning(board) == 1:
                print('Player O wins')
                break
        elif is_terminal(board):
            print("Draw game")
            break
