import csv

lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on the Fire", "Flight"]]

f = open("movies.csv", "w")
w = csv.writer(f, delimiter=",")
for list in lists:
    w.writerow(list)