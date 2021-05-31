fruit = list()
fruit = ["Apple", "Orange", "Pear"]
print(fruit)
print(fruit[2])

colors = ["yellow", "red", "green"]
print(colors)
item = colors.pop()
print(item)
print(colors)

color1 = ["yellow", "red", "green"]
color2 = ["brown", "blue", "pink"]
colors = color1 + color2

print(colors)

print("green" in colors)
print("yellow" in colors)
print("black" not in colors)
print("white" not in colors)

print(len(colors))

guess = input("You can guess a color: ")

if (guess in colors):
    print("Your guess is corrected")
else:
    print("Your guess is WRONG")
