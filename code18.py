# Python

score = input("Enter your score: ")
try: 
    if float(score) >=0.9:
        print("Grade: A")
    elif float(score) >=0.8:
        print("Grade: B")
    elif float(score) >=0.7:
        print("Grade: C")
    elif float(score) >=0.6:
        print("Grade: D")
    elif float(score)a < 0.6:
        print("Grade: F")
except:
    print("Bad score")