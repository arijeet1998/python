n,m=input("Enter n and m number :").split()
n=int(n)
m=int(m)
total=0
for i in range (n,m+1):
    total+=i
print(f"Sum of number between n to m number {total}")

