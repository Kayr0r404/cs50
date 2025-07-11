# python3

expression = input("put in your expression: ").strip().split()

if expression[1] == "+":
    print(float(round(int(expression[0]) + int(expression[2]), 1)))
elif expression[1] == "-":
    print(float(round(int(expression[0]) - int(expression[2]), 1)))
elif expression[1] == "*":
    print(float(round(int(expression[0]) * int(expression[2]), 1)))
elif expression[1] == "/":
    print(float(round(int(expression[0]) / int(expression[2]), 1)))
