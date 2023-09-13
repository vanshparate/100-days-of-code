# def add(*args):
#     # print(args[len(args)-1])
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum
# print(add(1,2,3,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply =5)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs['make']
        # self.model = kwargs['model']
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')

# my_car = Car(make='Nissan', model='GT-R')
my_car = Car()
print(my_car.make)