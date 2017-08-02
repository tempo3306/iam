f = open('ces.py', 'r',encoding="utf-8")
f2 = open('ces2.py', 'a',encoding="utf-8")
line = f.readlines()
f.seek(0)
for l in line:
    for i in range(len(l)):
        if l[i]=='#':
            l=l[:i]+' '*(len(l)-i-1)+'\n'
            break
    f2.write(l)
f.close()