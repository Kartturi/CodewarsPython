#challenge made by user578387
#A digital root is the recursive sum of all the digits in a number. 
# Given n, take the sum of the digits of n. If that value has more than 
# one digit, continue reducing in this way until a single-digit number is 
# produced. This is only applicable to the natural numbers.
#digital_root(16)
#=> 1 + 6
#=> 7

#own implementation
def digital_root(n):
    # ...
    strings = str(n)
    numArr = []
    newValue = 0
    for i in strings:
        numArr.append(int(i))
    for n in numArr:
        newValue += n
      
    if newValue < 10:
        return newValue
    else:
        return digital_root(newValue)

print(digital_root(942))