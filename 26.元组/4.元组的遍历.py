#元组是可迭代对象，所以可以使用for...in循环遍历
t=tuple((20,True,3.14,'hello'))
print('第一种获取元组元素的方式：索引')
print(t[0])
print(t[1])
print(t[2])
print(t[3])
#print(t[4])#索引超出范围
print('第一种获取元组元素的方式：遍历')
for item in t:
    print(item)