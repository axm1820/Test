#!/usr/bin/python -v 
x=''
number=4
limit=10
delement=(2*(number-2))-2
for i in xrange(1,limit):
    if (i > 0 and i <= number):
           print i,
    elif(i > number  and i < (number*2)):
           print "\n",(delement+1)*" ",str(i),
           delement=delement-2
    elif(i>=(number*2) and i < limit):
           if(i == (number*2)-1):
             print "\n",
           print i,
print str(0)
    
