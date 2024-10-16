from Lexer import Lexer

textInput = input("Enter some text: ")

lexer = Lexer().getLexer()
tokens = lexer.lex(textInput)

for token in tokens:
	print(token)