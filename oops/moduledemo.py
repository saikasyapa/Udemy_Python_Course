class Kettle(object):

    power_source = 'electricity'         ###class attribute

    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood",8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")
print("models :{0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
class:template for creating objects, all objects created using the small class will have the same characteristics.
object:an instance of a class
instantiate: create an instance of a class
method : a function defined in a class
attribute:a variable bound to an instance of a class
"""
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print('*' * 80)

kenwood.power = 1.5
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

### global variables and functions ,remember that as soon as we try to assign a value to a global variable,
###python create a new local variable that shattered the global one

Kettle.power_source = 'atomic'
print(Kettle.power_source)
kenwood.power_source = 'gas'
print(kenwood.power_source)
hamilton.power_source = 'wind'
print(hamilton.power_source)
