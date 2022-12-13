import random
from random import randint
def main():
    print("what is the result of calculation?")
    x=random.randint(0,100)
    y=random.randint(0,100)
    z=random.randint(0,2)
    print(x,y)
    t=0
    k=0
    while k<=2:
        k=+1
        u=int(input("Введи число"))
        if z==0:
            t=x*y
            print(x+"*"+y)
        elif z==1:
            print(x+"+"+y)
            t=x+y
        elif z==2:
            (x+"-"+y)
            t=x-y
        if t==u:
            print("Correct!")
        else:
            print ("lose!")
            break
main()