def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m) ** 2)
    return weight / (height ** 2)

def categorize_bmi(bmi):
    # Classify BMI into categories
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("BMI Calculator")

    # Get valid user inputs
    weight = get_valid_input("Enter your weight in kilograms: ", 20, 300)
    height = get_valid_input("Enter your height in meters: ", 0.5, 2.5)

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify and display the result
    category = categorize_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()
