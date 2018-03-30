tuple=('happy','sad','hungry','exited','worried')
print tuple[2]
print tuple[2:5]

# tuple[5]='bored'	can't update
print tuple

tuple2=('abc','xyz','lmn')
tuple3=tuple+tuple2
print tuple3

del tuple3
# print tuple3

print len(tuple)
print max(tuple)
print min(tuple)

# List to tuple conversion
list1=['a','c','d','r']
tuple4= tuple(list1)
print tuple4