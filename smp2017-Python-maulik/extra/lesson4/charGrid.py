grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

"""
Print the following pattern using above list of list:
   ..OO.OO..
   .OOOOOOO.
   .OOOOOOO.
   ..OOOOO..
   ...OOO...
   ....O....
"""

for i in range(len(grid[0])):
    for j in range(len(grid)) :                  
        print(grid[j][i],end="")
    print("")
