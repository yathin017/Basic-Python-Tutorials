# Lists store set of values of any data type

#List indexing
a=["Apple","Mango",7,False]
print(a[0])
# indexing lists is kinda same like indexing strings

#List Methods
l1=[1,3,2,7]
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(9)
print(l1)

l1.insert(3,8)  #inserts 8 at index 3
print(l1)

l1.pop(3)       #deletes element at index 3 and returns its value
print(l1)

l1.remove(3)
print(l1)