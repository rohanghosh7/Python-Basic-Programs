#String basics
a = "hi i am rohan"
print(a[1])
print(a[5])
print(len(a))

#String slicing
a = "RohanGhosh"
s = a[:5]
print(s)
t = a[0:]
print(t)

#String functions

#count function
a = "Hi Hi Hi Rohan Ghosh abc okay"
b = "Hi"
count = a.count(b)
print(count)

#find function
c = "Rohan"
f = a.find(c)
d = a[f:]
print(f)
print(d)

#replace
a = "Hi Hi Hi Rohan Ghosh abc okay"
a = a.replace(" ","-")
print(a)

#in
a = "Hi Hi Hi Rohan Ghosh abc okay"
b = "Rohan"
if(b in a):
	print("Yes")
else:
	print("No")

#for loops
a = "Hi Hi Hi Rohan Ghosh abc okay"

for c in a:
	print(c,end='')

#Case change
a = "Hi Hi Hi Rohan Ghosh abc okay"
a = a.upper()
print(a)