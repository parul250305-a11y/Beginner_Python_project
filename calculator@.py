def calculator():
    print("\nSimple Calculator")
    print("Press Q to Quit")

    operation = input("Enter operation (+, -, *, /): ")

    # Exit condition (base case)
    if operation.lower() == 'q':
        print("Thanks for using, see you again!")
        return

    try:
        a = float(input("Enter number A: "))
        b = float(input("Enter number B: "))

        match operation:
            case "+":
                print("Result:", a + b)

            case "-":
                print("Result:", a - b)

            case "*":
                print("Result:", a * b)

            case "/":
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Cannot divide by zero")

            case _:
                print("Invalid operation")

    except:
        print("Enter valid numbers!")

    # Recursive call (runs again)
    calculator()


# Start the calculator
calculator()


"""
try:
    a = int(input("Enter a Number A: "))
    b = int(input("Enter another Number B: "))
    print("enter operation : \n press + for add \n press - for subtract \n  press * for multiplication \n press \ for divide")

    operation = input("Enter Operation: ")

    match operation:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case _:
            print("Invalid operation")

except Exception:
    print("Error: Enter valid numbers")

"""
