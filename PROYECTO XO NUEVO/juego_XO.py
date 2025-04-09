# Tic-Tac-Toe (XO) en consola
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Revisar filas, columnas y diagonales
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


def main():
    print("=== Bienvenido a Tic-Tac-Toe (XO) ===")
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Jugador {current_player}, elige una casilla (1-9): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if move < 1 or move > 9:
            print("Movimiento fuera de rango. Intenta de nuevo.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("Esa casilla ya está ocupada. Elige otra.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Felicidades! El jugador {current_player} ha ganado.")
            break

        if is_draw(board):
            print_board(board)
            print("¡Empate!")
            break

        current_player = "O" if current_player == "X" else "X"

    print("Gracias por jugar :)")

if __name__ == "__main__":
    main()



