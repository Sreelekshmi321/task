"""Look at sample complex data structure

[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}] """


#1. Please sort the dictionary based on Age.

complexdata=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
complexdata.sort(key=lambda x:x['age'])
print(complexdata)


#2. Change the Name of id = 3 from syam to Shobhana

complexdata=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
update=complexdata[2]
update.update({'name':'shobhana'})    #update name
print(complexdata)


#3. Update Gender "Male" only for "Ajay" record."""

complexdata=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
update=complexdata[1]
update.update({'gender':'male'})    #update name
print(complexdata)