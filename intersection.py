t1 = (1,2,4,5)
t2 = (2,3,4,6)
t = ()
for i in t1:
    if i in t2:
        t += (i,)
print(t)
       
