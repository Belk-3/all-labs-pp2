# 5. Print all permutations of a string
from itertools import permutations
def print_permutations(string):
    perms = [''.join(perm) for perm in permutations(string)]
    print("Permutations:", perms)
    return perms
