# Create the Car class
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


    def show(self):
        print(self.brand)
        print(self.year)

# Create an object
c1 = Car("Toyota", 2020)
# Call the show method
c1.show ()

# ============================================
# KEY CONCEPTS EXPLAINED
# ============================================

# 1. CLASS (Car)
#    - A blueprint or template for creating objects
#    - Defines what attributes (data) and methods (functions) objects will have
#    - Think of it like a recipe for a car

# 2. __init__ (Constructor/Initializer)
#    - Special method that runs automatically when you create a new object
#    - "self" refers to the object being created
#    - self.brand and self.year are ATTRIBUTES - they store data
#    - In this example, it takes 2 parameters: brand and year

# 3. OBJECT (c1)
#    - An instance of the Car class (a real car created from the blueprint)
#    - Car("Toyota", 2020) creates a new object by calling the class
#    - This calls __init__ and sets brand="Toyota" and year=2020

# 4. ATTRIBUTES
#    - self.brand and self.year are attributes (data stored on the object)
#    - Each car object has its own brand and year separate from other cars
#    - Access them with: c1.brand or c1.year

# 5. METHODS
#    - show() is a method (a function inside a class)
#    - Methods let objects DO things or display information
#    - Called with: object_name.method_name()

# 6. HOW IT WORKS STEP-BY-STEP:
#    Step 1: class Car defines the blueprint
#    Step 2: c1 = Car("Toyota", 2020) creates a car object
#    Step 3: __init__ runs automatically, setting brand and year
#    Step 4: c1.show() is called, which prints the brand and year

# 7. WHY USE CLASSES?
#    - Organize related data and functions together
#    - Avoid repeating code (instead of separate variables, use one object)
#    - Easy to create multiple similar objects
#    - Makes code cleaner and more maintainable

# GAME BACKEND EXAMPLE:
# Instead of separate variables for each player:
#   player1_name = "Alice"
#   player1_level = 5
#   player1_health = 100
#   player2_name = "Bob"
#   player2_level = 3
# You'd have a Player class and create objects:
#   player1 = Player("Alice", 5, 100)
#   player2 = Player("Bob", 3, 100)
# Much cleaner! And you can call methods like:
#   player1.take_damage(10)
#   player2.level_up()

