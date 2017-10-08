num= list(range(input("Enter a number and even no.s will be displayed till that no.")))
print(num)
i=0
while True:
    if num[i]//2==0:
        print(num[i])
        i=i+1
        if i==num or i==num-1:
            break
        
