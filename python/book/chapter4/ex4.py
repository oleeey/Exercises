# Write a program with two functions. The first function should take an integer as a parameter and return the 
# result of the integer divided by 2. The second function shuld take an integer as a parameter and return the
# result of the integer multiplied by 4. Call the first function, save the result as a variable, and pass it
# as a parameter to the second function.

def divNum(num):
    return num / 2

def mulNum(num):
    return num * 4

x = divNum(10)
y = mulNum(x)
print(y)
