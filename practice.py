# commenting test123
'''for i in range( 10 ):
	print ( i )
	if i == 4:
		print ( "what?" )
mylist = [ 0, 1, 2, 3, 4]		#I can also comment out here
'''
'''
this is a long comment, kind of like adding notes to your code
you can just keep writing and writin
and when you want to end the comment you just...
'''
'''
for i in range( 10 ):
	print ( i )
	if i != 4: #Read about Boulean variables (T/F) also can use >= or <=
		print ( "what?" )
'''
'''
Can also use this kind of comment to comment out a part of the code that you don't want 
ran with the rest. For example, if I want to run one or the other of the for loops above
I can comment out the one I don't want ran.
'''
'''
i = 0
total = 0
while i < 10:
	total = total + i
	i = i + 1	#This looks like the counters for loops in C++
	print( total )
'''
# This is a mini program that runs a counter through 10 and prints what on the even counts

i = 0
while i < 10:
	if i % 2 == 0:
		print( i )
		print( "what?" )
	i = i +1

'''
# This is the same mini program as above, but now it is printing the odd counts
i = 0
while i < 10:
	if i % 2 != 0:
		print( i )
		print( "what?" )
	i = i +1
'''