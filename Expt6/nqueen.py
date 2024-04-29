def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

#index of the board array corresponds to a row, and the value at that index corresponds to the column where a queen is placed in that row.
def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions


n = int(input("Enter the number of queens: "))
solutions = solve_n_queens(n)

print(f"Total solutions for {n}-queens problem: {len(solutions)}")
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        line = ['. '] * n
        line[row] = 'Q '
        print(''.join(line))
    print()