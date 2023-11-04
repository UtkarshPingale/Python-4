import random as r
import string

list=['/','*','-','+','[',']','{','}','|','<','>','?','/',':',';','=','!','@','#','$','%','^','&','_']

print("Enter Total Words You Want")
a=int(input())
print("Enter Total Symbols You Want")
b=int(input())
print("Enter Total Number You Want")
c=int(input())

d=[]
for i in range (a):
    d.append(r.choice(string.ascii_letters))

for i in range (b):
    d.append(r.choice(list))

for i in range (c):
    d.append(r.randint(0,9))

print("Your Password Is : ",end="")
for i in range(len(d)):
    print(r.choice(d),end="")

print()
if len(d)>=9:
    print("Your password is strong")
elif len(d)>=5 and len(d)<=8:
    print("Your password can be more strong")
else:
    print("Your password is weak")