basket=('apple','orange','apple')
print(basket)

a=set('abracadabra')
b=set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b) #cunzai a huozhe b de zimu
print(a&b) #a b douyou de zimu
print(a^b) #cunzaiyu a b dan butongshi youde zimu

data={'kushal':'Fedora','kart_':'Debian','jace':'Mac'}
print(data['kart_'])
data['parthan']='Ubuntu'
print(data)
del data['kushal']
print(data)
print('ShiYanLou' in data)

sentence=[x +' uses ' + y  for x,y in data.items()]
print(sentence)

for x,y in data.items():
	print("{} uses {}".format(x,y))

data={}
data.setdefault('names',[]).append('Ruby')
print(data)
data.setdefault('names',[]).append('Python')
data.setdefault('names',[]).append('C')
print(data)

# for i,j in enumerate['a','b','c']: # bianli liebiao de tongshi huode suoyinzhi
	# print(i,j)


c=['efesef','dfwerfwe']
d=['hgtt','gthrrth']
for x,y in zip(a,b):
	print("{} uses {}".format(x,y))
