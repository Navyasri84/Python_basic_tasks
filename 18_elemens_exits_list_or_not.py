list=[int(x) for x in (input("Enter a list of elements:")).split()]
e=int(input("which element you want to find?"))
for i in list:
    if(e in list):
        print("The value",e,"is Found")
        break
    else:
        print("The value",e,"is Not found")
        break