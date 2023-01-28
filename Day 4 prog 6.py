def delchar(a,b):
    if len(b)!=1:
        return a
    else:
        return a.replace(b,"")
a="Good evening"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Take care"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="123456s"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Red rose"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="Flower"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))
