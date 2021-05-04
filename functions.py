def MathFunction(num1, num2, function):
    if function == "+":
        answer = num1 + num2
    elif function == "-":
        answer = num1 - num2
    elif function == "*":
        answer = num1 * num2
    elif function == "/":
        answer = float(num1) / float(num2)

    return answer


def UserInput():
    input("You need to enter 2 numbers to perform and addition.")
    ui_1 = int(input("Enter your first number: "))
    ui_2 = int(input("Enter your second number: "))
    function = str(input("Enter function (*,/,+,-): "))
    added_num = MathFunction(ui_1, ui_2, function)
    return added_num


user_answer = UserInput()

print(user_answer)