from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print( " ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  print("Turn", turn + 1)
  if guess_row == ship_row and guess_col == ship_row:
    print("Congratz! U capsized my battleship")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print("Wow dude!, that's not on the ocean.")
    elif (board[guess_row][guess_col] == 'X'):
        print("You guessed that one already.")
    else:
      print("Hell nah, try again")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print("Game Over")


