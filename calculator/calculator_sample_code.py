'''
CALCULATORS STANDARD AND POSTFIX
'''

def infix_calculator(calculation):
    calculation_split = calculation.split(" ")
    result = int(calculation_split[0])

    for i in calculation_split[1:]:
        if not i.isdigit():
            operator = i
        else:
            if operator == "+":
                result += int(i)
            if operator == "-":
                result -= int(i)
            if operator == "*":
                result *= int(i)
            if operator == "/":
                result /= int(i)
    print(result)
    return result

def postfix_calculator(calculation):
    calculation_split = calculation.split(" ")

    calculator_stack = []

    for i in calculation_split:
        if i.isdigit():
            calculator_stack.append(i)
        else:
            last_item = int(calculator_stack.pop(-1))
            second_last_item = int(calculator_stack.pop(-1))
            if i == "+":
                result = last_item + second_last_item
            if i == "-":
                result = last_item - second_last_item
            if i == "*":
                result = last_item * second_last_item
            if i == "/":
                result = last_item / second_last_item
            calculator_stack.append(result)
    print(calculator_stack[0])
    return calculator_stack[0]

if __name__ == "__main__":
    infix_calculator("2 - 2")
    postfix_calculator("2 2 - 5 +")