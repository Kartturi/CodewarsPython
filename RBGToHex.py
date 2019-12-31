def rgb(r, g, b):
    return f'{hexValueConverter(r)}{hexValueConverter(g)}{hexValueConverter(b)}'

def hexValueConverter(value):
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        
        temp = value / 16
        resList = str(temp).split('.')
        firstValue = 0
        secondValue = 0
        
        if len(resList) < 2:
            firstValue = int(resList[0])
        else:
            firstValue = int(resList[0])
            secondValue = int(float(f'0.{resList[1]}') * 16)
        #calculations
        return getHexValue(firstValue) + getHexValue(secondValue)

def getHexValue(value):
        param = value
        result = ''
        outerValues = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        if value >= 10:
            return str(outerValues[param])
        else:
            return str(param)


#improved version
def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

print(rgb2(255,144,124))