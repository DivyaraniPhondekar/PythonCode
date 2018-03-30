# while loop with else

var1 = 100 
while var1<105:
	print "value increase by 1"
	var1+=1
else:
	print "condition becomes false"

# for loop

for l in 'Python':     # traversal of a string sequence 
	if l=='t':
		break
  	print ('Current Letter :', l) 
else:
	print "doen't contain d letter"

fruits = ['banana', 'apple',  'mango'] 
for fruit in fruits:        # traversal of List sequence 
    if fruit=='apple':
   		continue
print 'Current fruit is ',fruit


friends=['nihu','khush','nam','raj']	# iterating by sequence index
for index in range(len(friends)):
	print "my Current friend",friends[index]


# pass stmt does nothing. 
# It can be used when stmt is required syntacticallly but the pgm reqiures no action.

for letter in 'Python':  
   if letter == 'h': 
      pass 
      print ('This is pass block') 
   print ('Current Letter :', letter)  
print ("Good bye!") 