# Sets are a collection of non repetetive elements
# Properties:
# -> unordered
# -> unindexed
# -> no way to change items
# -> cannot contain duplicate values
a=set()
print(type(a))

#Adding values to an empty set
a.add(1)
a.add(4)
a.add(4)
a.add(5)
a.add(5)      #Adding a value repeatedly does not change a set
a.add(6)
a.add((1,4,5,6))

# a.add({4:5})  # cannot add lists or dictionary to a set
print(a)

print(len(a))

#Removing items in a empty set
a.remove(1)
print(a)

print(a.pop())
print(a)

# a.clear()     #empties a set

print(a.union({8,9}))
print(a)
print(a.intersection({6,8}))

# Question
s=set()
s.add(2)
s.add(2.0)
s.add("2")
print(s)
