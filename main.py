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
