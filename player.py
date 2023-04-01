class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.inventory = []
        self.location = starting_location
    
    def describe(self):
        print(f"You are in {self.location.description()}.")
        for door in self.location.doors:
            print(f"There is a {door.description(self)}. {door.known_string(self)}")
        for item in self.location.inventory:
            print(f"There is a {item.description()} in the roon.")
        for item in self.inventory:
            print(f"You have {item.description()}.")