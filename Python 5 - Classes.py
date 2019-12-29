
class Product:
    num_of_instances = 0

    def __init__(self, code, class_name, stock, min_item, price):
        self.code = code
        self.class_name = class_name
        self.stock = stock
        self.min_item = min_item
        self.price = price

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def class_name(self):
        return self.__class_name
    @class_name.setter
    def class_name(self, class_name):
        self.__class_name = class_name

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    @property
    def min_item(self):
        return self.__min_item
    @min_item.setter
    def min_item(self, min_item):
        self.__min_item = min_item

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return str(self.code) + " " + self.class_name + " " + \
               str(self.stock) + " " + str(self.min_item) + " " + str(self.price)



class ProductList:
    def __init__(self):
        self.m_products = []
        self.m_products.append(Product(1111, 'Vegetables', 150, 20, 5))
        self.m_products.append(Product(2222, 'Fruits', 100, 15, 6))
        self.m_products.append(Product(3333, 'Meat', 5, 10, 10))
        self.m_products.append(Product(4444, 'Cheese', 100, 15, 8))



prod = ProductList()


# C
def check_stock():
    for i in range(0, len(prod.m_products)):
        if prod.m_products[i].stock < prod.m_products[i].min_item:
            print("Item code: ", prod.m_products[i].code)
            print("Need to order: ", prod.m_products[i].min_item - prod.m_products[i].stock)
            print()

# E
def item_price():
    code = int(input("Enter item's code\n"))
    for i in range(0, len(prod.m_products)):
        if code == int(prod.m_products[i].code):
            print("Items price", prod.m_products[i].price)
            break
    else:
        print("Wrong code\n")

# F
def check_amount():
    counter = 0
    amount = int(input("Enter item's code\n"))
    for i in range(0, len(prod.m_products)):
        if amount < prod.m_products[i].stock:
            counter += 1
    print("Number of items less then amout: ", counter)



check_stock() #C
item_price() #E
check_amount() #F


