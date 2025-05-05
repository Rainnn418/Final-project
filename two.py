from one import books
a = books()
game = True 
while game:
    v = input("Add book -- 1  \nRemove book -- 2  \nShow books you added -- 3  \nCreate a file -- 4  \nOpen your file --  5  \n")

    if v == "1":
        b = a.Add()
    elif v == "2":
        c = a.Minus()
    elif v == "3":
        d = a.showbook()
    elif v == "4":
        e = a.save()
    elif v == "5":
        f = a.load()
    else:
        print("Worry")