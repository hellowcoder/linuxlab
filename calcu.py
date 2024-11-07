def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def multiply(i, j):
    return i * j

def divide(i, j):
    if j == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return i / j

def power(base, exponent):
    return base ** exponent

def inverse(i):
    if i == 0:
        print("Error: Inverse of zero is undefined.")
        return None
    return 1 / i

def get_number_input(prompt, num_type=float):
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Advanced Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("+: Addition")
        print("-: Subtraction")
        print("*: Multiplication")
        print("/: Division")
        print("^: Exponentiation")
        print("i: Inverse (1/x)")
        
        operation = input("Enter operation: ").strip()

        if operation == '+':
            a = get_number_input("Enter first number: ")
            b = get_number_input("Enter second number: ")
            print(f"The result of {a} + {b} is {add(a, b)}")
        
        elif operation == '-':
            a = get_number_input("Enter first number: ")
            b = get_number_input("Enter second number: ")
            print(f"The result of {a} - {b} is {subtract(a, b)}")
        
        elif operation == '*':
            a = get_number_input("Enter first number: ")
            b = get_number_input("Enter second number: ")
            print(f"The result of {a} * {b} is {multiply(a, b)}")
        
        elif operation == '/':
            a = get_number_input("Enter numerator: ")
            b = get_number_input("Enter denominator: ")
            result = divide(a, b)
            if result is not None:
                print(f"The result of {a} / {b} is {result:.5f}")
        
        elif operation == '^':
            a = get_number_input("Enter base: ")
            b = int(input("Enter exponent (integer): "))
            print(f"The result of {a} ^ {b} is {power(a, b)}")
        
        elif operation == 'i':
            a = get_number_input("Enter a number for inverse: ")
            result = inverse(a)
            if result is not None:
                print(f"The result of 1/{a} is {result:.5f}")
        
        else:
            print("Invalid operation. Please try again.")
            continue
        
        confirm = input("\nDo you want to perform another operation [y/N]? ").lower()
        if confirm != 'y':
            print("Thank you for using the Advanced Calculator! Goodbye.")
            break

if __name__ == "__main__":
    main()
