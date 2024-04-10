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

if __name__ == "__main__":
    print(infix_calculator("2 - 2"))