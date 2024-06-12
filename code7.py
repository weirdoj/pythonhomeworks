#code7.py

#ask the user to enter their favourit colour. If they enter "red" or "RED", display message "I like red too", otherwise display the message "I don't like [colour], i prefer red


color = input("Enter your colour: ")

color = str.lower(color)

if color == "red":
        print("I like red too")
else:
        print(f"I dont like {color}, I prefer red")

