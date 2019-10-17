def f(a,data=[]):
    data.append(a)
    return data
print(f(1))
print(f(2))
print(f(3))

def f(a,data=None):
    if data is None:
        data=[]
    data.append(a)
    return data

print(f(1))
print(f(2))

def func(a,b=5,c=10):
    print('a is'+str(a)+'and b is'+str(b)+'and c is'+str(c))

func(12,24)
func(12,c=24)
func(b=12,c=24,a=-1)

def hello (*,name='User'):
    print("Hello",name)

hello(name='shiyanlou')

