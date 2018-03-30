import re

print ("Find the digits")
print (re.findall(r'\d','meera 56765 road'))

print ("Find the non-digits")
print (re.findall(r'\D','meera 56765 road'))


print ("Find the non-spaces")
print (re.findall(r'\S','meera 56765 road'))