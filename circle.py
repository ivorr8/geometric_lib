import math


def area(r):
    '''Принимает радиус круга и возращает его площадь'''
    if r == 0:
        return "erorr" 
    elif isinstance(r, int):
        return math.pi * r * r
    else:
        return "erorr"
    


def perimeter(r):
    '''Принимает радиус круга и возращает его периметр'''
    if r == 0:
        return "erorr" 
    elif isinstance(r, int):
        return 2 * math.pi * r
    else:
        return "erorr"
    
    


