# _*_ coding: utf-8 _*_

## Tested with Python 3.5.x
#!/usr/bin/env python

from collections import OrderedDict


# used to display the used and unused cells in the grid
#grid_marks = ['D', 'D', 'R', 'R', 'R', 'D', 'R', 'D', 'R']
grid_marks = ['D', 'D', 'R', 'R', 'R', 'C6', 'D', 'C8', 'C9']

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

all_combos = []

base_inc = 3
new_start = 0
new_end = base_inc

rows = []
temp_set = set()

for combo in win_rows.keys():
	print("checking combo : ", win_rows[combo])
	for cell_num in win_rows[combo]:
		all_combos.append(grid_marks[cell_num])

print("Complete dump : ", all_combos)
for rpt in range(0, int( len(all_combos) / base_inc )):
	print("==" * 5+ " Combo : ", rpt)
	rows = []
	for i in range(new_start, new_end):
#		print(all_combos[i], end=' ')
		rows.append(all_combos[i])
	print("Evaluating {} for the winner".format(rows), end=' ')
	temp_set = set(rows)
	if len(temp_set) == 1:
		print("Got the winner in this combo : ", temp_set)
		winner = temp_set
		break
	else:
		print(" No winner here, moving on to next set")
		new_start = new_start + base_inc
		new_end   = new_end   + base_inc
		winner = "TIE"
		print("\n")

if winner == "TIE":
	print("Game ended in a TIE")
else:
	print("Winner of the game is : ", winner)
