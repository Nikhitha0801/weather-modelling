import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Not a quadratic equation (a = 0).")
        return
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Two Real Roots: {root1:.2f}, {root2:.2f}")
    elif d == 0:
        root = -b / (2*a)
        print(f"One Real Root: {root:.2f}")
    else:
        print("Complex Roots, No Real Solution.")

def hardcoded_input():
    print("\n--- Hardcoded Values ---")
    a, b, c = 1, -3, 2
    print(f"Equation: {a}x² + {b}x + {c} = 0")
    solve_quadratic(a, b, c)

def keyboard_input():
    print("\n--- Keyboard Input ---")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print(f"Equation: {a}x² + {b}x + {c} = 0")
    solve_quadratic(a, b, c)

def file_input_single():
    print("\n--- File Input (Single Set) ---")
    filename = input("Enter filename (e.g., input1.txt): ")
    try:
        with open(filename, "r") as file:
            line = file.readline()
            a, b, c = map(float, line.strip().split())
            print(f"Equation: {a}x² + {b}x + {c} = 0")
            solve_quadratic(a, b, c)
    except Exception as e:
        print("Error reading file:", e)

def file_input_multiple():
    print("\n--- File Input (Multiple Sets) ---")
    filename = input("Enter filename (e.g., input2.txt): ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for idx, line in enumerate(lines):
                try:
                    a, b, c = map(float, line.strip().split())
                    print(f"\nEquation {idx + 1}: {a}x² + {b}x + {c} = 0")
                    solve_quadratic(a, b, c)
                except:
                    print(f"Invalid input on line {idx + 1}: {line.strip()}")
    except Exception as e:
        print("Error reading file:", e)

# Main Menu
while True:
    print("\n========== Weather Modeling using Quadratic Equation ==========")
    print("1. Hardcoded values")
    print("2. Keyboard input")
    print("3. File input (single set)")
    print("4. File input (multiple sets)")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        hardcoded_input()
    elif choice == '2':
        keyboard_input()
    elif choice == '3':
        file_input_single()
    elif choice == '4':
        file_input_multiple()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
