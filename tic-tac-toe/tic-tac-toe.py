def display_board(row1, row2, row3):
	print(row1)
	print(row2)
	print(row3)

def prompt_user():
	while True:
		try:
			choice = int(input("Please choose a cell: "))
			if choice in range(0,9): 
				return choice 
			else: 
				raise ValueError
		except ValueError:
			print("Invalid input")
		
print(prompt_user())