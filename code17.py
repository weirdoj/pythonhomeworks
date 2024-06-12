#change fahrenheit to celsius
try:
    inp = float(input("Enter Fahrenheit temperature: "))
    cel =   (inp - 32.0) * 5.0 / 9.0

    print("Celsius temperature is : ", cel)
except:
    print("Please enter a number")

