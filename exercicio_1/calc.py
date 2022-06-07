firstValue = int(input("First value: "))
operator = input("Operator: ")
secondValue = int(input("Second value: "))

result = float

OPERATOR_SUM = "+"
OPERATOR_SUBTRACTION = "-"
OPERATOR_MULTIPLICATION = "*"
OPERATOR_DIVISION = "/"

#Main

if operator == OPERATOR_SUM:
    result = firstValue + secondValue
elif operator == OPERATOR_SUBTRACTION:
    result = firstValue - secondValue
elif operator == OPERATOR_MULTIPLICATION:
    result = firstValue * secondValue
elif operator == OPERATOR_DIVISION:
    result = firstValue / secondValue
else:
    print("Invalid option!")
    quit()

print(f"{firstValue} {operator} {secondValue} = {result}")