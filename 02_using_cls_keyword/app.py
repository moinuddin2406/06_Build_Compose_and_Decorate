class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
            print(f"Total Objects created: {cls.count}")

if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    obj4 = Counter()
    Counter.show_count()


    