# N Queens Problem using Backtracking

N = 4

# Print solution
def print_solution(board):

    for row in board:
        print(" ".join(row))

# Check safe position
def is_safe(board, row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col

    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

# Solve recursively
def solve_nq(board, col):

    # Base condition
    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):

            board[i][col] = 'Q'

            if solve_nq(board, col + 1):
                return True

            # Backtracking
            board[i][col] = '.'

    return False

# Main Program
board = [['.' for _ in range(N)] for _ in range(N)]

if solve_nq(board, 0):

    print("Solution Found:\n")

    print_solution(board)

else:
    print("No Solution Exists")
    