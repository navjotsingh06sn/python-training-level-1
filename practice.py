print("hello, World")
name= input(" Enter your name : ")
print(name)
value= int(input("enter your no : "))
print(value)

A=18
A=int(input("enter the age : "))
if (A>=18):
     print("can vote")
else:
     print("cannot vote")

a=float(input("enter the marks : "))
if (a>=90):
    print("Grade A")
elif(a>=70 and a<90):
    print("Grade B")
elif(a>50 and a<70):
    print("Grade C")
elif(a>33 and a<50):
    print("Grade P")
else:
    print("Failure")

b=True
c=False
print(b or c)
print(b and c)
print(not c)

d=0
for d in range(0,10):
    print(d)

i=1
while(i<=10):
    print(i)
    i+=1

j=10
while(j>=1):
    print(j)
    j-=1

ab=["navjot","sheetal","satnam","armaan"]
print(ab)
