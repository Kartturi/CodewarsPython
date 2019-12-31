# ROT13 is a simple letter substitution cipher that replaces a letter with the 
# letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13.
#  If there are numbers or special characters included in the string, they should be
#  returned as they are. Only letters from the latin/english alphabet should be shifted,
#  like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    #ascii numbers
    upper_begin = 65
    upper_end = 90
    lower_begin = 97
    lower_end = 122
    result = ''

    for char in message:
        ac = ord(char)
        #is alpabetic char
        if ac <= upper_end and ac >= upper_begin:
           result += getNewChar(upper_begin,upper_end,ac,13)
        elif ac <= lower_end and ac >= lower_begin:
            result += getNewChar(lower_begin,lower_end,ac,13)
        else:
            result += char 

    print(type('result'))
    return result

def getNewChar(low, top, curr, amount):
    desired = curr + amount
    if desired <= top:
        return chr(desired)
    else:
        return chr(desired - top + low - 1)

print(rot13('Test'))