class DoubleNumber:
    def __init__(self):
        self.__num = float(input("Enter your number: "))

    def double_num(self):
        return (self.__num * 2)

    def print_double(self):
        print("Here's its double:", self.double_num())


sample = DoubleNumber()
sample.double_num()
sample.print_double()
