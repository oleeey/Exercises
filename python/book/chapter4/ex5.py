# Write a function that converts a string to a float and returns the result. Use exception handling to catch the
# exception that could occur.

def convStr(text):
    """
    returns string input converted to a floating point number
    param text: string
    return: string
    """
    try:
        return float(text)

    except ValueError:
        print("Invalid input!")

print(convStr("1.28"))