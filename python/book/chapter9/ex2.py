
answer = input("How old are you: ")
with open("answer.txt", "a") as f:
    f.write(answer + "\n")

