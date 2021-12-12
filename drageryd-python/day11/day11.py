import sys

data = sys.stdin.read().strip()
sdata = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

grid = {x+y*1j: int(i)
        for y, row in enumerate(data.split("\n"))
        for x, i in enumerate(row)}

size = len(data.split("\n")[0]) + len(data.split("\n")) * 1j

def pretty_print(grid):
    for y in range(int(size.imag)):
        for x in range(int(size.real)):
            print(grid[x+y*1j], end="")
        print("")

adjacent = [1+1j, 1, 1-1j, 1j, -1j, -1+1j, -1, -1-1j]
flashes = 0
#pretty_print(grid)
i = 0
while True:
    i += 1
    # Add all by 1
    for p in grid:
        grid[p] += 1
    # Now there are no 0s
    flashing = [k for k,v in grid.items() if v > 9]
    while flashing:
        # Some seem to have gone over 9
        # Flash them and increment neighbors
        for k in flashing:
            flashes += 1
            # Add its adjecent tiles
            for a in adjacent:
                if k + a in grid and grid[k + a] != 0:
                    grid[k + a] += 1
            # Reset this to 0
            grid[k] = 0
            flashing = [k for k,v in grid.items() if v > 9]
    # Part 1
    if i == 100:
        print(flashes)
        #break
    # Part 2
    if not [1 for v in grid.values() if v != 0]:
        print(i)
        break
    
