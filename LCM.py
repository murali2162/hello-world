print("This will calculate LCM of 2 no.s")
x=int(input("Enter 1st no.\n"))
y=int(input("Enter 2nd no.\n"))
z=x
a=y
i=1
if x==y:
    print("You entered same no.s")
if x-y==1 or y-x==1:
    print("LCM is:",x*y)
else:
    while x>y:
        if z%y ==0:
            print("LCM is:",z)
            break
        else:
            i+=1
            z=x*i
    while y>x:
        if a%x == 0:
            print("LCM is:",a)
            break
        else:
            i+=1
            a=y*i
