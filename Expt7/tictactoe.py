import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return 10
        elif row.count("O") == 3:
            return -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return 10
            elif board[0][col] == "O":
                return -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 10
        elif board[0][0] == "O":
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 10
        elif board[0][2] == "O":
            return -10

    # If no one wins
    return 0

#check if any move left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def minimax(board, depth, is_max):
    score = evaluate(board)

    # If maximizer wins
    if score == 10:
        return score - depth

    # If minimizer wins
    if score == -10:
        return score + depth

    # If there are no moves left and no one wins
    if not is_moves_left(board):
        return 0

    # If it's the maximizer's move
    if is_max:
        best = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best
    else:
        best = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -sys.maxsize
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if player == "X":
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = player
        else:
            print("Computer's move:")
            row, col = find_best_move(board)
            board[row][col] = player

        print_board(board)
        result = evaluate(board)
        if result == 10:
            print("X wins!")
            break
        elif result == -10:
            print("O wins!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

play_game()
