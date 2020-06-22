class Fib:
    def __init__(self, min, max=0):
        self.min = min
        self.max = max

    def fibonacci(self):
        a = 0
        b = 1
        while True:
            c = a + b
            a = b
            b = c
            if self.max == 0:
                if len(str(b)) == self.min:
                    print(b)
                if len(str(b)) > self.min:
                    break
            else:
                if b in range(self.min, self.max + 1):
                    print(b)
                if b > self.max:
                    break


if __name__ == '__main__':
    fib = Fib(2)
    fib.fibonacci()
