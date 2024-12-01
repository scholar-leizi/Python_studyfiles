'''
集合的操作方法：
    s.add(x)：
        如果元素x不在集合s中，则将元素x添加到集合s
    s.remove(x)：
        如果元素x在集合中，将元素元素x在集合s中删除
    s.clear()：
        将集合s全部元素删除
'''
s={10,20,30}
print('原集合：',s)
s.add(40)
print('添加元素40：',s)
s.remove(10)
print('删除元素10：',s)
s.clear()
print('删除集合中的所有元素：',s)

#集合遍历
a={10,20,30,40,50,60,70,80,90,100}
for item in a:
    print(item)

#使用enumerate()遍历（可以遍历序号）
for index,item in enumerate(a):
    print(index,item)