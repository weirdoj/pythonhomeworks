# exercise 1
for c in "Camus":
    print(c)
    
# exercise 2
print("aldous was born in 1894.".capitalize())


# exercise 3
print("Where now? Who now? When now?".split('?'))

# exercise 4
print(' '.join(["The", "fox", "jumped", "over", "the", "fence", "."]))

# exercise 5
print("three" + "three" + "three")
print("three" * 3)

#exercise 6
#use \ to display \" Text in here \" in quote
print("She said \"Surely\"")

#exercise 7
my_string = "We are holding the true".capitalize()
my_string1 = "We are holding the true".upper()
print(my_string)
print(my_string1)

#exercise 8
n1 = input("Enter a noun: ")

v1 = input("Enter a verd: ")

adj = input("Enter an adjective: ")

n2 = input("Enter a noun: ")

r = """ The {} {} the {} {} """.format(n1, v1, adj, n2)
print(r)

