import math

'''
    Module--level test:
        >>> add(4,2)
        6.0
        >>> divide(10,2)
        5.0
'''
def add(a, b):
    '''Compute and return the addition between a and b
    Usage examples:
    >>> add(4.0,2.0)
    6.0
    >>> add(0.0,0.0)
    0.0
    >>> add(0.0,0.0)
    0
    >>> add(-1.2,0.0)
    -1.2
    >>> add(-1.2,-1.8)
    -3.0
    '''
    return a + b

def divide(a, b):
    '''Compute and return the division between a and b 
    Usage examples:
    >>> divide(10,2)
    5.0
    >>> divide(20,-2)
    -10.0
    >>> divide(10,1)
    10.0
    >>> divide(1.2,1)
    1.2
    >>> divide(1,0)
    Traceback (most recent call last):
        ...
    ValueError: El argumento divisor debe ser diferente de 0.
    '''
    if (b==0):
        raise ValueError("El argumento divisor debe ser diferente de 0.")
    
    return a / b

def product(a, b):
    '''Compute and return the product between a and b 
    Usage examples:
    >>> product(10,2)
    20
    >>> product(5,0)
    0
    >>> product(5.25,2.352)
    12.348
    >>> product(5,1.0)
    5.0
    >>> product(999999999999*9999999999)
    9999999998990000000001
    '''
    return a*b

def remainder(a, b):
    '''Compute and return the remainder between a and b 
    Usage examples:
    >>> remainder(10,2)
    0
    >>> remainder(5,2)
    1
    >>> remainder(5,0)
    Traceback (most recent call last):
        ...
    ValueError: El argumento divisor debe ser diferente de 0.
    >>> remainder(5.0,2.0)
    1.0
    >>> remainder(15,2.2)
    1.8
    '''
    if (b==0):
        raise ValueError("El argumento divisor debe ser diferente de 0.")
    return a % b

def sin(a):
    
    '''Compute and return the sin of a, with a as an angle 
    Usage examples:
    >>> sin(45)
    0.7071
    >>> sin(0)
    0.0
    >>> sin(90)
    1.0
    >>> sin(180)
    0.0
    >>> sin(360)
    0.0
    >>> sin(135)
    0.7071
    '''
    angle_radians = math.radians(a)
    return math.sin(angle_radians)

def cos(a):
    
    '''Compute and return the cos of a, with a as an angle
    Usage examples:
    >>> cos(90)
    0.0
    >>> cos(0)
    1
    >>> cos(180)
    -1.0
    >>> cos(360)
    1.0
    >>> cos(135)
    -0.7071
    '''
    angle_radians = math.radians(a)
    return math.cos(angle_radians)


def tan(a):
    
    '''Compute and return the tan of a, with a as an angle
    Usage examples:
    >>> tan(45)
    0
    >>> tan(0)
    0
    >>> cos(180)
    -1.0
    >>> cos(360)
    1.0
    >>> cos(135)
    -0.7071
    '''
    angle_radians = math.radians(a)
    
    return math.tan(angle_radians)

    
def greatestCommonDivisor(a, b):
    '''Compute and return the greatest common divisor between a and b
    Usage examples:
    >>> greatestCommonDivisor(2,20)
    2
    >>> greatestCommonDivisor(10,20)
    10
    >>> greatestCommonDivisor(3,6)
    3
    >>> greatestCommonDivisor(12,6)
    3
    >>> greatestCommonDivisor(5,25)
    5
    '''
    return math.gcd(a,b)

def summatory (numbers_array):
    '''Compute and return the sumatory of a array of numbers
    Usage examples:
    >>> summatory([2,20])
    22
    >>> summatory([2,20,30,50,80])
    182
    >>> summatory([0,0,0,0,0])
    0
    >>> summatory([-2,-2,-6,-8,-8,-8])
    -34
    >>> summatory([-0,-0,-0,-0])
    0
    '''
    return sum(numbers_array)

def factorial(n):
    """
    Calculate the factorial of a positive number.
    
    Args:
        n (int): El número del cual se desea calcular el factorial.
    
    Returns:
        int: El factorial de n.
    
    Raises:
        ValueError: Si n no es un número entero positivo.
    
    Examples:
        >>> factorial(0)
        1
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: El número debe ser entero positivo.
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        >>> factorial(1)
        1
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser entero positivo.")
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result