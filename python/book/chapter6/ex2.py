# Write a program that collects two strings from a user, inserts them into the string 
# "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string.

resp1 = input("What did you write today? ")
resp2 = input("To whom did you send it? ")

print("Yesterday I wrote a {}. I sent it to {}!".format(resp1, resp2))