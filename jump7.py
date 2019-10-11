i=1
while i<101:
    i+=1
    if i%7==0:
        continue
    elif i%10==7: 
        continue
    elif i//10==7:
        continue
    print(i)
