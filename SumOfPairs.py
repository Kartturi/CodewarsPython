# Sum of Pairs

# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]


def sum_pairs(ints, s):
    pairs = {}
    possibleResults = []
    lowest = None
    for i,num in enumerate(ints):
        soughtNum = s - num
        if soughtNum in pairs:
            possibleResults.append([pairs[soughtNum], i])
        else:
            pairs[num] = i
    if len(possibleResults) == 0:
        return None
    for res in possibleResults:
        if lowest == None:
            lowest = res
        elif res[1] < lowest[1]:
            lowest = res
        
    return [ints[lowest[0]], ints[lowest[1]]]

def sum_pairs2(ints,s):
    exist = set()
    for num in ints:
        if s - num in exist:
            return [s-num,num]
        exist.add(num)

    		
    		

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l2, -6))