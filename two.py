from one import books
a = books()
print(a.name, a.title)

v = input("would you like to add a book? (yes or no)")
if v == "yes":
    b = a.Add()
elif v == "no":
    print("gun")