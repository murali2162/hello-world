print("This will calculate GCD of 2 no.s")
x=int(input("Enter 1st no.\n"))
y=int(input("Enter 2nd no.\n"))
z=x
a=y
i=1
if x==y:
    print("You entered same no.s")
if x-y==1 or y-x==1:
    lcm=x*y
else:
    while x>y:
        if z%y ==0:
            lcm=z
            break
        else:
            i+=1
            z=x*i
    while y>x:
        if a%x == 0:
            lcm=a
            break
        else:
            i+=1
            a=y*i
while True:
    gcd=int((x*y)/lcm)
    print("GCD is:",gcd)
    break