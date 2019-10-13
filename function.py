def high(l):
    return [i.upper() for i in l]

def test(h,l):
    return h(l)

l=[]
for i in range(3):
    l.append(input())
    print(test(high,l))


# map 函数   接受一个函数和一个序列（迭代器）作为输入，然后对序列的每一个值应用这个函数，返回一个序列，其包含应用函数后的结果
lst=[1,2,3,4,5]
def square(num):
    return num*num
print(list(map(square,lst)))
