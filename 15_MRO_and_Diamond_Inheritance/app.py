class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")
class D(B, C):
    pass

if __name__ == "__main__":
    obj = D()
    obj.show()