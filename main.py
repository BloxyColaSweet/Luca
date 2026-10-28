from Omicron import *

class Integer(Omicron):
	Omicronic_IntrinsicType = int

x =  Integer           ()
x .  SetIntrinsicValue (23)
y =  Integer		   ()
y .  SetIntrinsicValue (78)
z =  Integer		   ()
z .  SetIntrinsicValue (29)
a =  Integer           ()
a .  ConnectToward     (x)
a .  ConnectToward     (y)
a .  ConnectToward     (z)

class Numbers(Omicron):
	
	class T_NumberOne		(Omicron): pass
	class T_NumberTwo		(Omicron): pass
	class T_NumberThree		(Omicron): pass
	class T_NumberFour		(Omicron): pass
	class T_NumberFive		(Omicron): pass
	class T_NumberSix		(Omicron): pass
	class T_NumberSeven		(Omicron): pass
	class T_NumberEight		(Omicron): pass
	class T_NumberNine		(Omicron): pass
	class T_NumberZero		(Omicron): pass

	class Chuckins(Omicron):

		class T_ChuckinsTen(Omicron): pass
		class T_ChuckinsTwelve(Omicron): pass
		class T_ChuckinsEleven(Omicron): pass

		LexicalAnalysis_TokenLexemeRegexPairs = {
			r"10": T_ChuckinsTen,
			r"11": T_ChuckinsEleven,
			r"12": T_ChuckinsTwelve
		}

	class T_Chuckins(Omicron): pass

	LexicalAnalysis_LexicalCandidates = {
		Chuckins: T_Chuckins
	}

	LexicalAnalysis_TokenLexemeRegexPairs = {
		r"0": T_NumberZero,
		r"1": T_NumberOne,
		r"2": T_NumberTwo,
		r"3": T_NumberThree,
		r"4": T_NumberFour,
		r"5": T_NumberFive,
		r"6": T_NumberSix,
		r"7": T_NumberSeven,
		r"8": T_NumberEight,
		r"9": T_NumberNine
	}

x = Numbers()
x.  LoadPrelexical("802710")
x.  StartLexicalAnalysis()
for token in x.LexicalAnalysis_LexicalTokenLexemeSequence:
	print(token.ReprAsLexemeToken())

