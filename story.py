story = """
Roses are {}
Violets are {}
Sugar is {}
And so are you.
"""

color = input("Input color: ")
color2 = input("Input another color: ")
adjective = input("Input an adjective: ")

print(story.format(color, color2, adjective))