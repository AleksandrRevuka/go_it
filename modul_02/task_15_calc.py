result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            user_input = input("Enter number: ")
        else:
            user_input = input("Enter operator: ")
        if user_input == "=":
            print(result)
            break
        if wait_for_number and user_input.isnumeric():
            operand = float(user_input)
            wait_for_number = False
        elif not wait_for_number and user_input in ["+", "-", "*", "/"]:
            operator = user_input
            wait_for_number = True
        else:
            print(f"'{user_input}' is not a number or '+' or '-' or '/' or '*'. Try again.")
        if result is None:
            result = operand
        if operator and not wait_for_number:
            if operator == "+":
                result = result + float(user_input)
            elif operator == "-":
                result = result - float(user_input)
            elif operator == "*":
                result = result * float(user_input)
            elif operator == "/":
                result = result / float(user_input)
            operator = None
            wait_for_number = False

    except ZeroDivisionError:
        print("Zero division error")
        break
