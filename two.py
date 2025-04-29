from one import books
a = books()
game = True 
while game:
    v = input("Would you like to add a book? (yes or no)")

    if v == "yes":
        a.Add()
    elif v == "no":
        a.Minus()
    else:
        print("Please enter 'yes' or 'no'.")
