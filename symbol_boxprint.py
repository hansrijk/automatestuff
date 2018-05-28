"""


*******************
*                 *
*                 *
*                 *
*                 *
*******************


"""

def boxPrint(symbol, width, heigth):
    
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a str of length 1.')
    if (width <2) or (heigth <2):
        raise Exception('"width" and "length" must be equal to or greater than 2')

    
    print(symbol * width)

    for i in range(heigth - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('X', 5, 25)
