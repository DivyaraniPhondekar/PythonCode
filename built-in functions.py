a=10
s='mystring'

def myfunct():
	a='hello'
	b='world'
	c=100
	print(globals())
	print(locals())
myfunct()

print(globals())

print eval('2**4')

a='hello'
print eval(repr(a))
print ord('A')