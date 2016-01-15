#!/usr/bin/python
from operator import itemgetter
jsondata={
 "id_number_1": {
 "firstName": "Joe",
 "lastName": "Smith",
 "birthDay": "1970-01-01",
 "phoneNumber": "123-456-7890",
},
 "id_number_2": {
 "firstName": "Jane",
 "lastName": "Smith",
 "birthDay": "1970-02-02",
 "phoneNumber": "555-555-1212",
},

 "id_number_3": {
 "firstName": "Andrews",
 "lastName": "Kevin",
 "birthDay": "1980-03-03",
 "phoneNumber": "987-654-3210"
 }
}
idlist=[]
for i in range(1,4):
   idlist.append('id_number_'+str(i))
# For each entry in idlist create an entry in jsonlist
jsonlist=[]
for i in idlist:
    jsonlist.append(jsondata[i])
print jsonlist 
keylist=['lastName','firstName','phoneNumber','birthDay']
for i in keylist:
    result = sorted(jsonlist, key=itemgetter(i))
    print "Retrieving sorted results for key " + i
    print "*******************************************"
    print result 
    print  "******************************************"
    
