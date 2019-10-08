def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
while True:
    a,b,c=input("Enter 3 number :").split()
    a=int(a)
    b=int(b)
    c=int(c)
    print("Maximun of 3 number is  "+ str(max(a,b,c)))
    op=int(input("Again Check \n1.Yes\n2.No\n"))
    if(op==2):
        print("Thank you")
        break

