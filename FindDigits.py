with open('/tmp/String.txt') as fobj:
    s= fobj.read()
res=' '
for char in s:
    if char.isdigit():
        res+=char
print(res)
