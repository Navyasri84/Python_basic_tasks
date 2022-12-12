m,n=[int(x) for x in input("Enter start value and stop value:").split(" ")]
i=m
if i%2==0: i=m+1
while(i<=n):
    print(i)
    i+=2


'''using for_loop'''

m=int(input("Enter the starting even number:"))
n=int(input("Enter the ending even number:"))

for i in range(m,n,2):
    print(i)

'''using while_loop'''
m=int(input("Enter the starting even number:"))
n=int(input("Enter the ending even number:"))
while(m<=n):
    print(m)
    m+=2


