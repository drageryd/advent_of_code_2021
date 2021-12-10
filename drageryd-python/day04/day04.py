import sys

i = sys.stdin.read().strip()
q = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# Strip double spaces and split boards
i = i.replace("  ", " ").split("\n\n")
#print(i)
draws = i[0].split(",")
boards = [[{x+y*1j:{"n":n, "m":False} for y,row in enumerate(b.split("\n")) for x,n in enumerate(row.strip().split(" "))},False] for b in i[1:]]

for d in draws:
    for i,bb in enumerate(boards):
        if bb[1]:
            continue

        # Mark board
        for xy, v in bb[0].items():
            if v["n"] == d:
                v["m"] = True
                break
        # Check if bingo
        if not bb[1]:
            for x in range(5):
                for y in range(5):
                    if not bb[0][x+y*1j]["m"]:
                        break
                else:
                    #Bingo on row
                    bb[1] = True
                    break
        if not bb[1]:
            for y in range(5):
                for x in range(5):
                    if not bb[0][x+y*1j]["m"]:
                        break
                else:
                    #Bingo on column
                    bb[1] = True
                    break
        if bb[1]:
            print("Bingo on board {}".format(i))
            print(int(d))
            s = sum(int(v["n"]) for xy,v in bb[0].items() if not v["m"])
            print(s)
            print(int(d) * s)
