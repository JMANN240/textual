from colorama import Fore, Style
import math

class Item:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        owner.inventory.append(self)
    
    def description(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL}"

class UsableItem(Item):
    def __init__(self, name, owner, max_uses=math.inf):
        super().__init__(name, owner)
        self.uses = 0
        self.max_uses = max_uses

class Key(UsableItem):
    def __init__(self, name, owner, door, max_uses=1):
        super().__init__(name, owner, max_uses)
        self.door = door
    
    def use(self, player):
        if self.door in player.location.doors:
            if self.door.locked:
                self.door.locked = False
                print(f"You unlock the {self.door.description(player)}.")
                self.uses += 1
                if self.uses == self.max_uses:
                    self.owner.inventory = [item for item in self.owner.inventory if item is not self]
            else:
                print(f"The {self.door.description(player)} is not locked.")
        else:
            print("There is no door for this key to unlock.")