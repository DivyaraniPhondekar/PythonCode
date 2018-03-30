fav_numbers = {'eric': 17, 'ever': 4} 
for name, number in fav_numbers.items():     
	print(name + ' loves ' + str(number)) 
	
for name in fav_numbers.keys():     
	print(name + ' loves a number')

for number in fav_numbers.values():     
	print(str(number) + ' is a favorite')

# key error
#print ("fav_numbers['divya'] ",fav_numbers['divya'])	

 # remove entry with key 'eric'
del fav_numbers['eric']
print fav_numbers
 
# remove all entries in dict 
fav_numbers.clear()     
print fav_numbers

# delete entire dictionary 
del fav_numbers     
# print fav_numbers  

dict={'stuff':'pen','cost':'10'}
print ('length : %d' %len(dict))

print (str(dict))

print type(dict)

# copy method does shallow copy
dict2=dict.copy()
print ("new dictionary : %s"% dict2)

dict = dict.fromkeys(dict) 
print ("New Dictionary : %s" %  str(dict)) 

dict = dict.fromkeys(dict, 10) 
print ("New Dictionary : %s" %  str(dict))

# dict.get(key,default=None) method
dict = {'Name': 'Zara', 'Age': 27} 
print ("Value : %s" %  dict.get('Age')) 
print ("Value : %s" %  dict.get('Sex')) 
print ("Value : %s" %  dict.setdefault('Sex',"NA"))

# Update dict() means append
dict2 = {'Sex': 'female' } 
dict.update(dict2) 
print ("updated dict : ", dict)