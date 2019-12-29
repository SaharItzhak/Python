
def get_data():
    num = 0
    my_list = []
    while num != -1:
        try:
            num = input("Please enter an integer or -1 to end\n")
            num = int(num)
            my_list.append(num)
        except ValueError:
            print("Not an integer\n")
    my_list = my_list[:-1]
    if len(my_list) % 2 != 0:
        raise ValueError("list must at even length\n")
    index = len(my_list)
    symmetric(index-1, my_list, 0)


def symmetric(index, my_list, i):
    if index == 0:
        return True
    else:
        if (int(my_list[index]) + int(my_list[i])) != 10:
            raise ValueError("Not a sum of a geometric series\n")
        symmetric(index-1, my_list, i+1)


get_data()
print(True)


# def symmetric():
#     my_list = []
#     counter = 0
#     while(counter != 4):
#         num = input("Please enter an integer\n")
#         try:
#             num = int(num)
#         except ValueError as value_error:
#             print(str(value_error))
#         else:
#             my_list.append(num)
#             print("{} was entered\n".format(num))
#             counter += 1
#
#     check_sym(my_list)
#
# def check_sym(my_list):
#     print(my_list)
#     print("BYE\n")
#
# symmetric()


