# Write a program with an infinite loop (with the option to type q to quit) and a list of numbers. Each time
# through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly.



while True:
    nums = [2, 55, 66, 30]
    user = input("Guess a number: ")
    if user == "q":
        break
    else:
        try:
            if int(user) in nums:
                print("You guessed correctly!")
            else:
                print("You guessed incorrectly!")
        except (TypeError, ValueError):
            print("Invalid input!")




    