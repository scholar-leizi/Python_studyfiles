'''
集合元素的判断操作：
    in或not in
集合元素的新增操作：
    调用add()方法，一次添加一个元素
    调用update()方法，至少添加一个元素
集合元素的删除方法：
    调用remove()方法，一次删除一个指定的元素，如果指定的元素不存在，会返回KKeyError
    调用discard()方法，一次删除一个指定元素即使元素不存在也不会放回异常
    调用pop()方法，一次删除一个任意元素
    调用clear()方法，清空集合
'''
s={10,20,30,40,50}
print(10 in s)
print(10 not in s)

s.add(60)
print(s)
s.update({80,'hello',90,3.14})
print(s)

s.remove('hello')
print(s)

#s.remove('hello')#KeyError
#print(s)
s.discard('hello')
print(s)

s.pop()
print(s)

s.clear()
print(s)