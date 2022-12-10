'''sortings strings'''

a="navyasri"
print(sorted(a))

'''sorting list'''

a=['n','a','v','y','a','s','r','i']
a.sort()
print(a)


sor=[]
n=int(input("How many strings?"))
for i in range(n):
    s=input("Enter String:")
    sor.append(s)
sor.sort(reverse=True)
print(sor)
print(sor[::-1])
print(*sor)
for i in sor:
    print(i,end=" ")