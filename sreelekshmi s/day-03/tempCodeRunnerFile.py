complexdata=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
update=complexdata[1]
update.update({'gender':'male'})    #update name
print(complexdata)