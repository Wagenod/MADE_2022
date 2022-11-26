# Task 1
#Функция д олжна принимать коэффициенты -a, b, c- квадратного уравнения
#a*x^2 + b*x + c = 0
#и возвращать кортеж квадратных коорней или None, если корней нет.

from math import sqrt


def solve_quadratic_equation(a, b, c):

    # if equation is not quadratic 
    if not a:
        if not b:
            return None

        return -c/b

    # if equation is quadratic
    D = b**2 - 4*a*c
    if D < 0:
        return None
    elif D == 0:
        return -b/(2*a), 
    else:
        return (-b + sqrt(D))/(2*a), (-b - sqrt(D))/(2*a)


print("Testing function solve_quadratic_equation ....")
assert solve_quadratic_equation(0, 0, 2) is None
assert solve_quadratic_equation(0, 3, 6) == -2
assert solve_quadratic_equation(1, 3, 6) is None
assert solve_quadratic_equation(1, -4, 4) == (2, )
assert solve_quadratic_equation(1, -3, 2) == (2, 1)
print ("Ok! All tests passed")


# Task 2
#Функция должна принимать на вход список чисел, разделять его на два 
#списка: четных и нечетных чисел, и возвращать кортеж из двух списков: четных и нечетных.

def split_even_odd_nums(numbers: list) -> tuple:
    if not numbers:
        return ()

    even_nums = []
    odd_nums = []
    for num in numbers:
        if not num%2:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    return even_nums, odd_nums


print("Testing function split_even_odd_nums ...")
assert split_even_odd_nums([]) == ()
assert split_even_odd_nums([2, 3, 1, 5]) == ([2], [3, 1, 5])
assert split_even_odd_nums([7, 3, 1, 5]) == ([], [7, 3, 1, 5])
assert split_even_odd_nums([2, 4]) == ([2, 4], [])
print ("Ok! All tests passed")
