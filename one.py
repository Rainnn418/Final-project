class books():
    def __init__(self):
        self.name = "XU"
        self.title = "Welcome"
        
    def Add(self):
        self.title = input("what book would you like to add?")
        print("You have added", self.title)