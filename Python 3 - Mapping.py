# EX3
# Name: Sahar Ithzak
# ID: 308389485


##################### Program 1 #####################
# user enters a radius and program prints the
# circle's perimeter

from math import pi
radius = float(input("Enter radius\n"))
print(2*pi*radius)

##################### Program 2 #####################
# user enters 2 series of integers and if the numbers
# of list 2 are exponent of list 1 program will print
# the sum of the 2 numbers of same index

list1 = [int(x) for x in input("Enter first list\n").split()]
list2 = [int(x) for x in input("Enter second list\n").split()]
result = []

for i in range(len(list1)):
    if list1[i]**2 != list2[i]:
        print("Error\n")
        exit(0)
    result.append(list1[i] + list2[i])

for i in result:
    print(i, end=" ")

##################### Program 3 #####################
# user enters a list of different types and porgram
# prints only the integers

x = [i for i in input("Enter input\n").split()]
print(list(filter(lambda x: x.isdigit(), x)))

##################### Program 4 #####################
# program prints the numbers from 0-200 that gives 0
# when divided by 5 and 7

list = []
[list.append(x) for x in range(0, 201) if x%5 == 0 and x%7 == 0]
print(list)


