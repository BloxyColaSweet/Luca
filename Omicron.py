# Import typing to support type annotations for the class and method signatures.  
import typing  

# Import the project utility module required by the application context.  
import Utils  

# Import support for regular expressions.
import re

# Define the Omicron class, which stores an intrinsic value that is constrained to a type.  
class Omicron:  

	# Document the Omicron class as a typed value wrapper.
	"""Container for a typed intrinsic value."""  

	# Set the default intrinsic type for instances that do not specify one.  
	Omicronic_IntrinsicType: type = typing.Any  

	# Set the regular expression default.
	LexicalAnalysis_LexicalRegexes: list[str] = []

	# Set the token for lexical regex default.
	LexicalAnalysis_TokensForLexicalRegex: type['Omicron'] = None

	# Set the token-lexeme regex pairs default.
	LexicalAnalysis_TokenLexemeRegexPairs: dict[str, 'Omicron'] = None

	# Set the lexical candidates default.
	LexicalAnalysis_LexicalCandidates: dict[type['Omicron'], type['Omicron']] = dict()

	# Initialize a new Omicron instance with an optional intrinsic type and initial value.  
	def __init__(  
				
		# Bind the instance reference for the constructor.  
		self: typing.Self,

		### Intrinsic Data ###
                                                                                                                                                                  
		# Accept an explicit intrinsic type for this instance.  
		Omicronic_IntrinsicType: type = typing.Any,
		
		# Accept an optional initial intrinsic value for the instance.  
		Omicronic_IntrinsicValue = None,  

        ### Connections & Associations ###

		# Accept a list of Omicrons to connect to.
		Omicronic_Connections: list['Omicron'] = [],

		### Lexical Analysis ###                                                                    

		# Sets the LexicalRegex when it goes through Lexical Analysis
		LexicalAnalysis_LexicalRegexes: list[str] = [],

		# Sets the token that corresponds to the lexical regex pattern/s.
		LexicalAnalysis_TokensForLexicalRegex: type['Omicron'] = None,

		# Sets the LoadedPrelexical
		LexicalAnalysis_StringSequenceLoadedPrelexical: str = "",

		# Sets the lexical candidates
	 	LexicalAnalysis_LexicalCandidates: dict[type['Omicron'], type['Omicron']] = dict(),

		### Lexical Objects ###

		# Sets the assigned stream position in the lexical streams
		LexicalObjects_AssignedLexicalStreamPosition: int = 0,

		# Sets the regex that has been captured
		LexicalObjects_AssignedLexicalRegexCaptured: str = "",

		# Sets the subtokens for the token group captured
		LexicalObjects_AssignedLexicalSubtokens: list['Omicron'] = [],

		# Sets the subtokens for the token group captured
		LexicalObjects_AssignedInheritedPosition: int = None,

		# Complete the constructor signature.
	):
				
		# Document the constructor behavior.
		"""Create an Omicron instance with an optional type and value."""  

		# If a concrete intrinsic type was supplied, use it for this instance.  
		if Omicronic_IntrinsicType != typing.Any: 

			# Store the provided intrinsic type on the instance.  
			self.Omicronic_IntrinsicType = Omicronic_IntrinsicType 

			# If no custom type was supplied, fall back to the class default.
		else:  

			# Restore the class-level intrinsic type for this instance.  
			self.Omicronic_IntrinsicType = self.__class__.Omicronic_IntrinsicType  

		# If a concrete LexicalRegex was supplied, use it for this instance.  
		if LexicalAnalysis_LexicalRegexes != []: 

			# Store the provided LexicalRegex on the instance.  
			self.LexicalAnalysis_LexicalRegexes = LexicalAnalysis_LexicalRegexes 

			# If no LexicalRegex was supplied, fall back to the class default.
		else:  

			# Restore the class-level LexicalRegex for this instance.  
			self.LexicalAnalysis_LexicalRegexes = self.__class__.LexicalAnalysis_LexicalRegexes  

		# If a concrete TokensForLexicalRegex was supplied, use it for this instance.  
		if LexicalAnalysis_TokensForLexicalRegex != None: 

			# Store the provided TokensForLexicalRegex on the instance.  
			self.LexicalAnalysis_TokensForLexicalRegex = LexicalAnalysis_TokensForLexicalRegex 

			# If no TokensForLexicalRegex was supplied, fall back to the class default.
		else:  

			# Restore the class-level LexicalRegex for this instance.  
			self.LexicalAnalysis_TokensForLexicalRegex = self.__class__.LexicalAnalysis_TokensForLexicalRegex    

		# If a concrete LexicalAnalysis_LexicalCandidates was supplied, use it for this instance.  
		if LexicalAnalysis_LexicalCandidates != dict(): 

			# Store the provided LexicalAnalysis_LexicalCandidates on the instance.  
			self.LexicalAnalysis_LexicalCandidates = LexicalAnalysis_LexicalCandidates 

			# If no LexicalAnalysis_LexicalCandidates was supplied, fall back to the class default.
		else:  

			# Restore the class-level LexicalAnalysis_LexicalCandidates for this instance.  
			self.LexicalAnalysis_LexicalCandidates = self.__class__.LexicalAnalysis_LexicalCandidates

		# Save the provided intrinsic value on the instance.  
		self.Omicronic_IntrinsicValue = Omicronic_IntrinsicValue  

		# Save the provided connections on the instance.
		self.Omicronic_Connections = Omicronic_Connections
		
		# Save the loaded prelexical stream on the instance.
		self.LexicalAnalysis_StringSequenceLoadedPrelexical = LexicalAnalysis_StringSequenceLoadedPrelexical

		# Save the assigned lexical stream position on the instance.
		self.LexicalObjects_AssignedLexicalStreamPosition = LexicalObjects_AssignedLexicalStreamPosition

		# Save the lexical regex captured on the instance
		self.LexicalObjects_AssignedLexicalRegexCaptured = LexicalObjects_AssignedLexicalRegexCaptured

		# Save a future lexical string sequence stream on the instance
		self.LexicalAnalysis_LexicalTokenLexemeSequence: list['Omicron'] = []

		#
		self.LexicalObjects_AssignedLexicalSubtokens = LexicalObjects_AssignedLexicalSubtokens

		#
		self.LexicalObjects_AssignedInheritedPosition = LexicalObjects_AssignedInheritedPosition

	# Set the intrinsic value only if it matches the configured type.  
	def SetIntrinsicValue(self, valueSet):  

		# Document the validation behavior of the setter.
		"""Assign a value only when it matches the declared intrinsic type."""  
		
		# Ensure the supplied value matches the configured type exactly.  
		if type(valueSet) != self.Omicronic_IntrinsicType: 

			# Raise a type error describing the required intrinsic type.  
			raise TypeError(f"The value to set the intrinsic value must be {self.Omicronic_IntrinsicType}") 
		
		# Store the validated value on the instance.  
		self.Omicronic_IntrinsicValue = valueSet 

	# Connect another Omicron to this Omicron into the Connections list.
	def ConnectToward(self, theOmicron: 'Omicron'):

		# Document the validation behavior of the setter.
		"""Connects this Omicron to another Omicron."""  

		# Checks if theOmicron is not an instance of an Omicron or its subclasses.
		if not isinstance(theOmicron, Omicron):

			# Raises a TypeError.
			raise TypeError(f"{theOmicron} must be of the Omicron type.")

		# Appends theOmicron into self.Connections list.
		self.Omicronic_Connections.append(theOmicron)

	# Loads an unloaded prelexical string
	def LoadPrelexical(self, prelexical: str):

		# Document this function
		"""Loads an unloaded prelexical string."""

		# Sets the unloaded prelexcical to self.LoadedPrelexical
		self.LexicalAnalysis_StringSequenceLoadedPrelexical = prelexical

	# Defines the method responsible for starting lexical analysis.
	def StartLexicalAnalysis(self):
		# Documents the purpose and behavior of the lexical analysis method.
		"""Analyze the loaded prelexical input and identify substrings matching the configured lexical regexes."""

		# Initializes a list for collecting debug results.
		debugReturningList = []

		# Initializes the starting index for the current substring.
		startingPositionCount = 0

		# Initializes the counter used to calculate the ending index.
		endingPositionCount = 0

		# Stores the total length of the loaded prelexical input.
		lengthOfPrelexical = len(self.LexicalAnalysis_StringSequenceLoadedPrelexical)

		# Iterates over each possible starting position in the input.
		while startingPositionCount <= lengthOfPrelexical:

			# Resets the ending index to the total input length.
			resultantPositionEnd = lengthOfPrelexical

			# Iterates over progressively shorter substrings from the current starting position.
			while resultantPositionEnd > startingPositionCount:

				# Extracts the substring between the current starting and ending indices.
				focusedString = self.LexicalAnalysis_StringSequenceLoadedPrelexical[startingPositionCount:resultantPositionEnd]

				# Leaves the optional debug-result collection disabled.
				# debugReturningList.append(focusedString)

				if self.LexicalAnalysis_TokenLexemeRegexPairs != None:
					self.LexicalAnalysis_LexicalRegexes = list(self.LexicalAnalysis_TokenLexemeRegexPairs.keys())

				# Prints the configured lexical regular expressions for debugging.
				print(self.LexicalAnalysis_LexicalRegexes)

				# Checks each lexical candidate
				for eachLexicalCandidate in self.LexicalAnalysis_LexicalCandidates.keys():

					# 
					currentCandidate = eachLexicalCandidate()

					#
					currentCandidate.LoadPrelexical(focusedString)

					#
					currentCandidate.StartLexicalAnalysis()

					#
					currentCandidate.LexicalObjects_AssignedLexicalStreamPosition = startingPositionCount

					#
					currentCandidate.LexicalObjects_AssignedLexicalRegexCaptured = focusedString

					#
					if currentCandidate.CheckForTokens():

						#
						self.LexicalAnalysis_LexicalTokenLexemeSequence.append(
							self.LexicalAnalysis_LexicalCandidates[eachLexicalCandidate](
								LexicalObjects_AssignedInheritedPosition = startingPositionCount,
								LexicalObjects_AssignedLexicalSubtokens = currentCandidate.LexicalAnalysis_LexicalTokenLexemeSequence,
							)
						)

				# Checks the current substring against each configured lexical regular expression.
				for eachRegex in self.LexicalAnalysis_LexicalRegexes:

					# Attempts to match the entire substring against the current regular expression.
					regularExpressionMatchObject = re.fullmatch(eachRegex, focusedString)

					# Leaves a location for additional regular-expression debugging output.
					# print debug here

					# Checks whether the regular expression matched the entire substring.
					if regularExpressionMatchObject:

						# Prints a message indicating that a matching substring was found.
						print('appended')

						if self.LexicalAnalysis_TokenLexemeRegexPairs != None:
							
							# Appends a token representing the matched substring to the lexical sequence.
							self.LexicalAnalysis_LexicalTokenLexemeSequence.append(

								# Constructs a lexical token with the starting position and matched substring.
								self.LexicalAnalysis_TokenLexemeRegexPairs[eachRegex](

									# Assigns the substring's starting index to the token.
									LexicalObjects_AssignedLexicalStreamPosition=startingPositionCount,

									# Assigns the matched substring to the token.
									LexicalObjects_AssignedLexicalRegexCaptured=focusedString,
								)
							)

						else:
							
							# Appends a token representing the matched substring to the lexical sequence.
							self.LexicalAnalysis_LexicalTokenLexemeSequence.append(

								# Constructs a lexical token with the starting position and matched substring.
								self.LexicalAnalysis_TokensForLexicalRegex(

									# Assigns the substring's starting index to the token.
									LexicalObjects_AssignedLexicalStreamPosition=startingPositionCount,

									# Assigns the matched substring to the token.
									LexicalObjects_AssignedLexicalRegexCaptured=focusedString,
								)
							)

				# Increments the ending-position counter to shorten the next substring.
				endingPositionCount += 1

				# Calculates the next ending index by subtracting the counter from the input length.
				resultantPositionEnd = lengthOfPrelexical - endingPositionCount

			# Executes when the inner while loop terminates without encountering break.
			else:

				# Leaves a location for additional inner-loop debugging output.
				# print debug here
				pass

			# Resets the ending-position counter before processing the next starting position.
			endingPositionCount = 0

			# Advances the starting index to the next position in the input.
			startingPositionCount += 1

		# Executes when the outer while loop terminates without encountering break.
		else:

			# Leaves a location for additional outer-loop debugging output.
			# print debug here
			pass

		# Leaves a location for final debugging output.
		# print debug here

		# Returns the debug-result list, which is currently not populated by this method.
		return debugReturningList

	# Defines the method responsible for representing a lexical token as a string.
	def ReprAsLexemeToken(self):
		# Documents the purpose and output of the token representation method.
		"""Return a string containing the token class name, assigned stream position, and captured lexeme."""

		# Formats the token's class name, assigned position, and captured lexeme into a string.
		return "{}({}, {})".format(
			self.__class__.__name__,
			self.LexicalObjects_AssignedLexicalStreamPosition,
			repr(self.LexicalObjects_AssignedLexicalRegexCaptured)
		)

	#
	def ReprLexemeObject(self):
		

	#
	def CheckForTokens(self):
		print('CheckForTokens!')
		print(self.LexicalAnalysis_LexicalTokenLexemeSequence)
		return (self.LexicalAnalysis_LexicalTokenLexemeSequence != [])