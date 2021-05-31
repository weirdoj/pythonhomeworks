my_dict = dict()
print(my_dict)

fruits = {"apple":"red","banana":"yellow"}
print(fruits)

bill = dict({"Bill Gates":"charitable"})

print("Bill Gates" in bill)

ryhms = dict({
  "1":"fun",
  "2":"smile",
  "3":"me",
  "4":"floor"
})

n = input("type a number: ")
if n in ryhms:
    a = ryhms[n]
    print(a)
else:
    print("Not Found")
