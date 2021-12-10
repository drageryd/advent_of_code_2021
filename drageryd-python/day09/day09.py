import  sys

data = sys.stdin.read()
adata = """2199943210
3987894921
9856789892
8767896789
9899965678"""

heightmap = {x+y*1j:int(v) for y,row in enumerate(data.split("\n")) for x,v in enumerate(row)}

adjacent = (1, -1, 1j, -1j)
basins = []
s = 0
for coordinate, height in heightmap.items():
    for a in adjacent:
        # If any of the adjacent is lower the coordinate is not a low point
        h = heightmap.get(coordinate + a)
        if h is not None and height >= h:
            break
    else:
        # If for loop does not break the coordinate is a low point
        #print(coordinate, height)
        basins.append([set([coordinate]), set()])
        s += height + 1
print(s)

# Mark all != 9 fields as "basin"
for coordinate in heightmap:
    if heightmap[coordinate] == 9:
        heightmap[coordinate] = False
    else:
        heightmap[coordinate] = True

basins = []
basin_coordinates = set(c for c,b in heightmap.items() if b)
while basin_coordinates:
    # Get a coordinate
    basin = set()
    queue = [basin_coordinates.pop()]
    while queue:
        c = queue.pop()
        # add c to basin
        basin.add(c)
        queue += [c + a for a in adjacent if c + a in basin_coordinates]
        basin_coordinates.difference_update(queue)
    basins.append(basin)

#for b in basins:
#    print(b)

basins.sort(key=lambda x: len(x))

# Get length of top three
a = basins.pop()
b = basins.pop()
c = basins.pop()
print(a, len(a))
print(b, len(b))
print(c, len(c))

print(len(a) * len(b) * len(c))

"""
# All basins consist of a pair of unexplored coordinates and known points in the basin
for unexplored, known in basins:
    # Loop through unexplored coordinates and check if yet unexplored points are higher
    while unexplored:
        coordinate = unexplored.pop()
        height = heightmap[coordinate]
        #print(coordinate)
        al = [coordinate + a for a in adjacent if coordinate + a not in known]
        hl = [heightmap[a] > height for a in al if a in heightmap]
        # if hl exist and all heights are higher
        if hl and hl.count(False) == 0:
            # All surounding points are higher
            # Add c to known
            known.add(coordinate)
            # Add adjacent to unexplored
            unexplored.update([coordinate + a for a in adjacent if coordinate + a in heightmap and coordinate + a not in known])

basins.sort(key=lambda x: len(x[1]))

p = [[heightmap[x+y*1j] for x,v in enumerate(row)] for y,row in enumerate(data.split("\n"))]
#for b in basins:
#    for c in b[1]:
#        p[int(c.imag)][int(c.real)] = "x"
for row in p:
    print("".join(row))

# Get length of top three
a = basins.pop()[1]
b = basins.pop()[1]
c = basins.pop()[1]
#print(a, len(a))
#print(b, len(b))
#print(c, len(c))

print(len(a) * len(b) * len(c))
"""
