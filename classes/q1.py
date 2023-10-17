class cat():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is standing.")


my_cat = cat('kitty')
print(my_cat.name + " is a great cat!")
my_cat.sit()