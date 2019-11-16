print('Enter your number : ')
n=int(input())
a=list()
for num in range(0,n+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            a.append(num)
print(a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]!=a[j] and a[i]+a[j]==n:
            print(a[i],a[j])
