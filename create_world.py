from room import Room, Door
from player import Player
from item import Key

# The example layout
# x: locked door
# o: unlocked door
# 'u': player
# F: key

#
#       outside
#
#     +--x--+
#     |     |
# +---+     |
# | F o 'u' |
# +---+-----+
#

# Rooms
starting_room = Room("starting room")
closet = Room("closet")
outside = Room("outside")


# Doors
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


# Items
key = Key("front door key", closet, front_door)

# The player
player = Player("JT", starting_room)