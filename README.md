# Textual

## A Framework for Text-Based Games

### Setup

Python is a pre-requisite for this project. Install it however you want and make sure that it is in your path. Setup instructions are as follows.

0. (Optional) Setup a virtual environment with `python -m venv env` and activate it with `source env/bin/activate`.

1. Install the required packages with `pip install -r requirements.txt`.

2. Run `main.py` and play!

### Components

- **Player**: Always needed. Represents the player. Has an inventory and a location.
- **Room**: Represents different areas in the world. At least one room is required to start the player in. Has an inventory of items found in the room.
- **Door**: Relates room to each other. Can be locked and unknown.
- **Key**: Unlocks a door. One time use by default.

Alter `create_world.py` to make different worlds using these components.