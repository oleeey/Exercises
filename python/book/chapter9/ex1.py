import os, csv

os.chdir("C:\\Users\oleee\Desktop")

f = open("finanzen.csv", "r")
r = csv.reader(f, delimiter=",")
for row in r:
    print(row)
