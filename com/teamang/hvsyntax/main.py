import json5
import os
from Lexer import Lexer

class SyntaxChecker():

	rootPath = os.getcwd()

	def __init__(self, includeLexerPrefix: bool = True):
		"""
		Initializes the lexer and runs the checker
		"""
		with open(os.path.join(self.rootPath, "resources/tokens.jsonc"), "r") as file:
			tokens = json5.load(file)
			self.lexer = Lexer(tokens, includeLexerPrefix, True).getLexer()

	def runChecker(self, continueRunning: bool = False):
		"""
		Runs the checker and prints the tokens
		"""
		exitCommands = ["exit", "quit", "stop", "end"]

		while True:
			try:
				textInput = input("\n\nEnter some text: ")

				if (textInput.lower() in exitCommands) or (textInput.lower()[0] == "q"):
					break

				tokens = self.lexer.lex(textInput)

				for token in tokens:
					print(token)
			except Exception as e:
				print("\n======= ERROR =======")
				print(e)
				print("=====================\n")
		return


"""
SAMPLE INPUT:

check (myVar == 5) { ary->push(myVar); }

arr<str> ary = ["Hello", "World"];

int x = 1;
"""
checker = SyntaxChecker(False)

checker.runChecker(True)
