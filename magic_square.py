n1=int(input("enter the number of row column: "))
a=[]
i=0
while i<n1:
    j=0
    b=[]
    while j<n1:
        x=int(input("enter the num: "))
        b.append(x)
        j=j+1
    i=i+1
    a.append(b)
print(a)

i=0
while i<n1:
    j=0
    while j<n1:
        print(a[i][j],end=" ")
        j=j+1
    i=i+1
    print()
sum1=0
sum2=0
i=0
while i<n1:
    j=0
    while j<n1:
        if i==j:
            sum1=sum1+a[i][j]
        if i+j==2:
            sum2=sum2+a[i][j]
        j=j+1
    i=i+1
    print()
i=0
while i<n1:
    r=0
    c=0
    j=0
    while j<n1:
        r=r+a[i][j]
        c=c+a[i][j]
        j=j+1
    i=i+1
    print()
if sum1==sum2 and r==c:
    print("magic square")
else:
    print("not magic square")