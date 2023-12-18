row1 = [7, 8, 9]
row2 = [4, 5, 6]
row3 = [1, 2, 3]

def display_board(row1, row2, row3):
	'''This function prints the three rows of a tic-tac-toe board. 
	
	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list'''

	print(*row1)
	print(*row2)
	print(*row3)

def prompt_user(row1, row2, row3):
	'''This function prompts the user for input and verifies it using a try-except block. 
	
	Checks if input is an integer and if it is still available on the board. 

	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list
	
	Returns
	-------
	integer
		user's input.'''

	while True:
		try:
			choice = int(input("Please choose a cell: "))
			# Checks if the input is an integer and if it is still available on the board.
			if choice in (row1 + row2 + row3):
				return choice 
			else: 
				raise ValueError
		except ValueError:
			print("Invalid input")

def check_diagonal(row1, row2, row3):
	'''Checks to see if there is a winning diagonal. 
	
	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list
	
	Returns
	-------
	boolean
		True if there is a winning diagonal, False otherwise.'''

	return ((row1[0] == row2[1] == row3[2]) or (row1[2] == row2[1] == row3[0]))

def check_columns(row1, row2, row3):
	'''Checks to see if there is a winning column.
	
	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list
	
	Returns
	-------
	boolean
		True if there is a winning column, False otherwise.'''

	index = 0

	while(index < len(row1)):
		if row1[index] == row2[index] == row3[index]:
			return True 
		else: 
			index += 1

	return False

def check_row(row1, row2, row3):
	'''Checks to see if there is a winning row.
	
	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list

	Returns
	-------
	boolean
		True if there is a winning row, False otherwise.'''

	return (len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1)

def check_board(row1, row2, row3):
	'''Checks if there is a winning diagonal, column, or row. 
	
	Parameters
	----------
	row1 : list
	row2 : list
	row3 : list
	
	Returns
	-------
	boolean
		True if there is a winning diagonal, column, or row. False otherwise.'''
	return check_diagonal(row1, row2, row3) or check_columns(row1, row2, row3) or check_row(row1, row2, row3)

def change_token(input, token):
	'''This function changes a cell in row1, row2, or row3 depending on the input
	number and the player's token (X or O)
	
	Parameters
	----------
	input - int
	token - string'''

	if input > 0 and input < 4:
		row3[input - 1] = token
	elif input > 3 and input < 7:
		row2[input - 4] = token
	else:
		row1[input - 7] = token

def play_round():
	'''This function plays a round of tic-tac-toe between two human players.'''
	print("Welcome to Tic-Tac-Toe!\nPlayer 1 will be 'X'\nPlayer 2 will be 'O'\n")

	turn = 0

	while turn < 10:
		if turn % 2 == 0:
			display_board(row1, row2, row3)
			print("\nPlayer 1, it is your turn")
			change_token(prompt_user(row1, row2, row3), 'X')

			if check_board(row1, row2, row3):
				print("Player 1 is the winner!")
				break
			
			turn += 1
		else:
			display_board(row1, row2, row3)
			print("\nPlayer 2, it is your turn")
			change_token(prompt_user(row1, row2, row3), 'O')

			if check_board(row1, row2, row3):
				print("Player 2 is the winner!")
				break
			
			turn += 1

play_round()