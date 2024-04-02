#Unlimited positional arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# print(add(1,2,3,4))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print (n)

calculate(2, add = 3, multiply= 3)

class CAr:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = CAr(make="Nissan", model = "GTR")
print(my_car.model)