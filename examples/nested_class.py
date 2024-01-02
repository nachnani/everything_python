class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self,name,species):
        new_animal = self.Animal(name,species)
        self.animals.append(new_animal)



    class Animal:

        def __init__(self,name,species):
            self.name = name
            self.species = species

        def display_info(self):
            print(f"Name: {self.name}, Species: {self.species} " )


#creating a zoo
my_zoo = Zoo()

#add animals to zoo
my_zoo.add_animal("Lion","Mammal")
my_zoo.add_animal("Eagle","Bird")
my_zoo.add_animal("Crocodile","Reptile")

for animal in my_zoo.animals:
    animal.display_info()
