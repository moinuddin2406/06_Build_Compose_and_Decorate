# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class mathUtils:
    @staticmethod
    def add(a,b):
        return a+b

if __name__ == "__main__":
    result = mathUtils.add(4,5)
    print("Total :", result)