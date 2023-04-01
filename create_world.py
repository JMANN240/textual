from room import Room, Door
from player import Player
from item import Key

starting_room = Room("starting room")
closet = Room("closet")
outside = Room("outside")

starting_room_closet_door = Door(
    starting_room, "to the left",
    closet, "in front of you",
    known=True
)

front_door = Door(
    starting_room, "in front of you",
    outside, "behind you",
    locked=True
)

key = Key("front door key", closet, front_door)

player = Player("JT", starting_room)