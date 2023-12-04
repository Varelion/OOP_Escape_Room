class GameObject:
	# Note: fields can be created with only the initializer function.
	name = ""
	appearance = ""
	feel = ""
	smell = ""

# Every initializer needs to have this syntax, of __ and init and a 'self' parameter.
	def __init__(self, name, appearance, feel, smell):
		self.name = name
		self.appearance = appearance
		self.feel = feel
		self.smell = smell

	def look(self):
		# the 'f' at the beginning of the string denotes that it is a formater
		# string, and {} allow for string literals.
		return f"You look the {self.name}. \n {self.appearance}\n"

	def feel(self):
		return f"You feel the {self.name}. \n {self.feel}\n"

	def sniff(self):
		return f"You sniff the {self.name}. \n {self.smell}\n"

# Here we create an object from the class, feeding in the parameters, and then printing their fields' values.
game_object = GameObject("Object_Name", "Some_Appearance", "Some_Feel", "Some_Smell")
print(game_object.name)
print(game_object.sniff())


# Room initializer

class Room:
	escape_code = 0
	game_objects = []

	def __init__(self, escape_code, game_objects):
		self.escape_code = escape_code
		self.game_objects = game_objects

	def check_code(self, code):
		# if self.code == code:
		# 	return True
		# if self.code != code:
		# 	return False
		return self.code == code

	def get_game_object_names(self, objects_in_game):
		names = []
		for object in objects_in_game:
			names.append(object.name)
		return names

class Game:
	def __init__(self, room):
		self.attempts = 0
		Objects = self.create_objects
		self.room = Room(111,[])

	def create_objects(self):
        return [
          GameObject(
            "Sweater",
            "It's a blue sweater that had the number 12 switched on it.",
            "Someone has unstitched the second number, leaving only the 1.",
            "The sweater smells of laundry detergent."),
          GameObject(
            "Chair",
            "It's a wooden chair with only 3 legs.",
            "Someone had deliberately snapped off one of the legs.",
            "It smells like old wood."),
          GameObject(
            "Journal",
            "The final entry states that time should be hours then minutes then seconds (H-M-S).",
            "The cover is worn and several pages are missing.",
            "It smells like musty leather."),
          GameObject(
            "Bowl of soup",
            "It appears to be tomato soup.",
            "It has cooled down to room temperature.",
            "You detect 7 different herbs and spices."),
          GameObject(
            "Clock",
            "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
            "The battery compartment is open and empty.",
            "It smells of plastic."),
        ]
