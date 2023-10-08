# Write a program that lets the user ask your height, favourite colour, or favourite author, and returns
# the result from the dictionary you created in the previous challenge.

myDict = {"Height": 1.91, "Favourite color": "Black", "Occupation": "IT Technician"}

def askUser(name):
    if name in myDict:
        print(myDict[name])
    else:
        print("No data available")

askUser("Height")
askUser("Heightt")