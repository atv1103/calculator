print("Dear Sir / Madam! Try to show you a calculator.")
print("Please choose a type - simple (operation with two numbers) or complex (endless operation)")
type = input("Enter a \"simple \" or \"complex\" word>> ")

if type == "simple" or type == "Simple" or type == "SIMPLE":  # The simple calculator
    first_number = float(input("Enter the first number>> "))
    operation = input("Enter the symbol (+, -, *, /)>> ")
    second_number = float(input("Enter the second nimber>> "))
    if operation == "+":
        print("Result is", first_number + second_number)
    elif operation == "-":
        print("Result is", first_number - second_number)
    elif operation == "*":
        print("Result is", first_number * second_number)
    elif operation == "/":
        if second_number != 0:
            print("Result is", first_number / second_number)
        print("Cannot be divided by 0!")
    else:
        print("Error")

elif type == "complex" or type == "Complex" or type == "COMPLEX":  # The endless calculator
    total = 0
    text = input(
        "It's endless mode, enter \"Stop\" for end. Enter \"Next\" to start>> ")
    # if Stop
    if text == "stop" or text == "Stop" or text == "STOP":
        print("You didn't count! Your result is 0")
    # if Next
    elif text == "next" or text == "Next" or text == "NEXT":
        first_number = float(input("Enter the first number>> "))
        operation = input("Enter the symbol (+, -, *, /)>> ")
        second_number = float(input("Enter the next number>> "))

        if operation == "+":
            total = first_number + second_number
            print("Total is", total)
            while text != "Stop" or text != "stop" or text != "STOP":
                text = input(
                    "Enter the symbol (+, -, *, /) or enter \"Stop\" for end>> ")
                if text == "Stop" or text == "stop" or text == "STOP":
                    print("Total results is", total)
                    break
                next_number = float(input("Enter the next number>> "))
                total += next_number
                print("Total is", total)

        elif operation == "-":
            total = first_number - second_number
            print("Total is", total)
            while text != "Stop" or text != "stop" or text != "STOP":
                text = input(
                    "Enter the symbol (+, -, *, /) or enter \"Stop\" for end>> ")
                if text == "Stop" or text == "stop" or text == "STOP":
                    print("Total results is", total)
                    break
                next_number = float(input("Enter the next number>> "))
                total -= next_number
                print("Total is", total)

        elif operation == "*":
            total = first_number * second_number
            print("Total is", total)
            while text != "Stop" or text != "stop" or text != "STOP":
                text = input(
                    "Enter the symbol (+, -, *, /) or enter \"Stop\" for end>> ")
                if text == "Stop" or text == "stop" or text == "STOP":
                    print("Total results is", total)
                    break
                next_number = float(input("Enter the next number>> "))
                total *= next_number
                print("Total is", total)

        elif operation == "/":
            if second_number != 0:
                total = first_number / second_number
                print("Total is", total)
                while text != "Stop" or text != "stop" or text != "STOP":
                    text = input(
                        "Enter the symbol (+, -, *, /) or enter \"Stop\" for end>> ")
                    if text == "Stop" or text == "stop" or text == "STOP":
                        print("Total results is", total)
                        break
                    next_number = float(input("Enter the next number>> "))
                    total /= next_number
                    print("Total is", total)
            else:
                print("Cannot be divided by 0!")

        else:  # If wrong operation
            print("Error")
    else:  # If not “Stop” and not “Next”
        print("Error")
else:  # If not “Simple” and not "Complex"
    print("Error")
