import os
class bcolors:
     RED = '\033[91m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     BLUE = '\033[94m'
     PURPLE = '\033[95m'
     ENDC = '\033[0m'
     
class books():
    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = 0
        self.Books = {}
        
    def Add(self):
        try:
            self.title = input(bcolors.BLUE + "Enter the name of the book you add    \n" + bcolors.ENDC)
            self.author = input(bcolors.BLUE + "Enter the author of the book you add    \n" + bcolors.ENDC)
            self.price = float(input(bcolors.BLUE + "Enter the listing price of the book    \n" + bcolors.ENDC))
            self.Books[self.title] = {'author': self.author, 'price': self.price}
       
            print(bcolors.GREEN + "You have added", self.title + bcolors.ENDC)
            print(self.Books)
        except:
            print(bcolors.RED + "Please enter the correct price." + bcolors.ENDC)

    def Minus(self):
        self.title = input(bcolors.BLUE + "Enter the name of the book you remove    \n" + bcolors.ENDC)
        try:
            str(self.title)
            if self.title in self.Books:
               del self.Books[self.title]
               print(bcolors.GREEN + "The remaining books:", self.title + bcolors.ENDC)
            else:
                print(bcolors.RED + "Please enter a correct book title" + bcolors.ENDC)
        except:
            print(bcolors.RED + "Please enter a correct book title" + bcolors.ENDC)

    def showbook(self):
        if not self.Books:
           print(bcolors.RED + "No books available." + bcolors.ENDC)

        for x in self.Books:
            print(bcolors.YELLOW + x + bcolors.ENDC)
            print(bcolors.PURPLE + "Author: ", self.Books[x]["author"] + bcolors.ENDC)
            print(bcolors.PURPLE + "Price: ", str(self.Books[x]["price"]) + bcolors.ENDC)

    def save(self):
        name = input(bcolors.BLUE + "What do you want the file to be named?" + bcolors.ENDC)
        with open(name, "w") as f:    
            for x in self.Books:
                f.write(f"Title: {x}\nAuthor: {self.Books[x]['author']}\nPrice: {self.Books[x]['price']}\n\n")
            print(bcolors.GREEN + f"All books saved to {name}" + bcolors.ENDC)

    def load(self):
        filename = input(bcolors.BLUE + "Which file do you want to load?" + bcolors.ENDC)
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for x in f:
                    strs = x.strip().split(",")
                    if len(strs) == 3:
                        self.title = strs[0]
                        self.author = strs[1]
                        self.price = float(strs[2])
                    self.Books[self.title] = {"author": self.author, "price": self.price}
            print(bcolors.GREEN + "File loaded successfully!" + bcolors.ENDC)
        else:
            print(bcolors.RED + "The file does not exist" + bcolors.ENDC)

    def delete(self):
        filename = input(bcolors.BLUE + "Which file do you want to delete?" + bcolors.ENDC)
        if os.path.exists(filename):
           os.remove(filename)
           print(bcolors.GREEN + "You have deleted." + bcolors.ENDC)
        else:
            print(bcolors.RED + "The file does not exist" + bcolors.ENDC)
            