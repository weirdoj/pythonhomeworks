#python program showing how to multiple input using split

x,y = input("Enter 2 values: ").split()

print("Number of boys: ", x)
print("number of girls: ", y)
print("First number is {} and second number is {}".format(x,y))

x=[int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)