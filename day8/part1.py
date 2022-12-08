import numpy as np

with open("./input.txt") as file:
    tree_heights = [[eval(height) for height in list(line.strip())] for line in file.readlines()]

num_visible_trees = 0
tree_grid = np.array(tree_heights)
print(tree_grid)

num_rows, num_cols = tree_grid.shape

for index, tree_height in np.ndenumerate(tree_grid):
    print(index, tree_height)
    row_num = index[0]
    col_num = index[1]

    row = tree_grid[row_num,:]
    col = tree_grid[:,col_num]

    # outer tree?
    if (row_num in [0,num_rows-1] or col_num in [0,num_cols-1]) :
        num_visible_trees += 1
    else :
        # visible from the left?
        if (max(row[0:col_num]) < tree_height) :
            num_visible_trees += 1
        # visible from the right?
        elif (max(row[col_num+1:]) < tree_height) :
            num_visible_trees += 1
        # visible from the top?
        elif (max(col[0:row_num]) < tree_height) :
            num_visible_trees += 1
        # visible from the bottom?
        elif (max(col[row_num+1:]) < tree_height) :
            num_visible_trees += 1

print(num_visible_trees)