# Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the
# characters before the comma.

x = "It was a bright cold day in April, and the clocks were striking thirteen."
index = x.index(",")
y = x[0:index]
print(y)

