class cat():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + " is eatting.")

class SARcat(cat):
    def __init__(self, name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")


my_cat = SARcat('kitty')
print(my_cat.name + " is a search cat.")
my_cat.eat()
my_cat.search()