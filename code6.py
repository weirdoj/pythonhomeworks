#code6.py

# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display message "Thank you", otherwise display the message "Incorrected answer

num = int(input("Enter number : "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrected answer")
