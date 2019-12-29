
# EX3
# Name: Sahar Ithzak
# ID: 308389485


##################### Program 1 #####################
# program prints the prime numbers from 1-200

# from math import sqrt
#
# list = []
# for i in range(2, 200):
#     for j in range(2, int(sqrt(i))+1):
#         if(i % j == 0):
#             break
#     else:
#         list.append(i)
#
# for i, j in enumerate(list):
#     print(i, j)


##################### Program 2 #####################

# x = int(input("Enter first number\n"))
# y = int(input("Enter second number\n"))
#
# def add(x, y):
#     return x+y
# def dec(x, y):
#     return x-y
# def mul(x, y):
#     return x*y
# def dev(x, y):
#     return x/y
# def dev_round(x, y):
#     return x//y
# def mod(x, y):
#     return x%y
# def pow(x, y):
#     return x**y
#
# funcs = [add, dec, mul, dev, dev_round, mod, pow]
# values = list(map(lambda a: a(x, y), funcs))
# print(values)

##################### Program 3 #####################

basket = ['Tomatoes', 'Cucumbers', 'Peppers', 'Onions',
          'Potatoes', 'Carrots', 'Zucchinis', 'Cabbages',
          'Lettuces', 'Eggplants']

dict = {}
result = []
for i in basket:
    result.append(int(input("how many {}?".format(i))))

x = dict(sorted(result.items()))
print(x)
#[print(i, j, end=" ") for i in basket for j in result]


print_list = {}

for i in basket:
    num = input("how many {}? ".format(i))
    if not num:
        num = 0
    print_list[i] = int(num)


print_list = dict(sorted(print_list.items(), key=lambda pair:pair[1],reverse=True))
print(print_list)
