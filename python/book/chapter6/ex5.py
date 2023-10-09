# Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammatically correct
# string. There should be a space between each word, but no space between the word fence and the full stop that
# follows it. (Don't forget, you learned a method that turns a list of strings into a single string.)

list = ["The", "fox", "jumped", "over", "the", "fence", "."]
string = " ".join(list)
string = string[:-2] + "."
print(string)