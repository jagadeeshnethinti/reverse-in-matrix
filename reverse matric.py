a=int(input())
b=int(input())
k=a*b
for i in range(1,a+1):
    for j in range(1,b+1):
      print(k,end='')
      k=k-1
    print()