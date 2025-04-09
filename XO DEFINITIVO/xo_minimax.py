import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = str(i * 3 + j + 1)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = str(i * 3 + j + 1)
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = str(i * 3 + j + 1)
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    print("=== Tic-Tac-Toe (Jugador vs Máquina Invencible) ===")
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    human = "X"
    computer = "O"
    turn = "X"

    while True:
        print_board(board)

        if turn == human:
            try:
                move = int(input("Tu turno (1-9): "))
            except ValueError:
                print("Por favor ingresa un número válido.")
                continue

            if move < 1 or move > 9:
                print("Movimiento fuera de rango.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ['X', 'O']:
                print("Esa casilla ya está ocupada.")
                continue

            board[row][col] = human
        else:
            print("Turno de la máquina...")
            row, col = best_move(board)
            board[row][col] = computer

        if check_winner(board, turn):
            print_board(board)
            if turn == human:
                print("¡Ganaste! ¿Eres humano o una IA? 😮")
            else:
                print("La máquina ha ganado. ¡No puedes ganarle!")
            break

        if is_draw(board):
            print_board(board)
            print("¡Empate!")
            break

        turn = computer if turn == human else human

    print("Gracias por jugar.")

if __name__ == "__main__":
    main()
