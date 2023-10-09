# Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like
# ["Where now?", "Who now?", "When now?"].

list = "Where now? Who now? When now?".split("?")
del list[-1]

list2 = []
for i in list:
    list2.append(i.strip() + "?")

print(list2)
