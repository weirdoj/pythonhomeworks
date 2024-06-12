#code4.py
# Ask for 2 numbers, if the first one is larger than the second, display the second number first and than the first number. Otherwise show the first number first and then the second

firstnumber = int(input("Enter number 1: "))
secondnumber = int(input("Enter number 2: "))

if firstnumber > secondnumber:
    print(firstnumber, secondnumber)
else:
    print(secondnumber, firstnumber)
    

