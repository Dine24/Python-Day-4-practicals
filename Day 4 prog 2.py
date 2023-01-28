t=int(input("enter total users="))
if(t==0):
    print("invalid input")
    t=t=int(input("enter total users="))
elif(t<0):
    print("invalid input")
    t=t=int(input("enter total users="))
s=int(input("enter staff users="))
n=(s//3)
if(t<s):
    print("invalid input")
elif(t==s):
    print("student users are=",t-(s-n))
else:
    print("student users are=",t-s-n)
