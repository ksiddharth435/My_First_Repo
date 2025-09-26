# Function to print Hello, World!
def print_hello_world():
    print("Hello, World!")

# Function to demonstrate program structure
def demonstrate_structure():
    print('This line is printed directly from the main function of the program')
    secondary_function()

def secondary_function():
    print('This line is printed from a secondary function call within the main function')
    tertiary_function()

def tertiary_function():
    print('This line is printed from tertiary function which is called from secondary function')

# Function to calculate square
def square(num):
    return num * num

# Function to test square function
def test_square():
    number = float(input("Enter a natural number to be squared: "))
    print('square of number ' + str(number) + ' is ' + str(square(number)))  # Prints 9

# Function for simple input/output
def simple_input_output():
    user_name = input("Enter your name: ")
    print("Hello, " + user_name + "!")

# Function for input/output with square
def input_output_square():
    number = int(input("Enter a whole number to be squared: "))
    print('square of number ' + str(number) + ' is ' + str(square(number)))

# Function to demonstrate Variable Assignments and Types
def variable_assignments_and_types():
    a = 5
    b = 3.2
    c = "Hello"
    d = True
    print(f"a: {a}, type: {type(a)}") # formatted string literals (f-strings)
    print(f"b: {b}, type: {type(b)}") # include variables directly inside strings, evaluated at runtime.
    print(f"c: {c}, type: {type(c)}") # Anything inside {} is evaluated as a Python expression.
    print(f"d: {d}, type: {type(d)}")

# Function to demonstrate operators etc
def operators_demo():
    x = 10
    y = 3
    # Arithmetic Operators
    print(f"x: {x}, y: {y}")  # x and y
    print(f"x + y = {x + y}")  # Addition
    print(f"x - y = {x - y}")  # Subtraction
    print(f"x * y = {x * y}")  # Multiplication
    print(f"x / y = {x / y}")  # Division
    print(f"x // y = {x // y}") # Floor Division
    print(f"x % y = {x % y}")  # Modulus
    print(f"x ** y = {x ** y}") # Exponentiation

    # Assignment Operators
    print(f"x: {x}, y: {y}")  # x and y
    x += 2
    print(f"x after x += 2: {x}")   # x = x + 2
    x *= 3
    print(f"x after x *= 3: {x}")   # x = x * 3
    x -= 5
    print(f"x after x -= 5: {x}")   # x = x - 5
    x /= 4      
    print(f"x after x /= 4: {x}")   # x = x / 4
    x %= 3      
    print(f"x after x %= 3: {x}")   # x = x % 3
    x **= 2             
    print(f"x after x **= 2: {x}")  # x = x ** 2
    x //= 2
    print(f"x after x //= 2: {x}")  # x = x // 2
    x = 10  # Reset x for further operations

    # Comparison Operators
    print(f"x: {x}, y: {y}")  # x and y
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"x < y: {x < y}")
    print(f"x >= y: {x >= y}")
    print(f"x <= y: {x <= y}")

    # Logical Operators
    a = True
    b = False
    print(f"a { a } b { b }")
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"not a: {not a}")

# Main function to call steps as per user's wish
def main():
    print("Choose an option:")
    print("1. Print Hello World")
    print("2. Demonstrate program structure")
    print("3. Test square function")
    print("4. Simple input/output")
    print("5. Input/output with square")
    print("6. Variable assignments and types")
    print("7. Operators demonstration")
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        print_hello_world()
    elif choice == '2':
        demonstrate_structure()
    elif choice == '3':
        test_square()
    elif choice == '4':
        simple_input_output()
    elif choice == '5':
        input_output_square()
    elif choice == '6':
        variable_assignments_and_types()
    elif choice == '7':
        operators_demo()
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()