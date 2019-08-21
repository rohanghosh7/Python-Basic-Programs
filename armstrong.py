n=int(input("Enter a number="))
copy=n
sum=0
while n>0:
    d=n%10;
    sum+=d**3
    n//=10
if sum==copy:
    print(copy,"is armstrong")
else:
    print(copy,"is not armstrong")
