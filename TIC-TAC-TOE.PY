board = [" " for i in range(9)]
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
def check_winner(player):
    win_conditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
print("===================================")
print("      TIC TAC TOE GAME")
print("===================================")
for turn in range(9):
    print_board()
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    move = int(input(f"Player {player}, choose position (0-8): "))
    if board[move] == " ":
        board[move] = player
    else:
        print("Position already taken!")
        continue

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
else:
    print_board()
    print("It's a Draw!")
