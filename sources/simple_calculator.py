
import calc

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Product")
print("4.Division")

while True:
    # Take input from the user
    choice = int(input("Enter choice(1/2/3/4): "))

    
    if choice in (1,2,3,4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(num1, "+", num2, "=", calc.add(num1, num2))

        elif choice == 2:
            print(num1, "-", num2, "=", calc.subtract(num1, num2))
      
        elif choice == 3:
            print(num1, "*", num2, "=", calc.product(num1, num2))

        else:
            print(num1, "/", num2, "=", calc.div(num1, num2))
        continue
    else:
        print("Invalid Input")