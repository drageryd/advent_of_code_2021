import sys

fish = [int(x) for x in sys.stdin.read().strip().split(",")]

def simulate(fish, days):
    fish = list(fish)
    for day in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
    return len(fish)

test = [int(x) for x in "3,4,3,1,2".split(",")]

print(simulate(test, 18))
print(simulate(test, 80))
print(simulate(fish, 80))


def simulate(fish, days):
    # One fish reproduces every 7 days
    # So the every day there will be a certain number of fish born
    born = [0] * days
    # Generate fish born from initial population
    for f in fish:
        for d in range(days):
            if (d - f) % 7 == 0:
                born[d] += 1
    # The initial fish will not be counted by main loop
    count = len(fish)
    # Every day there are x fish born that will spawn new fish
    for day in range(days):
        # Fish born today
        b = born[day]
        #print("Day", day, ",", b, "fish born")
        # Add to main count
        count += b
        # Calculate when these fish will produce fish
        for d in range(day + 3, days):
            if (d - day - 2) % 7 == 0:
                # There are b fish today
                born[d] += b
    return count
    
print(simulate(test, 18))
print(simulate(test, 80))
print(simulate(fish, 80))
print(simulate(test, 256))
print(simulate(fish, 256))
