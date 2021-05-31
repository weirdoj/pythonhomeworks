# Create file and read file
# r : read file
# w : write file
# w+ : read and write

import os

#os.path.join("dev","python","file.txt")

st = open("file1.txt","w")
st.write("Today is Monday.")
st.close()

# new exercise, open file and add file content into list.

import os
mylist = list()

with open ("file.txt","r") as f:
    mylist.append(f.read())

with open ("file1.txt","w") as s:
    s.write("Today it is raining hard")

with open ("file1.txt","r") as s:
    mylist.append(s.read())

print(mylist)
