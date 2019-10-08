n=int(input("Enter the size of fibonacci series :"))
a=-1
b=1
for i in range (n):
    c=a+b
    print(f"{c}",end="   ")
    a=b
    b=c
    