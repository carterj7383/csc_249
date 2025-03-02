#Joshua Carter
#2.H1_Recursion 
#Data Structure & Algorithms (CSC-249-0901)

def factorial_iterative(n):
    if n < 0:
        return "Error: Can't calculate factorial of a negative."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    if n < 0:
        return "Error: Can't calculate factorial of a negative."
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    if n < 0:
        return "Error: Can't calculate Fibonacci for negative numbers."
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    
    return b


def fibonacci_recursive(n):
    if n < 0:
        return "Error: Can't calculate Fibonacci for negative numbers."
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def display_menu():
    print("\n=== ALGORITHM IMPLEMENTATION ===")
    print("1. Factorial (Iterative)")
    print("2. Factorial (Recursive)")
    print("3. Fibonacci (Iterative)")
    print("4. Fibonacci (Recursive)")
    print("5. Run all with test values")
    print("6. Exit")
    return input("Enter your choice (1-6): ")


def get_number():
    while True:
        try:
            return int(input("Enter a non-negative integer: "))
        except ValueError:
            print("Please enter a valid integer.")


def run_all_tests():
    test_numbers = [0, 5, 10]
    
    print("\nITERATIVE FACTORIAL")
    print("-----------------")
    for num in test_numbers:
        result = factorial_iterative(num)
        print(f"{num}! = {result}")
    
    print("\nRECURSIVE FACTORIAL")
    print("-----------------")
    for num in test_numbers:
        result = factorial_recursive(num)
        print(f"{num}! = {result}")
    
    print("\nITERATIVE FIBONACCI")
    print("-----------------")
    for num in test_numbers:
        result = fibonacci_iterative(num)
        print(f"Fibonacci({num}) = {result}")
    
    print("\nRECURSIVE FIBONACCI")
    print("-----------------")
    for num in test_numbers:
        result = fibonacci_recursive(num)
        print(f"Fibonacci({num}) = {result}")


def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            n = get_number()
            result = factorial_iterative(n)
            print(f"\nFactorial of {n} (Iterative): {result}")
            
        elif choice == '2':
            n = get_number()
            if n > 995:
                print("Value too large for recursive approach. Try a smaller number.")
            else:
                result = factorial_recursive(n)
                print(f"\nFactorial of {n} (Recursive): {result}")
            
        elif choice == '3':
            n = get_number()
            result = fibonacci_iterative(n)
            print(f"\nFibonacci({n}) (Iterative): {result}")
            
        elif choice == '4':
            n = get_number()
            if n > 35:
                print("Value too large for basic recursion. Try a smaller number.")
            else:
                result = fibonacci_recursive(n)
                print(f"\nFibonacci({n}) (Recursive): {result}")
            
        elif choice == '5':
            run_all_tests()
            
        elif choice == '6':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    print("Welcome to the Iterative vs Recursive Algorithm Implementations")
    main()