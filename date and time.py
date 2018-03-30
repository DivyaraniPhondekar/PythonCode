import time;
import calendar;

ticks=time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks) 

print (time.localtime())

localtime = time.asctime( time.localtime()) 
print ("Local current time :", localtime)

cal = calendar.month(2016, 2) 
print ("Here is the calendar:") 
print (cal) 

print ("time.altzone : ", time.altzone)

t = time.localtime() 
print ("asctime : ",time.asctime(t))