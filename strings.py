l1=[0,0,1,2,3,3,3,4,5,5,5]
l2=[]
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
    print(l2)
print(l2)