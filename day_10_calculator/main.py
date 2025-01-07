import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def perform_calculation():
    #boolean to determine if we should erase total or use it for next calc
    accumulate = True
    #get user input number 1
    first_number = float(input("What is the first number?"))
    while accumulate:
        #determine which function to call depending on operation
        operation = input("What is the mathematical operation? Choose from *, /, +, -.")
        #get second input #
        second_number = float(input("What is the second number?"))
        #perform chosen calc
        result = operations[operation](first_number,second_number)
        print(f"The answer is {result}")
        #determine if user wants to use total to continue
        continue_with_result = input("Do you want to continue with the same result? Type y or n")
        if continue_with_result == "n":
            accumulate = False
            print("\n" *15)
            perform_calculation()
        if continue_with_result == "y":
            first_number = result

perform_calculation()