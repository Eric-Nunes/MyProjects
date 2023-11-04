def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    
    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {interpretation}")

if __name__ == "__main__":
    main()
