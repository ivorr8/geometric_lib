
def area(a):
    '''Принимает сторону квадрата и возращает его площадь'''
    if a == 0:
        return "erorr" 
    elif isinstance(a, int):
        return a * a
    else:
        return "erorr"


def perimeter(a):
    '''Принимает сторону квадрата и возращает его периметр'''
    if a == 0:
        return "erorr" 
    elif isinstance(a, int):
        return a * 4
    else:
        return "erorr"

