mylist=[2,45,67,0,213,8]
num=2
try:
	for i in mylist:
		a=num/i
		print(a)
except:
	print("divided by zero")
finally:
	print("after exception")