from one import books
class bcolors:
     RED = '\033[91m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     BLUE = '\033[94m'
     PURPLE = '\033[95m'
     ENDC = '\033[0m'

a = books()
game = True 
while game:
    v = input("Add book -- 1  \nRemove book -- 2  \nShow added books -- 3  \nCreate a file -- 4  \nLoad file --  5  \nShow added file --  6  \nDelete file -- 7\n")
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
    elif v == "6":
        g = a.showfile()
    elif v == "7":
        h = a.delete()
    else:
        print(bcolors.RED + "Worry" + bcolors.ENDC)