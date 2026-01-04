import math

HUMAN = 1
AI = -1
EMPTY = 0

pos_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

def new_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

board = new_board()

def print_board(b):
    symbols = {HUMAN: "O", AI: "X", EMPTY: "."}
    for row in b:
        print(" ".join(symbols[cell] for cell in row))
    print()

def available_moves(b):
    return [(r, c) for r in range(3) for c in range(3) if b[r][c] == EMPTY]

def check_winner(b, p):
    for i in range(3):
        if all(b[i][j] == p for j in range(3)):
            return True
        if all(b[j][i] == p for j in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)):
        return True
    if all(b[i][2 - i] == p for i in range(3)):
        return True
    return False

def is_full(b):
    return not any(EMPTY in row for row in b)

def minimax(b, turn):
    if check_winner(b, AI):
        return 1
    if check_winner(b, HUMAN):
        return -1
    if is_full(b):
        return 0

    if turn == AI:
        best = -math.inf
        for r, c in available_moves(b):
            b[r][c] = AI
            best = max(best, minimax(b, HUMAN))
            b[r][c] = EMPTY
        return best
    else:
        best = math.inf
        for r, c in available_moves(b):
            b[r][c] = HUMAN
            best = min(best, minimax(b, AI))
            b[r][c] = EMPTY
        return best

def best_move(b):
    best_score = -math.inf
    move = None
    for r, c in available_moves(b):
        b[r][c] = AI
        score = minimax(b, HUMAN)
        b[r][c] = EMPTY
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def play():
    global board
    board = new_board()

    print("\nImpossible Tic-Tac-Toe")
    print("You are O | AI is X")
    print("Choose positions 1–9 as:")
    print("1 2 3\n4 5 6\n7 8 9\n")

    while True:
        print_board(board)

        try:
            move = int(input("Your move (1-9): "))
        except:
            print("Invalid input.")
            continue

        if move not in pos_map:
            print("Choose a number between 1 and 9.")
            continue

        r, c = pos_map[move]
        if board[r][c] != EMPTY:
            print("That position is taken.")
            continue

        board[r][c] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("You won? That should not happen.")
            break

        if is_full(board):
            print_board(board)
            print("Draw. Anyway only Jha can beat his algorithm.")
            break

        r, c = best_move(board)
        board[r][c] = AI

        if check_winner(board, AI):
            print_board(board)
            print("Hehe… no matter how brainy you are,")
            print("you can’t beat the framework Jha made.")
            break

        if is_full(board):
            print_board(board)
            print("Draw. You survived.")
            break

    if input("\nPlay again? (y/n): ").lower() == "y":
        play()

play()
