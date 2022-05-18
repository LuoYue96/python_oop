l1=input().split(',')
l2=input().split(',')
tmp1=len(l1)
tmp2=len(l2)
var1=0
var2=0
for i in l1[::-1]:
    tmp = int(i)
    var1+= tmp*10**(tmp1-1)
    tmp1-=1
for i in l2[::-1]:
    tmp = int(i)
    var2+= tmp*10**(tmp2-1)
    tmp2-=1
sum=var1+var2
tmp3=str(sum)
list1=[]
for i in tmp3[::-1]:
    list1.append(int(i))
print(list1)
