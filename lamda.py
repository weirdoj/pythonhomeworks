def myfunction(n):
    return lambda a: a * n

mydoubler = myfunction(2)
print(mydoubler(20))