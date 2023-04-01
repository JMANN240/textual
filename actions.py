from util import fuzzy_match

def dance(_player):
    print(f"You dance like crazy.")

def grab(player, test_item):
    matching_items = [item for item in player.location.inventory if fuzzy_match(item.name, test_item)]
    if len(matching_items) == 0:
        print(f"There is no {test_item}.")
    else:
        item = matching_items[0]
        item.owner.inventory = [check_item for check_item in item.owner.inventory if check_item is not item]
        item.owner = player
        player.inventory.append(item)
        print(f"You grab the {item.description()}")

def go(player, direction):
    matched_doors = [door for door in player.location.doors if fuzzy_match(door.room_location(player.location), direction)]
    if len(matched_doors) == 0:
        print(f"You can't go {direction}")
    else:
        door = matched_doors[0]
        if door.locked:
            print(f"The door {door.room_location(player.location)} is locked.")
        else:
            other_room = door.other(player.location)
            player.location = other_room
            door.known = True
            print(f"You go {direction}")

def use(player, test_item):
    matching_items = [item for item in player.inventory if fuzzy_match(item.name, test_item)]
    if len(matching_items) == 0:
        print(f"You don't have {test_item}.")
    else:
        item = matching_items[0]
        use_method = getattr(item, 'use')
        if callable(use_method):
            item.use(player)
        else:
            print(f"Can't use {item.description()}")