from colorama import Fore, Style

class Room:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.doors = []
    
    def description(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL}"
        

class Door:
    def __init__(self, room_one, room_one_location, room_two, room_two_location, locked=False, known=False):
        self.rooms = (room_one, room_two)
        self.locations = (room_one_location, room_two_location)
        room_one.doors.append(self)
        room_two.doors.append(self)
        self.locked = locked
        self.known = known
    
    def other(self, current_room):
        return [room for room in self.rooms if room is not current_room][0]
    
    def room_location(self, test_room):
        return [location for room, location in zip(self.rooms, self.locations) if room is test_room][0]
    
    def description(self, player):
        room = player.location
        door_location = self.room_location(room)
        locked_string = ""
        if self.locked:
            locked_string = "locked "
        return f"{locked_string}door {Fore.GREEN}{door_location}{Style.RESET_ALL}"

    def known_string(self, player):
        return "You don't know where it goes." if not self.known else f"It leads to {self.other(player.location).description()}."