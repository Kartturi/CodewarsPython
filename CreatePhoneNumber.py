# Write a function that accepts an array of 10 integers (between 0 and 9), 
# 7that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!


def create_phone_number(n):
    #your code here
    num = 0
    init = []
    middle = []
    rest =[]
    while num < len(n):
        if num < 3:
            init.append(str(n[num]))
        elif num < 6:
            middle.append(str(n[num]))
        else:
            rest.append(str(n[num]))
        num += 1
    str1 = "".join(init)
    str2 = "".join(middle)
    str3 = "".join(rest)
    return "({}) {}-{}".format(str1,str2,str3)

    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))