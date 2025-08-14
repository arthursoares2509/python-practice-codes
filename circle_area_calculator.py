import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    print("\nWelcome to the Circle Area Calculator!\n")
    
    while True:
        radius_input = input("Please enter the radius of the circle: ").strip()
        
        try:
            radius = float(radius_input)
            if radius <= 0:
                print("The radius must be a positive number. Try again.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")
            continue
        
        area = calculate_circle_area(radius)
        print(f"\nThe area of a circle with radius {radius} is: {area:.2f}\n")
        
        cont = input("Do you want to calculate another circle? (yes/no): ").strip().lower()
        if cont != "yes":
            print("\nExiting the Circle Area Calculator. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
