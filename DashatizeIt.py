
# Given a number, return a string with dash'-'marks before and after each 
# odd integer, but do not begin or end the string with a dash mark.

# Ex:

# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

def dashatize(num):
    newList = []
    build = ''

    if num is None:
        return 'None'
    for i,char in enumerate(str(num),start=0):
        if not char.isdigit():
            continue
        if int(char) % 2 == 0:
            build += char
            if i == len(str(num)) - 1:
                newList.append(build)
        else:
            if len(build) > 0:
                newList.append(build)
            build = ''
            newList.append(char)
    return '-'.join(newList)

print(dashatize(''))