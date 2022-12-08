import numpy as np

with open("./input.txt") as file:
    tree_heights = [[eval(height) for height in list(line.strip())] for line in file.readlines()]

best_scenic_score = 0
tree_grid = np.array(tree_heights)
print(tree_grid)

num_rows, num_cols = tree_grid.shape

for index, tree_height in np.ndenumerate(tree_grid):
    print(index, tree_height)
    row_num = index[0]
    col_num = index[1]

    row = tree_grid[row_num,:]
    col = tree_grid[:,col_num]

    left_score = 0
    for other_tree_height in np.flip(row[0:col_num]) :
        left_score += 1
        if (other_tree_height >= tree_height):
            break
    
    right_score = 0
    for other_tree_height in row[col_num+1:] :
        right_score += 1
        if (other_tree_height >= tree_height):
            break
    
    top_score = 0
    for other_tree_height in np.flip(col[0:row_num]) :
        top_score += 1
        if (other_tree_height >= tree_height):
            break

    down_score = 0
    for other_tree_height in col[row_num+1:] :
        down_score += 1
        if (other_tree_height >= tree_height):
            break

    curr_score = left_score * right_score * top_score * down_score
    best_scenic_score = max(curr_score, best_scenic_score)

print(best_scenic_score)