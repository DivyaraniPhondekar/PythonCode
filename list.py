squares = []
for x in range(1, 11):  
    squares.append(x**2) 

for x in squares:
	print x

list1 = ['physics', 'chemistry', 'maths']
print max(list1)	# checks ASCII value

list1.append('history')
print list1

print list1.count('maths')

print list1.index('maths')

list1.insert(2,'computer science')
print list1

list1.pop()
print list1

list1.pop(1)
print list1

list2=['vishal','divya','swati','aniket','amogh']
list2.remove('amogh')
print list2

list2.reverse()
print list2

list2.sort()
print list2