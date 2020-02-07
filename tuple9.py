b = []
t = ('gokul','nabeel','tomu','gokul','gaurav','tomu')
for i in t:
    if t.count(i)>1:
        if i not in b:
            b.append(i)
print(b)
