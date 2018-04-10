"""


*******************
*                 *
*                 *
*                 *
*                 *
*******************


"""

def boxPrint(symbol, width, heigth):
    print(symbol * width)

    for i in range(heigth - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
