try:
    firstValue = int(input("First value: "))
    secondValue = int(input("Second value: "))
except Exception as exception:
    print("Invalid number")
    exit(1)

operator = input("Operator: ")

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
    quit(1)

print(f"{firstValue} {operator} {secondValue} = {result}")
