# Tuple is an immutable data in python

a=(1,2,5,3,3,2,2,1,4,3)

# t1=() #empty tuple
# t1=(1) #wrong way to declare single element in a tuple

t1=(1,) #declaring single element in a tuple
print(t1)

#printing elements of tuple
print(a)

print(a[0])

#cannot update values of tuple
# a[0]=9

# Tuple methods
print(a.count(3)) #returns no. of times 3 was repeated in the tuple

print(a.index(3)) #returns the index of the first 3
