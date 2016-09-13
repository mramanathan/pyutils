# _*_ coding: utf-8 _*_

#!/usr/bin/env python


from random import randrange
from itertools import repeat

grid_marks = { 1: ["C1", "C2", "C3"],
               2: ["C4", "C5", "C6"],
               3: ["C7", "C8", "C9"]
             }



def validNum(input):
	try:
		stat = [True for x in range(1,10) if x == input]
		return stat[0]
	except IndexError:
		return False

# one more way to check validity of user input
#def valid(x):
#	if x == input:
#		return True

#for i in filter(valid, range(0,3)):
#	print("Got this: ", i)



def redrawGrid(cells_used):

	"""
	"""

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



def main():

	"""
	"""

	# help menu

	total_cells = 9
	cells_used = []

	# start fresh game
	if len(cells_used) == 0:
		print("=" * 2 + "Let's start a new game ... remember cells are numbered to help you\n")
		print("=" * 2 + "When game starts, C1, C3 markings will indicate empty cells\n)
		showGrid()

	user_choice = input("Enter a valid cell number [0-9]: ")
#	comp_choice = randrange(1,10,1)

	if len(cells_used) <= total_cells:

	if validNum(int(user_choice)):
		print("User's choice was : " + "C" + user_choice)
		cells_used.append("C" + user_choice)
		redrawGrid(cells_used)
	else:
		if validNum(int(user_choice)):
			print("User's choice was : " + "C" + user_choice)
			cells_used.append("C" + choice)



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
