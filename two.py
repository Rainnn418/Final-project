from one import books
a = books()
game = True 
while game:
    v = input("Would you like to add a book? (yes or no)")

    if v == "yes":
        b = a.Add()
    elif v == "no":
        c = a.Minus()
    elif v == "y":
        d = a.showbook()
    else:
        print("Please enter 'yes' or 'no'.")
