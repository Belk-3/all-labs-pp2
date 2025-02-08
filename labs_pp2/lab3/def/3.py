# 3. Solve chickens and rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            print(f"Chickens: {chickens}, Rabbits: {rabbits}")
            return chickens, rabbits
    print("No solution found")
    return None
