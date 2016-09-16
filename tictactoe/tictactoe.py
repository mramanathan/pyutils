# _*_ coding: utf-8 _*_

## Tested with Python 3.5.x
#!/usr/bin/env python


from random import randrange
from itertools import repeat
from time import sleep
from os import system


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
mincells_chkwinner = 5

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

	"""
	"""

	print("\n\n")
	row_delim = "=" * 20
	col_delim = "||"
#	for g in uxip:
#	    usedcell = "C" + str(g)
#	    print("Cell, ", usedcell + " is at index position in grid marks : ", end=' == ')
#	    print(grid_marks.index(usedcell), end=" ")
#	    grid_marks[grid_marks.index(usedcell)] = "X"

#	num = 1
#	for i in range(1,5):
#		print(row_delim + "\n")
#		if i != 4:
#			print(col_delim, end='')
#			for j in range(1,4):
#				print(" " + next(cnine) + str(num) + " ", end=col_delim)
#				num += 1
#			print("\n")

	print("%~>" * 5 + "Used cells are : ", cells_used)

	return None



def showGrid(input=''):

	"""
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

	"""
	"""

	user_choice = input("^^" * 5 + " User A: Enter a valid cell number [1-9]: ")
	user_choice.strip()
#	if validNum(int(user_choice)):
	if user_choice.isdigit():
		print("User's choice was : " + "C" + user_choice)
		cells_used.append("C" + user_choice)
		print("Cell, C" + user_choice + " is at index position in grid : ", end=' == ')
		print(grid_marks.index("C" + user_choice)+1, end=" ")
		print("\n")
		grid_marks[grid_marks.index("C" + user_choice)] = "R"
		print("Valid empty (marked as CX) cells available : ", grid_marks)
		redrawGrid()
		print("\n")
#		winnerStatus()

	return None



def userDPlay():

	"""
	"""

	user_choice = input("^^" * 5 + " User D: Enter a valid cell number [1-9]: ")
	user_choice.strip()
#	if validNum(int(user_choice)):
	if user_choice.isdigit():
		print("User's choice was : " + "C" + user_choice)
		cells_used.append("C" + user_choice)
		print("Cell, C" + user_choice + " is at index position in grid : ", end=' == ')
		print(grid_marks.index("C" + user_choice)+1, end=" ")
		print("\n")
		grid_marks[grid_marks.index("C" + user_choice)] = "D"
		print("Valid empty (marked as CX) cells available : ", grid_marks)
		redrawGrid()
		print("\n")
#		winnerStatus()

	return None



""" On hold until we find a solution for:
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
		print("\n")
		grid_marks[grid_marks.index("C" + comp_choice)] = "D"
		print("Valid empty (marked as CX) cells available : ", grid_marks)
		print("\n")
#		redrawGrid()
#		winnerStatus()

	return None



def whoWinner():

	"""

	"""

	winset = set()

	for combo in win_rows.keys():
		print("checking combo : ", win_rows[combo])
		for cell_num in win_rows[combo]:
			winset.add(grid_marks[cell_num])
		print("Got this set : ", winset)
		# set returns the unique element from ['R', 'R', 'R']
		if len(winset) == 1:
			game_over = True
			print("Got the winner.")
			break
		else:
			game_over = False
			winset = set()
			print("No winner yet!")

	if game_over == True:
		return (game_over, winset, win_rows[combo])
	else:
		return False,0,0



def main():

	"""
	"""

	# help menu


	# start fresh game
	if len(cells_used) == 0:
		print("==" * 10 + "  Welcome to the game of Tic-Tac-Toe  " + "==" * 10 + "\n")
		print("=" * 5 + " Remember cells are numbered to help you\n")
		print("=" * 5 + " And, C1...C9 markings indicate empty cells")
		showGrid()


	while (total_cells-len(cells_used) != 0):
		if len(cells_used) >= mincells_chkwinner:
			(game_over, userset, usercells) = whoWinner()
			if game_over == True:
				print("Got the winner, hurray. It is, ", userset)
				print("And, it's in the cell combo: ", usercells)
				print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
				exit(0)
#			else:
#				continue
		else:
			print("$&" * 5 + " {} free cells available in the grid".format(total_cells-len(cells_used)))
			userAPlay()
			if len(cells_used) == total_cells:
				(game_over, userset, usercells) = whoWinner()
				if game_over == True:
					print("Got the winner, hurray. It is, ", userset)
					print("And, it's in the cell combo: ", usercells)
					print("/\\/\\" * 5 + " Game over buddies!!!! " + "/\\/\\" * 5 + "\n\n")
					exit(0)
				else:
					print("#$" * 5 + "Hey, it's a TIE, game over")
					exit(0)
			else:
				print("$&" * 5 + " {} free cells available in the grid".format(total_cells-len(cells_used)))
				userDPlay()
#		compPlay()

	# Based on valid input, fill the grid
	# show the updated grid and prompt the
	# next user to play
	# if the number of moves by any user
	# equals 3, then check valid arrangement
	# of cells and determine if there are any
	# winners.

	return None



if __name__ == "__main__":
	main()
