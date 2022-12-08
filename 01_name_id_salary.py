'''Printing the name, id and salary from the user input'''

Name= input("Enter your name:")
Id= int(input("Enter your Id number:"))
Salary= float(input("Enter your Salary:"))

print("Your name is",Name,",Your Id is",Id,"and Your salary is",Salary)
print(f"Your name is {Name}, Your Id is {Id} and Your salary is {Salary}")
print("Your name is {}, Your Id is {} and Your salary is {}".format(Name,Id,Salary) )
print("Your name is {1}, Your Id is {0} and Your salary is {2}".format(Id,Name,Salary) )
