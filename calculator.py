def add():
    a=int(input("No:"))
    b=int(input("No:"))
    c=a+b
    print(c)   

def sub():
    a=int(input("No:"))
    b=int(input("No:"))
    c=a-b
    print(c)   

def mul():
    a=int(input("No:"))
    b=int(input("No:"))
    c=a+b
    print(c)

def div():
    a=int(input("No:"))
    b=int(input("No:"))
    c=a+b
    print(c)   


   

def main():
    a=int(input("1) ADD \n2) SUB \n3) MULTIPLICATION \n4) DIVISION :"))
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        mul()
    elif a==4:
        div()

main()
        
