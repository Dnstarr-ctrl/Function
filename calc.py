def add(n1,n2):
    return n1+n2
def subtract(n3,n4):
    return n3-n4
def multiply(n5,b5):
    return n5*b5
def divide(n7,a3):
    return n7/a3
useroperatorchoose=input("Please enter the operation to perform: A) Add B) Subtract C) Multiply D) Divide: ").upper()
numchoosing=int(input("Enter the 1st number:"))
numchoosing2=int(input("Enter the 2nd number:"))
if useroperatorchoose=="A":
    print(numchoosing ,"+" ,numchoosing2, " =",add(numchoosing,numchoosing2))
elif useroperatorchoose=="B":
    print(numchoosing, "-", numchoosing2, " =",subtract(numchoosing-numchoosing2))
elif useroperatorchoose=="C":
    print(numchoosing, "*", numchoosing2, " =",multiply(numchoosing*numchoosing2))
elif useroperatorchoose=="D":
    print(numchoosing, "/", numchoosing2, " =" , divide(numchoosing/numchoosing2))
else:
    print("error!")