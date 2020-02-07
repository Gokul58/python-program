n = int(input("enter the number"))
t = n
r = 0
while(n>0) :
     a = n % 10
     r = r+a*a*a
     n = n//10
if(r==t):
     print("armstrong number")
else:
     print("not a armstrong number")
