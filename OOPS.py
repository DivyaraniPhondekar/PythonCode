class Parent:
	pass

class Myclass(Parent):
	"Common base class"
	objcount=0
	def __init__(self,name,age):
		self.age=age
		self.name=name
		Myclass.objcount +=1

	def display(self):
		print ("Details : ",self.age,self.name)

obj1=Myclass("Zara",29)
obj2=Myclass("Raj",22)

obj1.display()
obj2.display()

print ("Total no. of objects %d" % Myclass.objcount)

print ("Myclass.__doc__:", Myclass.__doc__) 
print ("Myclass.__name__:", Myclass.__name__) 
print ("Myclass.__module__:", Myclass.__module__) 
print ("Myclass.__bases__:", Myclass.__bases__) 
print ("Myclass.__dict__:", Myclass.__dict__ ) 