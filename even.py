num= list(range(2*32))
print(num)
i=0
while True:
    if num[i]//2==0:
        print(num[i])
        i=i+1
        if i==2*32:
            break
        
