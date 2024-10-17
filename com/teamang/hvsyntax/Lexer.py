from rply import LexerGenerator
import re

WHITESPACE = r"\s+"

class Lexer():
	def __init__(self, tokens: dict, includeLexerPrefix: bool = True, debug: bool = False):
		if (type(tokens) != dict):
			raise Exception("Tokens must be a dictionary")

		self.lexer = LexerGenerator()
		self.tokens = tokens
		self.includeLexerPrefix = includeLexerPrefix
		self.debug = debug

	def addTokens(self):
		for tokenKey in self.tokens:
			try:
				altKey = tokenKey
				if (not self.includeLexerPrefix):
					altKey = tokenKey.split(" - ")[1]

				if (self.debug):
					print(f"Adding token {self.tokens[tokenKey]} as {altKey}")
				self.lexer.add(altKey, re.compile(self.tokens[tokenKey]))
			except Exception as e:
				print(f"Error adding token {self.tokens[tokenKey]}: {e}")

		self.lexer.ignore(WHITESPACE)

	def getLexer(self):
		self.addTokens()
		return self.lexer.build()
