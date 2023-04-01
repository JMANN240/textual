from words import *
from create_world import *
from util import fuzzy_in

def process_command(command):
	split_command = command.split(" ")
	split_command_length = len(split_command)
	if split_command_length == 1:
		return split_command[0], None
	else:
		return split_command[0], " ".join(split_command[1:])

def turn():
	player.describe()
	command = input("> ")
	verb, noun = process_command(command)
	fuzzy_verb = fuzzy_in(verbs, verb)
	if fuzzy_verb in transitive_verbs:
		if noun is None:
			print(f"{verb} what?")
		else:
			action = transitive_verbs[fuzzy_verb]
			action(player, noun)
	elif fuzzy_verb in intransitive_verbs:
		action = intransitive_verbs[fuzzy_verb]
		action(player)
	else:
		print(f"You don't know how to {command}.")
	print()

while True:
	turn()