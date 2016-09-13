# _*_ coding: utf-8 _*_

#!/usr/bin/env python

from itertools import repeat

# one more way to check validity of user input
#def valid(x):
#	if x == input:
#		return True

#for i in filter(valid, range(0,3)):
#	print("Got this: ", i)

def validNum(input):
	try:
		stat = [True for x in range(1,10) if x == input]
		return stat[0]
	except IndexError:
		return False


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
	# Invoke showgrid
	showGrid()
	cells_used = []
	# collect user input
	choice = input("Enter a valid cell number [0-9]: ")
	if len(cells_used) == 0:
		if validNum(int(choice)):
			print("User's choice was : " + "C" + choice)
			cell_used.append("C" + choice)
		else:
			choice = input("Enter a valid cell number [0-9]: ")
	else:


	# validate input -- available numbers
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
