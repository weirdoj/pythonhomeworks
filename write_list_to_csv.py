# Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 
# and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.


import csv
list= [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant","Inception"], ["Training Day", "Man on Fire", "Flight"]]

# option 1
with open('test.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['List1 ', 'List2', 'List3'])
    writer.writeheader()
    writer = csv.writer(csv_file, lineterminator='\n')
    writer.writerows(list)

# option 2:
with open("movies.csv", "w") as csvfile: 
    spamwriter = csv.writer(csvfile, delimiter=",") 
    for movie_list in list: 
        spamwriter.writerow(movie_list)  
