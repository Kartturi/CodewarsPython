#Made by BattleRattle
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. 
# We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is 
# secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘

# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be
#  another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also 
# be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never 
# finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

# Can you help us to find all those variations? It would be nice to have a function, that returns an array 
# (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could 
# name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed
#  one and also the results, must be strings, because of potentially leading '0's. We already prepared some 
# test cases for you.


# Detective, we count on you!

#from itertools import product

# ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

from itertools import combinations

def get_pins(observed):
    possibleNums = []
    for num in observed:
        possibleNums = possibleNums + findLockValues(int(num))
    
    joined = ''.join([str(x) for x in possibleNums])
    result = []
    for item in list(set(combinations(joined,len(observed)))):
        result.append(''.join(item))
    return result

    

def findLockValues(num):
    if num == 0:
        return [0,8]
    elif num == 8:
        return [7,8,9,5,0]

    lock = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    plan = {0: 'forward', 1:'both', 2:'back'}
    instructs = []
    
    
    for i,lis in enumerate(lock):
        if num in lis:
            instructs = [plan[i],plan[lis.index(num)]]
    
    return computeValues(instructs,num)


def computeValues(instructs,num):
    result = []
    result.append(num)
    if instructs[0] == 'forward':
        result.append(num + 3)
    elif instructs[0] == 'both':
        result.append(num + 3)
        result.append(num - 3)
    else:
        result.append(num - 3)
    
    if instructs[1] == 'forward':
        result.append(num + 1)
    elif instructs[1] == 'both':
        result.append(num + 1)
        result.append(num - 1)
    else:
        result.append(num - 1)

    return result




print(get_pins('8'))