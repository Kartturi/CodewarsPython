#challenge made by wink
# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
# IPs should be considered valid if they consist of four octets, with values between
#  0 and 255, inclusive.

# Input to the function is guaranteed to be a single string.

# Examples
# Valid inputs:

# 1.2.3.4
# 123.45.67.89
# Invalid inputs:

# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Note that leading zeros (e.g. 01.02.03.04) are considered invalid.


def is_valid_IP(strng):
    splitted = strng.split('.')
    isValid = True
    if len(splitted) != 4:
        return False
    for item in splitted:
        try:
            if int(item2) < 0 or int(item2) > 256:
                isValid = False
            if len(item2) > 0 and item2[0] == '0':
                isValid = False
        except:
            isValid = False
    return isValid 

def is_valid_id2(str):
    splitted = str.split('.')
    passed = 0
    for item in splitted:
        if item.isdigit()
            if item[0] != '0'
                if 0 < int(item) <= 255 
                    passed += 1
    return passed == 4


print(is_valid_IP('123.45.67.89'))
print(is_valid_IP('123.456.78.90'))
print(is_valid_IP('123.045.067.089'))