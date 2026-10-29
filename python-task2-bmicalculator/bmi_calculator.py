def calculate_bmi():
    print("===== BMI CALCULATOR =====")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (metres): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("\n----- BMI RESULT -----")
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Error: Enter valid numeric values only.")


if __name__ == "__main__":
    calculate_bmi()
