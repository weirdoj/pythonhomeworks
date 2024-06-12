#python code

print("This is a simple program\n")
print("Note: simple way to do\n")
print()

print("Challenges")
# Ask for the user first name and display the output message
name = input("Please input your name: ")
print("Hello", name)

# Ask for the user's first name and then ask for their surname and display output message

firstname = input("Please input your first name: ")
surname = input("Please input your last name: ")
print("Hello", firstname, surname)

#write code that will display the joke "What do you call a bear with no teeth?" and on the next line display the answer "A gummy bear!" Try to create it using only one line of code

print("What do you call a bear with no teeth?\nA gummy bear! ")

# Ask for the total price of bill, then ask how many dinner there are. Divide the total bill by the number of diners and show how much each person must pay

total = int(input("What is the total pay: "))
people = int(input("Number of people: "))
eachpay = total / people
print("Each people must pay: ", eachpay)

num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2st number: "))
num3 = int(input("Please enter 3rd number: "))
answer = (num1 + num2) * num3
print("The answer is ", answer)



