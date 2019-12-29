
# def func():
#     x = abs(int(input("Enter a positive integer\n")))
#     D = abs(float(input("Enter accuracy level\n")))
#
#     result = 0
#     while(True):
#         for i in range(0, 100):
#             next_num = calc(i, x)
#             result += next_num
#             if next_num < D:
#                 print(result)
#                 print(i)
#                 return
#
#
# def calc(i, x):
#     import math
#     return x ** i / math.factorial(i)
#
#
# func()


import math


def func():
    x = abs(int(input("Enter a positive integer\n")))
    d = abs(float(input("Enter accuracy level\n")))
    sum = 0
    index = 0
    next_num = 1
    print(rec_func(x, d, next_num, index, sum))


def rec_func(x, d, next_num, index, sum):
    if next_num < d:
        print(index)
        return sum
    index += 1
    next_num = float(calc(index, x))
    return float(rec_func(x, d, next_num, index, sum) + next_num)


def calc(i, x):
    return x ** i / math.factorial(i)


func()