# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product():
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price
   
if __name__ == "__main__":
   p = Product(300)
   print(p.price)
   p.price =250
   print(p.price)
   del p.price
   print(p.price)
        