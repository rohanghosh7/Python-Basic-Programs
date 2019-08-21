n=int(input("Enter a number="))
copy=n
rev=0
while n>0:
    d=n%10;
    rev=(rev*10)+d
    n//=10
if rev==copy:
    print(copy,"is palindrome")
else:
    print(copy,"is not palindrome")
