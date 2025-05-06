class bcolors:
     RED = '\033[91m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     BLUE = '\033[94m'
     PURPLE = '\033[95m'
     ENDC = '\033[0m'
     
class books():
    def __init__(self):
        self.author = ""
        self.title = ""
        self.price = 0
        self.Books = {}
        
    def Add(self):
        self.title = input(bcolors.BLUE + "Enter the name of the book you add    \n" + bcolors.ENDC)
        self.author = input(bcolors.BLUE + "Enter the Author of the book you add    \n" + bcolors.ENDC)
        self.price = float(input(bcolors.BLUE + "Enter the listing price of the book    \n" + bcolors.ENDC))
        self.Books[self.title] = {'author': self.author, 'price': self.price}
       
        print(bcolors.GREEN + "You have added", self.title + bcolors.ENDC)
        print(self.Books)

    def Minus(self):
        self.title = input(bcolors.BLUE + "Enter the name of the book you remove    \n" + bcolors.ENDC)
        try:
            str(self.title)
            if self.title in self.Books:
               del self.Books[self.title]
               print(bcolors.GREEN + "The remaining books:", self.title + bcolors.ENDC)
        except:
            print("Please enter a book title")

    def showbook(self):
        for x in self.Books:
            print(bcolors.YELLOW + x + bcolors.ENDC)
            print(bcolors.PURPLE + "Author: ", self.Books[x]["author"] + bcolors.ENDC)
            print(bcolors.PURPLE + "Price: ", str(self.Books[x]["price"]) + bcolors.ENDC)
    
    def save(self):
        name = input("What do you want the file to be named? ")
        with open(name, "w") as f:    
            f.write(str(self.Books))
            print(bcolors.GREEN + f"《{self.title}》saved to {name}" + bcolors.ENDC)
           
    def load(self):
        filename = input("Which file do you want to open?")
        with open(filename, "r") as f:
             print("Title: ",self.title)
             print("Author: ", self.Books[self.title]["author"])
             print("Price: ", self.Books[self.title]["price"])
