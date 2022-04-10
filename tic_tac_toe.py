Last login: Sun Apr  3 08:42:06 on ttys001
bharatraj@Kids-iMac ~ % cd tic_tac_toe 
bharatraj@Kids-iMac tic_tac_toe % ls
LICENSE			README.md		copy_tic_tac_toe.py	temp			tic_tac_toe.py
bharatraj@Kids-iMac tic_tac_toe % vi tic_tac_toe.py 







































































import random
from flask import Flask
from flask import request
import requests

app = Flask("server")

def invalid_check(slot):
        b = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        for i in b:
                if slot == i:
                        if board[slot] == ' ':
                                return(False)
        return(True)

def print_winner (winner):
        if winner == 'X':
                print('player X won')
        elif winner == 'O':
                print('player O won')

def is_game_over():
        checks = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
        for check in checks:
                if board[check[0]] == board[check[1]] and board[check[0]] == board[check[2]] and board[check[0]] != ' ':
                        print_winner(board[check[0]])
                        return(True)
                elif board['A1'] != ' ' and board['A2'] != ' ' and board['A3'] != ' ' and board['B1'] != ' ' and board['B2'] != ' ' and board['B3'] != ' ' and board['C1'] != ' ' and board['C2'] != ' ' and board['C3'] != ' ':
                        print("Draw")
                        return (True)
        return (False)

def run_server1():
        app.run()

def run_server2():
        print_board(board)
        slot_2 = input("Server, please enter a slot (A1, A2, A3...)")
        while invalid_check(slot_2) == (True):
                slot_2 = input("invalid move, please move again")
                if invalid_check(slot_2) == (False):
                        break
        if is_game_over() == (False):
                print_board(board)
                board[slot_2] = myMarker
                if is_game_over() == (True):
                        print_winner(myMarker)
                        return(True)
                dict2 = {"message": "move", "marker": myMarker, "position": slot_2}
                #url = "http://127.0.0.1:5000/command"
                #response2 = requests.post(url, dict2)
                #print(response2.text)
                return dict2
        else:
                isgameover=is_game_over()
@app.route('/')
def hello():
        return "Hello World Again!"

@app.route('/command', methods=['GET', 'POST'])
-- INSERT --
import random
from flask import Flask
from flask import request
import requests

app = Flask("server")

def invalid_check(slot):
	b = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
	for i in b:
		if slot == i:
			if board[slot] == ' ':
				return(False)
	return(True)    

def print_winner (winner):
	if winner == 'X':
		print('player X won')
	elif winner == 'O':
		print('player O won')

def is_game_over():
	checks = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
	for check in checks:
		if board[check[0]] == board[check[1]] and board[check[0]] == board[check[2]] and board[check[0]] != ' ':
			print_winner(board[check[0]])
			return(True)
		elif board['A1'] != ' ' and board['A2'] != ' ' and board['A3'] != ' ' and board['B1'] != ' ' and board['B2'] != ' ' and board['B3'] != ' ' and board['C1'] != ' ' and board['C2'] != ' ' and board['C3'] != ' ': 
			print("Draw")
			return (True)
	return (False)

def run_server1():
	app.run()

def run_server2():
	print_board(board)
	slot_2 = input("Server, please enter a slot (A1, A2, A3...)")
	while invalid_check(slot_2) == (True):
		slot_2 = input("invalid move, please move again")
		if invalid_check(slot_2) == (False):
			break
	if is_game_over() == (False):
		print_board(board)
		board[slot_2] = myMarker
		if is_game_over() == (True):
			print_winner(myMarker)
			return(True)
		dict2 = {"message": "move", "marker": myMarker, "position": slot_2}
		#url = "http://127.0.0.1:5000/command"
		#response2 = requests.post(url, dict2)
		#print(response2.text)
		return dict2
	else:
		isgameover=is_game_over()
@app.route('/')
def hello():
	return "Hello World Again!"

@app.route('/command', methods=['GET', 'POST'])
def command():
	global myMarker
	print(request.form)
	response_dict = request.form.to_dict()
	print(response_dict)
	slot_s = response_dict["position"]
	otherMarker=response_dict["marker"]
	if otherMarker == "X":
		myMarker = "O"
	else:
		myMarker = "X"
	if invalid_check(slot_s) == False:
		board[slot_s] = response_dict['marker']
		print_board(board)
		ok = slot_okay()
	if invalid_check(slot_s) == True:
		ok = slot_not_okay()
	response = run_server2()
	return response
	#okay = {"status": "ok"}
	#return okay

	
def slot_okay():
	okay = {"status": "ok"}
	return okay
def slot_not_okay():
	not_okay = {"status": "not ok"}
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

def print_board(board):
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
	arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	positions = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
	for array in arrays:
		if num == array:
			return positions[num1]
	return 'a'

def computer_move():
	n = random.randint(1,9)
	return(n)

def client_1(slot_1):
	for i in range(9):
		slot_1 = input("Client,  please enter a slot (A1, A2, A3...)")
		while invalid_check(slot_1) == (True):
			slot_1 = input("invalid move, please move again")
			if invalid_check(slot_1) == (False):
				break
		isgameover = is_game_over()
		if isgameover == (True):
			break
		if isgameover == (False):
			dict = {"message": "move", "marker": marker, "position": slot_1}
			url = "http://127.0.0.1:5000/command"
			response = requests.post(url, dict)
			print(response.text)
			dict = eval(response.text)
			board[slot_1] = marker
			print_board(board)
			slot_2 = dict["position"]
			board[slot_2] = dict["marker"]
			print_board(board)
			

player_choice = input("player vs. player (p), player vs. bot (b), bot vs. bot using client and server (bot), player vs. bot, when player is client (c), player vs. bot, when player is server (s), player vs. player, when player is client (pc), player vs. player when player is server (ps)")
if player_choice == "p":
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
elif player_choice == "b":
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
elif player_choice == "c":
	
	marker = input("Do you want to be X or O?")
	for i in range(3):
		slot_1 = input("Client,  please enter a slot (A1, A2, A3...)")
		while invalid_check(slot_1) == (True):
			slot_1 = input("invalid move, please move again")
			if invalid_check(slot_1) == (False):
				board[slot_1] = marker
				break
		board[slot_1] = marker 
		if is_game_over() == (False):
			dict = {"message": "move", "marker": marker, "position": slot_1}
			url = "http://127.0.0.1:5000/command"
			response = requests.post(url, dict)
			print(response.text)
			dict = eval(response.text)
			slot_2 = dict["position"]
			board[slot_2] = dict["marker"]
			print_board(board)
elif player_choice == "s":
	run_server1()
elif player_choice == "pc":
	marker = input("Do you want to be X or O?")
	slot_1 = input("Client, please enter a slot (A1, A2, A3...)")
	while invalid_check(slot_1)  == (True):
		slot_1 = input("invalid move, please move again")
		board[slot_1] = marker
		print_board(board)
		isgameover = is_game_over()
