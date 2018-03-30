# keyword argument
def callme(name,age):
	"This is keyword argument function"
	print (name,age)
	return

callme(age=22,name='divya')


# default argument
def callme(name,age=22):
	print (name,age)
	return

callme('divya')

 
# Function definition is here 
def printinfo( arg1, *vartuple): 
   "This prints a variable passed arguments" 
   print ("Output is: ") 
   print (arg1) 
   for var in vartuple: 
      print (var) 
   return 
# Now you can call printinfo function 
printinfo( 10 ) 
printinfo( 70, 60, 50 ) 