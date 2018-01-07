from random import randint

board = []
for each in range(0,5):
  board.append(["O"] * 5)

orientation = randint(0, 1)

def print_board(board_in):
  for row in board:
    print(" ".join(row))

def rand_row(board_in):
  if orientation == 0:
    return randint(0, len(board_in) - 1)
  elif orientation == 1:
    return randint(0, len(board_in) - 3)

def rand_col(board_in):
  if orientation == 0:
    return randint(0, len(board_in[0]) - 3)
  elif orientation == 1:
    return randint(0, len(board_in[0]) - 1)

if orientation == 0:
  ship_row_1 = rand_row(board)
  ship_row_2 = ship_row_1
  ship_row_3 = ship_row_2
  ship_col_1 = rand_col(board)
  ship_col_2 = ship_col_1 + 1
  ship_col_3 = ship_col_2 + 1
elif orientation == 1:
  ship_row_1 = rand_row(board)
  ship_row_2 = ship_row_1 + 1
  ship_row_3 = ship_row_2 + 1
  ship_col_1 = rand_col(board)
  ship_col_2 = ship_col_1
  ship_col_3 = ship_col_2
  
#print("Ship location (row, column): {}, {}; {}, {}".format(ship_row_1, ship_col_1, ship_row_2, ship_col_2))
#board[ship_row_1][ship_col_1] = "B"
#board[ship_row_2][ship_col_2] = "B"
#board[ship_row_3][ship_col_3] = "B"
#print("Orientation: {}".format(orientation))
print_board(board)

for turn in range(0, 4):
  print("Turn: ", turn + 1)

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row_3 and guess_col == ship_col_3):
    print("HIT!")
    board[guess_row][guess_col] = "#"
    if board[ship_row_1][ship_col_1] == "#" and board[ship_row_2][ship_col_2] == "#" and board[ship_row_3][ship_col_3] == "#":
      print("You sank the ship! You win!")
      print_board(board)
      break
    print_board(board)
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "#"):
      print("Sorry, you already guessed that spot.")
    else:
      print("MISS!")
      board[guess_row][guess_col] = "X"
    print_board(board)
  if turn == 3:
    print("Game over. Where was the ship?")
    print()
    if board[ship_row_1][ship_col_1] != "#":
      board[ship_row_1][ship_col_1] = "B"
    if board[ship_row_2][ship_col_2] != "#":
      board[ship_row_2][ship_col_2] = "B"
    if board[ship_row_3][ship_col_3] != "#":
      board[ship_row_3][ship_col_3] = "B"
    print_board(board)
  print()
