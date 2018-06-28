#!/usr/bin/env python
"""
     v22 = 
	v14 + v15 == 205
     && v13 + v16 == 201
     && v11 + v14 + v15 == 314
     && v13 + v16 + v12 + v17 == 367  
     && Buffer + v9 == 194
     && v17 + v16 + v15 + v14 + v13 + v12 + v11 + v10 + v9 + Buffer == 923;

	char[8] = 85
	char[0] + char[2] = 128
	char[4] - char[7] = -50
	char[6] + char[9] = 219


	Congratulations! You guessed the right password, but the message you see is wrong.
	Try to look for some unreferenced data, that can be decrypted the same way as this text.




"""

def Hint_Password():
	from z3 import Int, Solver

	Buffer =    Int('Buffer')
	v9     =    Int('v9')
	v10    =    Int('v10')
	v11    =    Int('v11')
	v12    =    Int('v12')
	v13    =    Int('v13')
	v14    =    Int('v14')
	v15    =    Int('v15')
	v16    =    Int('v16')
	v17    =    Int('v17')

	s = Solver()
	
	s.add(Buffer > 31, Buffer < 127)
	s.add(v9 > 31, v9 < 127)
	s.add(v10 > 31, v10 < 127)
	s.add(v11 > 31, v11 < 127)
	s.add(v12 > 31, v12 < 127)
	s.add(v13 > 31, v13 < 127)
	s.add(v14 > 31, v14 < 127)
	s.add(v15 > 31, v15 < 127)
	s.add(v16 > 31, v16 < 127)
	s.add(v17 > 31, v17 < 127)

	s.add(v14 + v15 == 205)
	s.add(v13 + v16 == 201)
	s.add(v11 + v14 + v15 == 314)
	s.add(v13 + v16 + v12 + v17 == 367)
	s.add(Buffer + v9 == 194)
	s.add(v17 + v16 + v15 + v14 + v13 + v12 + v11 + v10 + v9 + Buffer == 923)

	return "Status : %s \nPassword = %s" %  (
			s.check(), 
			chr(s.model()[Buffer].as_long()) + chr(s.model()[v9].as_long())  + 
			chr(s.model()[v10].as_long())    + chr(s.model()[v11].as_long()) + 
			chr(s.model()[v12].as_long())    + chr(s.model()[v13].as_long()) + 
			chr(s.model()[v14].as_long())    + chr(s.model()[v15].as_long()) + 
			chr(s.model()[v16].as_long())    + chr(s.model()[v17].as_long())  
						) 

	
def Password():
	from z3 import Int, Solver

	Buffer =    Int('Buffer')
	v9     =    Int('v9')
	v10    =    Int('v10')
	v11    =    Int('v11')
	v12    =    Int('v12')
	v13    =    Int('v13')
	v14    =    Int('v14')
	v15    =    Int('v15')
	v16    =    Int('v16')
	v17    =    Int('v17')

	s = Solver()

	s.add(v14 + v15 == 205)
	s.add(v13 + v16 == 201)
	s.add(v11 + v14 + v15 == 314)
	s.add(v13 + v16 + v12 + v17 == 367)
	s.add(Buffer + v9 == 194)
	s.add(v17 + v16 + v15 + v14 + v13 + v12 + v11 + v10 + v9 + Buffer == 923)
	s.add(v16 == 85)
	s.add(Buffer + v10 == 128)
	s.add(v12 - v15 == -50)
	s.add(v14 + v17 == 219)
	
	return "Status : %s \nPassword = %s" %  (
			s.check(), 
			chr(s.model()[Buffer].as_long()) + chr(s.model()[v9].as_long())  + 
			chr(s.model()[v10].as_long())    + chr(s.model()[v11].as_long()) + 
			chr(s.model()[v12].as_long())    + chr(s.model()[v13].as_long()) + 
			chr(s.model()[v14].as_long())    + chr(s.model()[v15].as_long()) + 
			chr(s.model()[v16].as_long())    + chr(s.model()[v17].as_long())  
						) 
	
print Hint_Password()
print Password()










