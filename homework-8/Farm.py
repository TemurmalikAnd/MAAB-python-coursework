class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        print(f"{self.name} is eating {food}. 🍽️")

    def sleep(self):
        print(f"{self.name} is sleeping peacefully 😴")

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this!")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}, Weight: {self.weight}kg"

class Cow(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.sound = "Moo"

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def produce_milk(self):
        print(f"{self.name} is giving milk 🥛.")

class Chicken(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.sound = "Cluck"

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def lay_eggs(self):
        print(f"{self.name} laid an egg 🥚.")

class Pig(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.sound = "Oink"

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in the mud 🐷.")

# ---------- Farm Simulation ----------
def run_farm_simulation():
    print("Welcome to Happy Farm 🐓🐄🐖\n" + "-" * 40)

    # Create animal instances
    bessie = Cow("Gertruda", 5, 600)
    clucky = Chicken("O'rdak", 2, 2)
    porky = Pig("Cho'chqa", 3, 120)

    # Add to farm list
    farm_animals = [bessie, clucky, porky]

    # Display info & behaviors
    for animal in farm_animals:
        print(animal)
        animal.make_sound()
        animal.eat("grass" if isinstance(animal, Cow) else "corn")
        animal.sleep()

        # Specific behaviors
        if isinstance(animal, Cow):
            animal.produce_milk()
        elif isinstance(animal, Chicken):
            animal.lay_eggs()
        elif isinstance(animal, Pig):
            animal.roll_in_mud()

        print("-" * 40)

if __name__ == "__main__":
    run_farm_simulation()
