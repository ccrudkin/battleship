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

def check_guess(row, col):
  counter = 0
  for entry in range(3):
    if row == ship_loc_row[entry] and col == ship_loc_col[entry]:
      counter += 1
  return counter

def hit_checker():
  counter = 0
  for entry in range(3):
    if board[ship_loc_row[entry]][ship_loc_col[entry]] == "#":
      counter += 1
  return counter

ship_loc_row = {}
ship_loc_col = {}

if orientation == 0:
  ship_loc_row[0] = rand_row(board)
  ship_loc_row[1] = ship_loc_row[0]
  ship_loc_row[2] = ship_loc_row[1]
  ship_loc_col[0] = rand_col(board)
  ship_loc_col[1] = ship_loc_col[0] + 1
  ship_loc_col[2] = ship_loc_col[1] + 1
elif orientation == 1:
  ship_loc_row[0] = rand_row(board)
  ship_loc_row[1] = ship_loc_row[0] + 1
  ship_loc_row[2] = ship_loc_row[1] + 1
  ship_loc_col[0] = rand_col(board)
  ship_loc_col[1] = ship_loc_col[0]
  ship_loc_col[2] = ship_loc_col[1]
  
#print("Ship location (row, column): {}, {}; {}, {}".format(ship_row_1, ship_col_1, ship_row_2, ship_col_2))

#for debugging / cheating:
#for entry in range(3):
  #board[ship_loc_row[entry]][ship_loc_col[entry]] = "B"
#print("Orientation: {}".format(orientation))

print_board(board)

for turn in range(0, 4):
  print("Turn: ", turn + 1)

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  for entry in range(3):
    if check_guess(guess_row, guess_col) == 1:
      print("HIT!")
      board[guess_row][guess_col] = "#"
      if hit_checker() == 3:
        print("You sank the ship! You win!")
        break
      break
    else:
      if guess_row not in range(5) or guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
        break
      elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "#"):
        print("Sorry, you already guessed that spot.")
        break
      else:
        print("MISS!")
        board[guess_row][guess_col] = "X"
        break
  if hit_checker() == 3:
    print_board(board)
    break
  elif turn == 3:
    print("Game over. Where was the ship?")
    print()
    for entry in range(3):
      if board[ship_loc_row[entry]][ship_loc_col[entry]] != "#":
        board[ship_loc_row[entry]][ship_loc_col[entry]] = "B"
    print_board(board)
    break
  print_board(board)
  print()
