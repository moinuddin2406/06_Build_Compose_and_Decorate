# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start        # set the starting number
        self.current = start      # initialize current to the starting number

    def __iter__(self):
        # Return the iterator object itself
        return self
    
    def __next__(self):
        # if current is less than 0, stop the iteration
        if self.current < 0:
            raise StopIteration
        # Decrease current by 1 and return the value
        self.current -= 1
        return self.current + 1   # Return the number before decrementing

# creating the countdown object
countdown = Countdown(5)

# using countdown object in a for loop
for number in countdown:
    print(number)
