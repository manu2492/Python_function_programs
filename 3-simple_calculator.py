print("""
please select one option:
    a-sustract
    b-add
    c-multiply
    d-divide
""")

operator = input('please select an option')
number1 = int(input('please select a number'))
number2 = int(input('please select your second number'))

def run(operator, number1, number2):

    if operator == 'a':
        print(number1 - number2)

    elif operator == 'b':
        print(number1 + number2)

    elif operator == 'c':
        print(number1 * number2)

    else:
        print(number1 / number2)

run(operator, number1, number2)





































