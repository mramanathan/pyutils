# _*_ coding: utf-8 _*_

## Tested with Python 3.5.x
#!/usr/bin/python3


from random import randrange
from itertools import repeat
#from time import sleep
#from os import system


# used to display the used and unused cells in the grid
grid_marks = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]

# used by whoWinner to determine which player won the game !
win_rows   = { 1: [0, 1, 2],
               2: [3, 4, 5],
               3: [6, 7, 8],
               4: [0, 3, 6],
               5: [1, 4, 7],
               6: [2, 5, 8],
               7: [0, 4, 8],
               8: [2, 4, 6]
             }

# cells in 3x3 matrix or grid
total_cells = 9

# Atleast 5 cells should be filled to determine a winner !
# Remember, numbering starts at index 0 !!!
mincells_chkwinner = 4

# Keep track of cells used by the players
cells_used = []



## replaced by inputstr.isdigit() ~> built-in string method
## preserved here to showcase list comprehension
#def validNum(input):
#	try:
#		stat = [True for x in range(1,10) if x == input]
#		return stat[0]
#	except IndexError:
#		return False

# one more way to check validity of user input
#def valid(x):
#	if x == input:
#		return True

#for i in filter(valid, range(0,3)):
#	print("Got this: ", i)



def redrawGrid():

	""" After every move by the player, it's

	good to show the latest status of the grid
	with used and empty cells.
	"""

	print("\n\n")
	row_delim = "=" * 20
	col_delim = "||"

	print("%~>" * 5 + " Used cells are : ", cells_used)

	base_inc = 3
	new_start = 0
	new_end = base_inc

	for i in range(1,5):
		print("\t" * 2 + row_delim + "\n")
		if i != 4:
			print("\t" * 2 + col_delim, end='')
			for j in range(new_start,new_end):
				print(" " + grid_marks[j] + " ", end=col_delim)
			new_start = new_start + base_inc
			new_end   = new_end + base_inc
			print("\n")

	return None



def showGrid(input=''):

	""" Initial display of the grid with some

	messages for the players to make their move.
	"""

	if input == "":
		print("\n\n")
		row_delim = "=" * 20
		col_delim = "||"
		num = 1
		cnine = repeat("C", 9)
		for i in range(1,5):
			print(row_delim + "\n")
			if i != 4:
				print(col_delim, end='')
				for j in range(1,4):
					print(" " + next(cnine) + str(num) + " ", end=col_delim)
					num += 1
				print("\n")

	return None



def userAPlay():

	""" Ask for input from user and update 'grid_marks' list,

	and update the status on console for next player
	to make his / her move.
	"""

	user_choice = input("\n" + "^^" * 5 + " User A: Enter a valid cell number [1-9]: ")
	user_choice.strip()
#	if validNum(int(user_choice)):
	if user_choice.isdigit():
		print("User's choice was : " + "C" + user_choice)
		cells_used.append("C" + user_choice)
		print("Cell, C" + user_choice + " is at index position in grid : ", end=' == ')
		print(grid_marks.index("C" + user_choice)+1, end=" ")
#		print("\n")
		grid_marks[grid_marks.index("C" + user_choice)] = "R"
		redrawGrid()
		print("Valid empty (marked as CX) cells available : ", grid_marks)
#		print("\n")
		if (len(cells_used) >= mincells_chkwinner):
			win_status = whoWinner()
			if win_status == "continue":
				print("@~!" * 5 + " Let us {} the game, no clear winner after {} moves".format(win_status, len(cells_used)) + " " + "@~!" * 5)
				userDPlay()
			elif win_status == "TIE":
				print("#$" * 5 + "Hey, it's a TIE, game over")
				print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
				exit(0)
			elif win_status == "WON":
				print("Got the winner, hurray. It is, ", win_status)
				print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
				exit(0)
		else:
			userDPlay()

	return None



def userDPlay():

	""" Ask for input from user and update 'grid_marks' list,

	and update the status on console for next player
	to make his / her move.
	"""

	user_choice = input("\n" + "^^" * 5 + " User D: Enter a valid cell number [1-9]: ")
	user_choice.strip()
#	if validNum(int(user_choice)):
	if user_choice.isdigit():
		print("User's choice was : " + "C" + user_choice)
		cells_used.append("C" + user_choice)
		print("Cell, C" + user_choice + " is at index position in grid : ", end=' == ')
		print(grid_marks.index("C" + user_choice)+1, end=" ")
#		print("\n")
		grid_marks[grid_marks.index("C" + user_choice)] = "D"
		redrawGrid()
		print("Valid empty (marked as CX) cells available : ", grid_marks)
#		print("\n")
		if (len(cells_used) >= mincells_chkwinner):
			win_status = whoWinner()
			if win_status == "continue":
				print("@~!" * 5 + " Let us {} the game, no clear winner after {} moves".format(win_status, len(cells_used)) + " " + "@~!" * 5)
				userAPlay()
			elif win_status == "TIE":
				print("#$" * 5 + "Hey, it's a TIE, game over")
				print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
				exit(0)
			elif win_status == "WON":
				print("Got the winner, hurray. It is, ", win_status)
				print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
				exit(0)
		else:
			userAPlay()

	return None



""" TODO: On hold until we find a solution for:
how shall we retain the numbers already used and feed 
that to random() such that when the turn of the 
computer arrives, different cells are chosen ? 
"""
def compPlay():

	"""
	"""

	print("++" * 5 + " Now it's the turn of the computer, allow R2D2 to think (ah,ah,ah) . . .\n")
	sleep(5)	
	comp_choice = randrange(1,10,1)
	if validNum(comp_choice):
		comp_choice = str(comp_choice)
		print("Computer's choice was : " + "C" + comp_choice)
		cells_used.append("C" + comp_choice)
		print("Cell, C", comp_choice + " is at index position in grid : ", end=' == ')
		print(grid_marks.index("C" + comp_choice)+1, end=" ")
#		print("\n")
		grid_marks[grid_marks.index("C" + comp_choice)] = "D"
#		print("\n")
#		redrawGrid()
		print("Valid empty (marked as CX) cells available : ", grid_marks)
#		whoWinner()

	return None



def whoWinner():

	""" Determine the winner or announce

	that game ended in TIE.
	This shall start after the 5th move
	in the grid.
	If there is a winner, return who is the
	winner, winning rows, flag to stop game.
	"""

	all_combos = []
	rows = []
	temp_set = set()

	base_inc = 3
	new_start = 0
	new_end = base_inc

	for combo in win_rows.keys():
#		print("checking combo : ", win_rows[combo])
		for cell_num in win_rows[combo]:
			all_combos.append(grid_marks[cell_num])

#	print("Complete dump : ", all_combos)
	# Match of the rows should be done for all 8 combination
	# of rows that can net the winner !!!
	for rpt in range(0, int( len(all_combos) / base_inc )):
#		print("==" * 5+ " Combo : ", rpt)
		rows = []
		for i in range(new_start, new_end):
#			print(all_combos[i], end=' ')
			rows.append(all_combos[i])
#		print("Evaluating {} for the winner".format(rows), end=' ')
		temp_set = set(rows)
		if len(temp_set) == 1:
			print("Got the winner in this combo : ", temp_set)
			winner = temp_set
			break
		else:
#			print(" No winner here, moving on to next set")
			new_start = new_start + base_inc
			new_end   = new_end   + base_inc
			winner = "TIE"
#			print("\n")

	# TO DO: if len of cell used < total cells and
	# status is not win, then continue
	# status is win, quit
	if len(cells_used) == total_cells or len(cells_used) != total_cells:
		if len(temp_set) == 1:
			winner = "WON"
			return winner

	if len(cells_used) == total_cells and len(temp_set) != 1:
		winner = "TIE"
		return winner

	if len(cells_used) != total_cells and len(temp_set) != 1:
		winner = "continue"
		return winner



def main():

	""" Simple Tic Tac Toe game that uses

	minimal built-in methods. Yeah, it's 
	kind of weird in many places.
	"""

	# help menu


	# start fresh game
	if len(cells_used) == 0:
		print("==" * 10 + "  Welcome to the game of Tic-Tac-Toe  " + "==" * 10 + "\n")
		print("=" * 5 + " Remember cells are numbered to help you\n")
		print("=" * 5 + " And, C1...C9 markings indicate empty cells")
		showGrid()


	print("$&" * 5 + " {} free cells available in the grid".format(total_cells-len(cells_used)))
	userAPlay()

	# TO DOs:
	# 1. Choice to replay the game.
	# 2. Enable compPlay()

	return None



if __name__ == "__main__":
	main()
