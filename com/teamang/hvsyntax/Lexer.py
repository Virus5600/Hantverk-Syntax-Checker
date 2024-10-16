from rply import ParserGenerator, LexerGenerator

TOKENS = {
	# COMMENTS
	"singleLineComment": r"\#",
	"multiLineCommentStart": r"\#--",
	"multiLineCommentEnd": r"--\#",

	# ACCESS MODIFIERS
	"public": r"shared",
	"private": r"self",
	"protected": r"internal",
	"default": r"grouped",
	"static": r"static",

	# DATA TYPES
	"string": r"str",
	"integer": r"int",
	"float": r"flt",
	"double": r"dbl",
	"boolean": r"bol",

	# OPERATORS
	"addition": r"\+",
	"subtraction": r"-",
	"multiplication": r"\*",
	"division": r"/",
	"modulo": r"%",
	"increment": r"\+\+",
	"decrement": r"--",
	"assignment": r"=",
	"additionAssignment": r"\+=",
	"subtractionAssignment": r"-=",
	"multiplicationAssignment": r"\*=",
	"divisionAssignment": r"/=",
	"moduloAssignment": r"%=",
	"not": r"!",

	# COMPARISON OPERATORS
	"equals": r"==",
	"notEquals": r"!=",
	"lessThan": r"<",
	"greaterThan": r">",
	"lessThanOrEqual": r"<=",
	"greaterThanOrEqual": r">=",
	"strictEquals": r"===",
	"strictNotEquals": r"!==",
	"and": r"&&",
	"or": r"\|\|",

	# KEYWORDS
	## CONDITIONAL ##
	"if": r"check",
	"else": r"otherwise",

	## LOOPS ##
	"for": r"from",
	"while": r"loop",

	## SCOPING ##
	"import": r"use",
	"class": r"template",
	"interface": r"modded",
	"function": r"fn",
	"extends": r"ext",
	"implements": r"mod",
	"return": r"return",
	"break": r"stop",
	"this": r"my",
	"super": r"parent",
	"new": r"new",

	## DATA STRUCTURES ##
	"null": r"null",
	"true": r"true",
	"false": r"false",
	"void": r"void",
	"array": r"arr",
	"dictionary": r"map",
	"number": r"\d+",
	"string": r"[A-z\s\!\#\$\%\&\(\)\*\+\,\-\.\:;\<\=\>\?\@\[\]\^\_\`\{\}\|\~/\\]+",
	"identifier": r"[A-z][A-z0-9_]*",
	"newline": r"\n",
	"whitespace": r"\s+",
	"semicolon": r";",
	"colon": r":",
	"comma": r",",
	"period": r"\.",
	"leftParen": r"\(",
	"rightParen": r"\)",
	"leftCurly": r"{",
	"rightCurly": r"}",
	"leftSquare": r"\[",
	"rightSquare": r"\]",
	"doubleQuote": r"\"",
	"singleQuote": r"\'",
	"backTick": r"`",
	"annotationIdent": r"::",
}

class Lexer():
	def __init__(self):
		self.lexer = LexerGenerator()
		
	def addTokens(self):
		for tokenKey in TOKENS:
			self.lexer.add(tokenKey, TOKENS[tokenKey])

		self.lexer.ignore(TOKENS["whitespace"])

	def getLexer(self):
		self.addTokens()
		return self.lexer.build()