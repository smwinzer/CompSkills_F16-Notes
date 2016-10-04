#Python practice from 9/15 class

nucleotides = ["A" , "C" , "G" , "T" , "N" , "Y" , "U"]

goodReads = nucleotides[0:4] #Indexing/taking a slice of a list

goodReads = nucleotides[:4] #start with beginning of list

ambiguousReads = nucleotides[4:] #Go through end of list

nucleotides[:-2]#Give the list minus the last two entries

nucleotides[::2] #Begin at the beginning and go through the end, skip every other entry

nucleotides[::-1] #Begin at the beginning and go through the end, but go backwards

s == s[::-1] #Is the string s a palindrome?

t[::-1].replace('o','X')

t = "foobar"
t[t.find('b'):] #output 'bar'

#to copy a variable into a second variable you cannot just set them equal
x = y[:] #You have to take a slice of the whole variable and store it as the second

#How to change the type of an object using casting
list(stringname) #changes a string named stringname into a list
str(listname) #changes a list named listname into a string

x.sort(reverse=True) #sorts the list x in reverse order
x.sort() #sorts the list x in regular order

x = "this is my integer %d, string %s, real %f" % (1,'foobar',2.34)

#How to define a function
def functionName( ):
		#double tab in and enter function information
		#create object inputs for a function by listing them within the function ()
		
def countNucs(s,n): # This function can be written to count nucleotide n in sequence s

countNucs?? #Gives a long description of the function countNucs including long comments

#Index positions start with 0 not 1!!

for n in range(5):
    print(nucleotides[n])
    #range is a useful function for iterations of things

for n in range(2,5)"
    print(nucleotides[n])

mySet=set(seqList) #take the list seqList and turn it into a set that has duplication removed

countNucs(sequence,set(sequence)) #Take the string sequence and create a set and then count
									#the objects within that set as they occur in sequence

#To run python scripts within ipython use %run script.py

