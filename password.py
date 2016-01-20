import sublime, sublime_plugin
from random import randrange
class PatternPasswordCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_input_panel("Input Pattern", "Cvcvcv99", self.generate_pass, None, None)

	def generate_pass(self, user_input):
		chars = "!@#$%^&*_-+=|/?:;<>~"
		letter_upper = "BCDFGHJKLMNPQRSTVWXYZ"
		letter_lower = "bcdfghjklmnpqrstvwxyz"
		vowels_upper = "AEIOU"
		vowels_lower = "aeiou"
		digits = "0123456789"
		result =""
		for char in user_input:
			if char == "/#":
				flag = randrange(0, len(chars))
				result += chars[flag]
			elif char == "c":
				flag = randrange(0, len(letter_lower))
				result += letter_lower[flag]
			elif char == "C":
				flag = randrange(0, len(letter_upper))
				result += letter_upper[flag]
			elif char == "v":
				flag = randrange(0, len(vowels_lower))
				result += vowels_lower[flag]
			elif char == "V":
				flag = randrange(0, len(vowels_upper))
				result += vowels_upper[flag]
			elif char == "9":
				flag = randrange(0, len(digits))
				result += digits[flag]
			else:
				result += char
		for region in self.view.sel():
			self.view.replace(self.view.begin_edit(), region, result)