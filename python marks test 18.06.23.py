marks = int(input("Enter your marks: "))  # Convert input to integer
40
if marks > 75:
    print("A")
    print("CONGRATULATIONS")
elif marks >= 65 and marks < 75:  # Use 'and' instead of 'or' for the correct range condition
    print("B")
elif marks >= 55 and marks < 65:
    print("C")
elif marks >= 45 and marks < 55:
    print("S")
else:
    print("F")
    print("Do better next time")  # Indentation fixed and added colon ':' after 'if marks<45'


