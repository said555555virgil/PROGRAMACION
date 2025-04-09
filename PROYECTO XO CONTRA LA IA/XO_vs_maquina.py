import random

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
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                empty.append((i, j))
    return empty


def computer_move(board):
    # IA básica: busca ganar o bloquear al jugador
    for player in ['O', 'X']:
        for row, col in get_empty_cells(board):
            board_copy = [r[:] for r in board]
            board_copy[row][col] = player
            if check_winner(board_copy, player):
                return row, col

    # Si no hay jugada ganadora o bloqueo, elige al azar
    return random.choice(get_empty_cells(board))


def main():
    print("=== Tic-Tac-Toe (Jugador vs Máquina) ===")
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    human = "X"
    computer = "O"

    turn = "X"  # X empieza

    while True:
        print_board(board)

        if turn == human:
            try:
                move = int(input("Tu turno (1-9): "))
            except ValueError:
                print("Entrada no válida.")
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
            row, col = computer_move(board)
            board[row][col] = computer

        # Verificar ganador
        if check_winner(board, turn):
            print_board(board)
            if turn == human:
                print("¡Felicidades, ganaste!")
            else:
                print("La máquina ha ganado. ¡Suerte la próxima!")
            break

        if is_draw(board):
            print_board(board)
            print("¡Empate!")
            break

        # Cambiar turno
        turn = computer if turn == human else human

    print("Gracias por jugar.")


if __name__ == "__main__":
    main()
