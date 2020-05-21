# Lists

l = [1,5,7,10,2,20,9]
print(l[0])

#List slicing
x = l[1:4]
print(x)

#Append
l.append(10)
print(l)

#Extend
b = [20,100]
l.extend(b)
print(l)

#Insert
l.insert(2,55)
print(l)

#Sorting
l.sort()
print(l)

#Delete
l.pop(5)
print(l)

#Count
a = l.count(20)
print(a)

#Length
b = len(l)
print(b)

#Sum
c = sum(l)
print(c)

l = [100,5,99,9,8,7,2]
x = l*3
print(x)

#For loop
for i in range(len(l)):
	print(l[i],end=' ')

#User input
l = []
n = 5
for i in range(n):
	a = int(input())
	l.append(a)

print(l)