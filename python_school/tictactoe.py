
def tictactoe_to_string(board):
    # str_board = f"""
    #     +---+---+---+
    #     |   |
    #     +---+
    # """

    str_board = ""

    for y in range(len(board)):
        width = len(board[y])
        str_board += "+---+" * width
        str_board += "\n"

        for x in range(width):
            str_board += f"| {board[y][x]} |"

        str_board += "\n"
        str_board += "+---+" * width
        str_board += "\n"

    return str_board

def check_plays(plays):
    current_play = plays[0]

    if current_play == " ":
        return None
        
    i = 1
    while i < len(plays) and plays[i] == current_play:
        i += 1
        
    if i == len(plays):
        return current_play

def check_rows(board):

    for row in board:
        winner = check_plays(row)
        if winner is not None:
            return winner

    return None

def check_columns(board):
    height = len(board)
    width = len(board[0])

    for x in range(width):
        column = []
        for y in range(height):
            column.append(board[y][x])

        winner = check_plays(column)
        if winner is not None:
            return winner

def check_winner(board):

    winner = check_rows(board)

    if winner is None:
        winner = check_columns(board)
    
    return winner

def play_turn(board, player, pos):
    (pos_x, pos_y) = pos

    board[pos_y][pos_x] = player

# def check_diagonal(board):

def tictactoe_game():
    winner = None
    current_player = "O"
    board = [[" " for x in range(3)] for y in range(3) ]
    print(tictactoe_to_string(board))
    while winner is None:
        print(f"Player turn : {current_player}")
        x = input("Give x coordinate : ")
        y = input("Give y coordinate : ")

        play_pos = (int(x), int(y))
        play_turn(board, current_player, play_pos)

        print(tictactoe_to_string(board))

        winner = check_winner(board)

        if current_player == "O":
            current_player = "X"
        else:
            current_player = "O"
    
    print(f"The winner is : {winner}")


if __name__ == "__main__":
    print("Hello tic tac toe :D")

    tictactoe_game()
    # board = [
    #     ["O", " ", "O"],
    #     ["X", "X", "O"],
    #     ["X", "O", "O"]
    # ]

    # print(tictactoe_to_string(board))
    # print(check_rows(board))
    # print(check_columns(board))