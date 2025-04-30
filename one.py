class books():
    def __init__(self):
        self.author = ""
        self.title = ""
        self.price = 0
        self.Books = {}
        
    def Add(self):
        self.title = input("Enter the name of the book you add    \n")
        self.author = input("Enter the Author of the book you add    \n")
        self.price = float(input("Enter the listing price of the book    \n"))
        self.Books[self.title] = {'author': self.author, 'price': self.price}
       
        print("You have added", self.title)
        print(self.Books)

    def Minus(self):
        self.title = input("Enter the name of the book you remove    \n")
        try:
            str(self.title)
            if self.title in self.Books:
               del self.Books[self.title]
               print("the remaining books:", self.title)
        except:
            print("Please enter a book title")

    def showbook(self):
        for x in self.Books:
            print(x)
            print(self.Books[x]["author"])
            print(self.Books[x]["price"])

