class MathsOperators:
    def __init__(self, numbers):
        self.numbers = numbers

    def add(self):
            """
            Sumatory of a numbers groups
            """
            total = 0
            for number in self.numbers:
                total += number
            return total


    def product(self):
            """
            Product of a numbers group
            """
            total = 1
            for number in self.numbers:
                total *= number
            return total