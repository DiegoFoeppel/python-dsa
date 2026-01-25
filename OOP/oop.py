# classes, methods, attributes and objects

# attributes -> variables inside class
# methods -> functions inside class

class StarCookie():

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def decorate(self):
        pass

    def consume(self):
        return 'Eating the cookie'
    
myCookie = StarCookie(100, 'red')
print(myCookie.color, myCookie.weight, myCookie.consume())



