import random
def invalid_check(slot):
  b = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
  for i in b:
    if slot == i:
      if board[slot] == ' ':
        return(False)
  return(True)    

def print_winner (winner):
  if winner == 'x':
    print('player ' + player_1 + ', ' + 'sorry, you lost.')
  elif winner == 'o':
    print('player ' + player_1 + ', ' + 'great job! You won!')

def is_game_over():
  checks = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
  for check in checks:
    if board[check[0]] == board[check[1]] == board[check[2]] != ' ':
      print_winner(board[check[0]])
      return(True)
    else:  
      if board['A1'] != ' ' and board['A2'] != ' ' and board['A3'] != ' ' and board['B1'] != ' ' and board['B2'] != ' ' and board['B3'] != ' ' and board['C1'] != ' ' and board['C2'] != ' ' and board['C3'] != ' ': 
        print("Draw")
        return (True)
  return (False)
  
def stop_opponent_win():
  positions = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']]
  for position in positions:
    if board[position[0]] == board[position[1]] == 'o':
      if board[position[2]] == ' ':
        return position[2]
    elif board[position[1]] == board[position[2]] == 'o':
      if board[position[0]] == ' ':
        return position[0]
    elif board[position[0]] == board[position[2]] == 'o':
      if board[position[1]] == ' ':
        return position[1]
  return ' ' 
      
def get_computer_win():
  positions = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']]
  for position in positions:
    if board[position[0]] == board[position[1]] == 'x':
      if board[position[2]] == ' ':
        return position[2]
    elif board[position[1]] == board[position[2]] == 'x':
      if board[position[0]] == ' ':
        return position[0]
    elif board[position[0]] == board[position[2]] == 'x':
      if board[position[1]] == ' ':
        return position[1]
  return ' '    

def print_board(b):
  print('')
  print('    1 2 3')
  print('')
  print('A  ' + '|' + board['A1'] + '|' + board['A2'] + '|' + board['A3'] + '|')
  print('   -------')
  print('B  ' + '|' + board['B1'] + '|' + board['B2'] + '|' + board['B3'] + '|')
  print('   -------')
  print('C  ' + '|' + board['C1'] + '|' + board['C2'] + '|' + board['C3'] + '|')
  print('')

board = {}
board['A1'] = ' '
board['B1'] = ' '
board['C1'] = ' '
board['A2'] = ' '
board['B2'] = ' '
board['C2'] = ' '
board['A3'] = ' '
board['B3'] = ' '
board['C3'] = ' '

def numbers(num):
  #create array
  arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  positions = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
  for array in arrays:
    if num == array:
      return positions[num-1]
  return 'a'

def computer_move():
  n = random.randint(1,9)
  return(n)

player_choice = input("do you want to play against another player or computer?")

if player_choice == "player":
  player_1 = input("Player x, please enter your name")
  player_2 = input("Player o, please enter your name")
  print_board(board)
  choice = 1
  for i in range(9):
    if choice == 1:
      slot_1 = input("Player " + player_1 + ", please enter a slot (A1, A2, A3...)")
      while invalid_check(slot_1) == (True):
        slot_1 = input("invalid move, please move again")
      board[slot_1] = 'x'
      print_board(board)
      choice = 2
    else:
      slot_2 = input("Player " + player_2 + ", please enter a slot")
      while invalid_check(slot_2) == (True):
        slot_2 = input("invalid move, please move again")
      board[slot_2] = 'o'
      print_board(board)
      choice = 1  
    isgameover = is_game_over()
    if isgameover == (True):
      break
elif player_choice == 'computer':
  player_1 = input("Player y, please enter your name")
  choice = 1
  for i in range(9):
    if choice == 1:
      slot_2 = get_computer_win()
      if slot_2 == ' ':
        slot_2 = stop_opponent_win()
        if slot_2 == ' ':
          n = computer_move()
          slot = numbers(n)
          if board['B2'] == ' ':
            board['B2'] = 'x'
          elif board[slot] == 'a':
            board[slot] = 'x'
          else:
            while board[slot] != ' ':
              num1 = computer_move()
              slot = numbers(num1)
              if board[slot] == ' ':
                board[slot] = 'x'
                break
        else:
          board[slot_2] = 'x'
      else:
        board[slot_2] = 'x'
      print_board(board)
      choice = 2
    else: 
      slot_1 = input("Player " + player_1 + ", please enter a slot (A1, A2, A3...)")
      if invalid_check(slot_1) == (True):
        slot_1 = input("invalid move, please move again")
        board[slot_1] = 'o'
      board[slot_1] = 'o'
      print_board(board)
      choice = 1
    isgameover = is_game_over()
    if isgameover == (True):
      break