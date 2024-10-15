import argparse

parser = argparse.ArgumentParser(prog="Arithmetic Operation",
                                 description="program for addition, " +
                                 "subtraction, division and " +
                                 "multiplication on 2 numbers")
parser.add_argument('-o', '--operation')
parser.add_argument('-n1', '--num1')
parser.add_argument('-n2', '--num2')
args = parser.parse_args()
operation = args.operation
try:
    num1 = float(args.num1)
    num2 = float(args.num2)
    if operation == "add":
        print(num1 + num2)
    elif operation == "multiply":
        print(num1 * num2)
    elif operation == "divide":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    elif operation == "subtract":
        print(num1 - num2)
    else:
        print("Invalid operation")
except (TypeError, ValueError):
    print("Invalid numerical input")
