#String Codes
a='ABCD'
b="XYZ"
c='''PQR'''
print(a,b,c)
#Str Indexing
a="I Love India"
print(a[2:7])
print(a[ :7])
print(a[7: ])
print(a[5])

#List Indexing
#append
list1=[5,7,"rr",[1,4,'R','Y'],"tegd"]
list2=["Hira",5,"Appa"]
list3=[1,2,7,4,5,6]
a="Ram"
list1.append(a)
print(list1)

# #Extend
list1.extend(list2)
print(list1)

# #Insert
list1.insert(2,a)
print(list1)

# #Remove
list1.remove(7)
print(list1)

#Index
b=list1.index("rr")
print(b)

# #Count
c=list1.count("tegd")
print(c)

#Sort
list3.sort()
print(list3)

# #Reverse
list3.reverse()
print(list3)

# #Copy
e=list2.copy()
print(e)

# #Clear
f=list3.clear()
print(f)

### Tuple##
# #count
a=(1,4,5,6,3,7,5,6,3,7)
print(a.count(5))

# #Index#
print(a.index(3))

## Dictionary Methods
# dic.clear{}
dic={1:"Hira",2:"Sona",3:"123",4:"Abc234"}
dic1={1:"Love",4:"India"}
dic.clear()
print(dic)

#dic.copy{}
a=dic.copy()
print(a)

#dic.Items{}
b=dic.items()
print(b)

#dic.Key{}
c=dic.keys()
print(c)

#dic.update{dic2}
dic.update(dic1)
print(dic)

#dic.values{}
e=dic.values()
print(e)

#dic.popitems{}
dic.popitem()
print(dic)

#dic.pop{}
dic.pop(1)
print(dic)

#dic.get{}
f=dic.get(3)
print(f)

####Set Method (remove, update, pop, copy, add, union, intersection, diffrence)
set1={3,6,"hira","Ponds"}
set2={"Vishw",453,"rr","hira"}
print(set)

#add
set1.add(7)
print(set1)

#Update
set1.update(set2)
print(set1)

#Remove
set1.remove(6)
print(set1)

#Copy
a=set1.copy()
print(a)

#pop
set1.pop()
print(set1)

#Union
h=set1.union(set2)
print(h)

#intersection
i=set1.intersection(set2)
print(i)

# #diffrence
s=set1.difference(set2)
print(s)


l1=[1,3,4,6,7,5,"Hira","tte"]
a=tuple(l1)
print(a)
print(type(a))

b=list(a)
print(b)
print(type(b))