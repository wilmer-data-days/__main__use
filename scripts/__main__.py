import sys
from maths_operators import MathsOperators

inputs = sys.argv[1:]
numbers = []

if inputs == []:
    print("Please add the numbers group when executed the project")
else:
    [numbers.append(int(x)) for x in inputs]
    instance = MathsOperators(numbers)
    print(f"Sumatory is {instance.add()}")
    print(f"Product is {instance.product()}")

