def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def multiply(i, j):
    return i * j

def divide(i, j):
    if j == 0:
        print("Error: Division by zero is not allowed.")
        return None  # Return None to indicate an error
    return i / j

def power(base, exponent):
    if base == 0 and exponent == 0:
        print("Error: 0^0 is undefined.")
        return None  # Return None to indicate an error
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result  # Handle negative exponent
    return result

def inverse(i):
    if i == 0:
        print("Error: Inverse of zero is undefined.")
        return None  # Return None to indicate an error
    return 1 / i

def main():
    confirm = 'n'
    while confirm.lower() == 'y':
        print("\nChoose an operation (+, -, *, /, ^):")
        print("+: Addition")
        print("-: Subtraction")
        print("*: Multiplication")
        print("/: Division")
        print("^: Power of a number (base ^ exponent)")
        print("i: Inverse of a number")
        
        operation = input("Enter operation: ")

        if operation == '+':
            a, b = map(int, input("Enter two integers: ").split())
            print(f"The result of {a} + {b} is {add(a, b)}")
        elif operation == '-':
            a, b = map(int, input("Enter two integers: ").split())
            print(f"The result of {a} - {b} is {subtract(a, b)}")
        elif operation == '*':
            a, b = map(int, input("Enter two integers: ").split())
            print(f"The result of {a} * {b} is {multiply(a, b)}")
        elif operation == '/':
            a, b = map(float, input("Enter two numbers (float values allowed): ").split())
            result = divide(a, b)
            if result is not None:
                print(f"The result of {a} / {b} is {result:.2f}")
        elif operation == '^':
            a, b = map(int, input("Enter base and exponent: ").split())
            result = power(a, b)
            if result is not None:
                print(f"The result of {a} ^ {b} is {result}")
        elif operation == 'i':
            a = int(input("Enter an integer: "))
            result = inverse(a)
            if result is not None:
                print(f"The result of 1/{a} is {result:.2f}")
        else:
            print("Invalid operation. Please try again.")

        confirm = input("Do you want to perform another operation [y/N]? ")

if __name__ == "__main__":
    main()
