list1=[]
total=0
for i in range(1,6):
    list1.append(input("Enter number :"))
for j in list1:
    total+=int(j)
print(f"Average of five number :{str(total/5)}")