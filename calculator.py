#Calculator
num1 = float(input("Enter a number: "))
operator = input("Choose the operator (+,-,/,*): ")
num2 = float(input("Enter another number: "))

if operator=="+":
    print(f"Answer: {num1} + {num2} = {num1+num2}")
elif operator== "-":
    print(f"Answer: {num1} - {num2} = {num1-num2}")
elif operator=="*":
    print(f"Answer: {num1} * {num2} = {num1*num2}")
elif operator=="/":
    print(f"Answer: {num1} / {num2} = {num1/num2}")
else:
    print("Please enter correct operator!")
