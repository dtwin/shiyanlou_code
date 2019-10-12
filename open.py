fobj=open("sample.txt")
print(fobj)


print(fobj.read())
print(fobj.read()) #读取完一遍后再读只能是空格

fobj.close()


fobj2=open("sample.txt")

print(fobj2.readline())

fobj2.close()




fobj3=open("sample.txt")

print(fobj3.readlines())

fobj2.close()



fobj4=open("sample.txt")

for x in fobj4:
    print(x, end=' ')

fobj4.close()


name=input("Enter the file name:")
fobj5=open(name)
print(fobj5.read())
fobj5.close()

name=input("Enter the file name:")
fobj5=open(name,'a')
fobj5.write('powerpork\n')
fobj5.write('powerpork\n')
fobj5.write('powerpork\n')
fobj5.write('powerpork\n')
fobj5.close()

fobj6=open("sample.txt")
print(fobj6.read())
fobj6.close()
