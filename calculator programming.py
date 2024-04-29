# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division, avoiding division by zero
def divide(x, y):
    try:
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")
    except ValueError as e:
        return str(e)

# Function to find the remainder
def remainder(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Cannot calculate remainder with zero divisor."

# Function to calculate the area of a circle using the radius
def area_of_circle(radius):
    return 3.14 * radius**2

# Function to calculate the circumference of a circle using the radius
def circumference_of_circle(radius):
    return 2 * 3.14 * radius

# Function to calculate the length of the hypotenuse using the Pythagorean theorem
def hypotenuse_length(a, b):
    return (a**2 + b**2)**0.5

# Function to convert square feet to square yards
def sqft_to_sqyd(sqft):
    return sqft / 9.0

# Function to convert square yards to square feet
def sqyd_to_sqft(sqyd):
    return sqyd * 9.0

# Function to convert liters to gallons
def litre_to_gallon(litre):
    return litre * 0.264172

# Function to convert gallons to liters
def gallon_to_litre(gallon):
    return gallon / 0.264172

# Function to convert feet to inches
def ft_to_inches(feet):
    return feet * 12.0

# Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54

# Function to convert centimeters to inches
def cm_to_inches(cm):
    return cm / 2.54

# Function to convert feet to centimeters
def feet_to_cm(feet):
    return feet * 30.48

# Function to convert inches to feet
def inches_to_feet_inches(length_in_inches): 
    feet = length_in_inches // 12
    inches = length_in_inches % 12
    return feet, inches                             #This will tell us the result in feet inches for example 62 inches is equal to 5 feet 2 inches

# Function to convert centimeters to feet
def cm_to_feet(cm):
    return cm / 30.48

# Main function to drive the program
def main():
    while True:
        print("Simple Calculator and Conversion Program:")
        print("1. Arithmetic Operations")
        print("2. Area and Circumference of Circle")
        print("3. Length of Hypotenuse (Pythagorean theorem)")
        print("4. Conversion")

        choice = input("Enter choice (1-4): ")

        if choice in ['1', '2', '3']:
            try:
                # Arithmetic operations and geometric calculations
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Remainder")
                try:
                    operation_choice = int(input("Enter operation choice (1-5): "))
                except ValueError:
                    print("Invalid input. Please enter a numerical choice.")
                    continue

                if operation_choice == 1:
                    result = add(num1, num2)
                elif operation_choice == 2:
                    result = subtract(num1, num2)
                elif operation_choice == 3:
                    result = multiply(num1, num2)
                elif operation_choice == 4:
                    result = divide(num1, num2)
                elif operation_choice == 5:
                    result = remainder(num1, num2)
                else:
                    print("Invalid operation choice. Please enter a number between 1 and 5.")

            elif choice == '2':
                radius = num1  # Assuming num1 is the radius for this calculation
                print("1. Area of Circle")
                print("2. Circumference of Circle")
                try:
                    geometric_choice = int(input("Enter geometric calculation choice (1-2): "))
                except ValueError:
                    print("Invalid input. Please enter a numerical choice.")
                    continue

                if geometric_choice == 1:
                    result = area_of_circle(radius)
                elif geometric_choice == 2:
                    result = circumference_of_circle(radius)
                else:
                    print("Invalid geometric calculation choice. Please enter 1 or 2.")

            elif choice == '3':
                try:
                    side_a = float(input("Enter side A: "))  # Assuming num1 is side A for this calculation
                    side_b = float(input("Enter side B: "))  # Assuming num2 is side B for this calculation
                except ValueError:
                    print("Invalid input. Please enter numerical values for side A and side B.")
                    continue

                result = hypotenuse_length(side_a, side_b)

            print("Result: ", result)

        elif choice == '4':
            print("Conversion Options:")
            print("1. Square Feet to Square Yards")
            print("2. Square Yards to Square Feet")
            print("3. Liters to Gallons")
            print("4. Gallons to Liters")
            print("5. Feet to Inches")
            print("6. Inches to Centimeters")
            print("7. Centimeters to Inches")
            print("8. Feet to Centimeters")
            print("9. Inches to Feet")
            print("10. Centimeters to Feet")
            try:
                conversion_choice = int(input("Enter conversion choice (1-10): "))
            except ValueError:
                print("Invalid input. Please enter a numerical choice.")
                continue

            if conversion_choice == 1:
                try:
                    sqft = float(input("Enter area in square feet: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for area.")
                    continue
                result = sqft_to_sqyd(sqft)
                print("Result: ", result, " square yards")
            elif conversion_choice == 2:
                try:
                    sqyd = float(input("Enter area in square yards: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for area.")
                    continue
                result = sqyd_to_sqft(sqyd)
                print("Result: ", result, " square feet")
            elif conversion_choice == 3:
                try:
                    litre = float(input("Enter volume in liters: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for volume.")
                    continue
                result = litre_to_gallon(litre)
                print("Result: ", result, " gallons")
            elif conversion_choice == 4:
                try:
                    gallon = float(input("Enter volume in gallons: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for volume.")
                    continue
                result = gallon_to_litre(gallon)
                print("Result: ", result, " liters")
            elif conversion_choice == 5:
                try:
                    feet = float(input("Enter length in feet: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                result = ft_to_inches(feet)
                print("Result: ", result, " inches")
            elif conversion_choice == 6:
                try:
                    inches = float(input("Enter length in inches: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                result = inches_to_cm(inches)
                print("Result: ", result, " centimeters")
            elif conversion_choice == 7:
                try:
                    cm = float(input("Enter length in centimeters: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                result = cm_to_inches(cm)
                print("Result: ", result, " inches")
            elif conversion_choice == 8:
                try:
                    feet = float(input("Enter length in feet: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                result = feet_to_cm(feet)
                print("Result: ", result, " centimeters")
            elif conversion_choice == 9:
                try:
                    length_in_inches = float(input("Enter length in inches: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                feet, inches = inches_to_feet_inches(length_in_inches)
                print("Result:", feet, "feet", inches, "inches" )
            elif conversion_choice == 10:
                try:
                    cm = float(input("Enter length in centimeters: "))
                except ValueError:
                    print("Invalid input. Please enter a numerical value for length.")
                    continue
                result = cm_to_feet(cm)
                print("Result: ", result, " feet")
            else:
                print("Invalid conversion choice. Please enter a number between 1 and 10.")

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        another_calculation = input("Do you want to perform another calculation or conversion? (yes/no): ")
        if another_calculation.lower() not in ['yes', 'y']:
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
