with open("day6-data-test", 'r') as f:
    lines = f.read().strip().splitlines()
    grid = [list(line.strip()) for line in lines]

def find_marker(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '^':
                return (row, col)
    return None

def move_guard(grid, gp, gd, visited_tiles):
    visited_tiles.add(gp)
    # print(f"Position: {gp}, Direction: {gd}")
    
    # # Debug: Print what's ahead
    # try:
    #     next_cell = grid[gp[0] + gd[0]][gp[1] + gd[1]]
    #     print(f"Next cell: {next_cell}")
    # except IndexError:
    #     print("Would go out of bounds!")
    
    # headed off the board case
    if (gp[1] + gd[1] < 0 or gp[0] + gd[0] < 0 or 
        gp[1] + gd[1] >= len(grid[0]) or gp[0] + gd[0] >= len(grid)):
        return visited_tiles
        
    if grid[gp[0] + gd[0]][gp[1] + gd[1]] == '#':
        # print(f"Hit obstacle, turning right from {gd}")
        gd = (gd[1], -gd[0])
        # print(f"New direction: {gd}")
    
    gp = (gp[0] + gd[0], gp[1] + gd[1])
    return move_guard(grid, gp, gd, visited_tiles)

# we're assuming "^" here
print(len(move_guard(grid, find_marker(grid), (-1,0), set())))

# debug
for y, row in enumerate(grid):
    print(f"{y:2d} {''.join(row)}")
