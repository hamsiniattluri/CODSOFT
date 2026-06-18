def print_board(board):
    display = []

    for i in range(9):
        if board[i] == ' ':
            display.append(str(i))
        else:
            display.append(board[i])

    print()
    print(f"{display[0]} | {display[1]} | {display[2]}")
    print("---------")
    print(f"{display[3]} | {display[4]} | {display[5]}")
    print("---------")
    print(f"{display[6]} | {display[7]} | {display[8]}")
    print()


def check_winner(board, player):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False


def is_draw(board):
    return ' ' not in board


def available_moves(board):
    return [i for i in range(9) if board[i] == ' ']


def minimax(board, ai, human, is_maximizing):

    if check_winner(board, ai):
        return 1

    if check_winner(board, human):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -1000

        for move in available_moves(board):
            board[move] = ai

            score = minimax(board, ai, human, False)

            board[move] = ' '

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = 1000

        for move in available_moves(board):
            board[move] = human

            score = minimax(board, ai, human, True)

            board[move] = ' '

            best_score = min(best_score, score)

        return best_score


def ai_move(board, ai, human):

    best_score = -1000
    best_move = None

    for move in available_moves(board):

        board[move] = ai

        score = minimax(board, ai, human, False)

        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = ai


def human_move(board, human):

    while True:

        try:
            move = int(input(f"Enter position (0-8) for {human}: "))

            if move < 0 or move > 8:
                print("Please enter a number between 0 and 8.")
                continue

            if board[move] != ' ':
                print("Position already occupied.")
                continue

            board[move] = human
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():

    board = [' '] * 9

    print("\n===== TIC-TAC-TOE AI =====\n")

    while True:
        human = input("Choose your symbol (X/O): ").upper()

        if human in ['X', 'O']:
            break

        print("Please choose X or O.")

    ai = 'O' if human == 'X' else 'X'

    while True:
        first = input("Who plays first? (human/ai): ").lower()

        if first in ['human', 'ai']:
            break

        print("Please enter 'human' or 'ai'.")

    print(f"\nYou are: {human}")
    print(f"AI is : {ai}")

    print("\nBoard Positions:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")

    current_player = first

    while True:

        print_board(board)

        if current_player == "human":

            human_move(board, human)

            if check_winner(board, human):
                print_board(board)
                print("🎉 Congratulations! You Win!")
                return "Human"

            current_player = "ai"

        else:

            print("🤖 AI is thinking...")

            ai_move(board, ai, human)

            if check_winner(board, ai):
                print_board(board)
                print("🤖 AI Wins!")
                return "AI"

            current_player = "human"

        if is_draw(board):
            print_board(board)
            print("🤝 It's a Draw!")
            return "Draw"


def main():

    human_score = 0
    ai_score = 0
    draws = 0

    while True:

        result = play_game()

        if result == "Human":
            human_score += 1

        elif result == "AI":
            ai_score += 1

        else:
            draws += 1

        print("\n========== SCOREBOARD ==========")
        print(f"Human Wins : {human_score}")
        print(f"AI Wins    : {ai_score}")
        print(f"Draws      : {draws}")
        print("================================")

        choice = input("\nPlay Again? (y/n): ").lower()

        if choice != 'y':
            print("\nThank you for playing Tic-Tac-Toe AI!")
            break


if __name__ == "__main__":
    main()