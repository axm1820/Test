#!/usr/bin/python -v
number=7
counter=1
twod_list = []
for i in xrange(number):
     new=[]
     for i in range(number):
       new.append(0)
     twod_list.append(new)

print twod_list
#Traverse the list 
start=0
column=0
for row in range(start,number):
    twod_list[row][column]=counter
    counter=counter+1
print twod_list
newrow=1

for column in range(newrow,number-1):
    twod_list[newrow][column]=counter
    counter=counter+1
    newrow=newrow+1
print twod_list
print "counter "+"is"+str(counter)

column=number-1
for row1 in range(0,number):
     twod_list[row1][column]=counter
     counter=counter+1

twod_list[number-1][number-1]=0
print twod_list 
#Iterate over the list to print letter n
for i in range(number):
    for j in range(number):
        if(twod_list[i][j] == 0):
           if(i==(number-1) and j==(number-1)):
             print 0,
           else:
             print " ",
        else:
           print twod_list[i][j],
    print ("\n"),    
