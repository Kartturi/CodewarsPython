def reverseString(str):
    reversed = ''
    for char in str:
        reversed = char + reversed
    return reversed


print(reverseString('abcd'))
