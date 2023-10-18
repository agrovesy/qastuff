
class Birds:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def eat(self):
        print(f"{self.name} is tweeting")
        
    def __str__(self):
        return f"{self.name} {self.species}"
    
class Owl(Birds):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
        
class Dodo(Birds):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
        
 #   def __str__(self):
 #       return f"{self.name} {self.species} {self.breed}"
    
    
my_bird1 = Birds("wiggles", "cat")   
 
print(my_bird1) 

my_bird2 = Owl("wiggles", "cat", "flying")   
 
print(my_bird2) 

my_bird3 = Dodo("wiggles", "cat", "flying")   
 
print(my_bird3) 