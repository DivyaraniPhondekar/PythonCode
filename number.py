import math
import random

#  Mathematical Functions--------------------------------------------------------
#  positive distance between x and zero. 
print abs(-14)

print math.ceil(45.889)

print math.floor(45.889)

print math.exp(13)

print math.log(13)

print max(278.34,56,67.88,12)

print min(278.34,56,67.88,12)

print math.modf(-100.12)
print math.modf(math.pi)

print (math.pow(3, 3))

print (round(544.34))

# returns squareroot
print (math.sqrt(100))

# random Functions-------------------------------------------------------------
print (random.choice(range(100)))

# This method returns a random float r, such that 0.0 <= r <= 1.0 
print (random.random())

list=['d','i','v','y','a']
random.shuffle(list)
print list

print random.uniform(3,7)

# Trigonometric Functions-----------------------------------------------------
print math.acos(0.64)
print math.asin(0.64)
print math.atan(0.64)
print math.sin(0.64)
print math.cos(0.64)
print math.tan(0.64)
print math.hypot(3,4)
print math.degrees(0.64)
print math.radians(0.64)
print math.pi
print math.e