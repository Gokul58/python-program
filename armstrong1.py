n = input("enter the number")
pw = len(n)
s = 0
for i in n:
    s += int(i)**pw
 
if int(n) == s:
    print("Armstrong number", s)
else:
    print("Not a armstrong number")
