'''
集合：
    是一种Python语言提供的内置数据类型
    是与字典，列表一样，都是可变类型的序列
    集合是没有值的字典
集合的创建：
    直接使用{}：
        s={'Python',False,120,3.14,120,3.14}
    使用内置函数set()：
        s1=set(range(6))
        print(s1)
        print(set([3,True,'Hello',3.14]))
        print(set((120,False,'Python',3.14)))
        print(set('Python'))
        print(set({321,True,3.14,'World'}))
        print(set())（空集合）
'''
print('-----直接使用{}-----')
s={'Python',False,120,3.14,120,3.14}
print(s)#集合中的元素不允许重复
print('-----使用内置函数set()-----')
s1=set(range(6))
print(s1,type(s1))

print(set([3,True,'Hello',3.14]))

print(set((120,False,'Python',3.14)))

print(set('Python'))#集合是无序的

print(set({321,True,3.14,'World'}))

#定义一个空集合
#s2={}  #dict字典类型
#print(s2)
s3=set()
print(s3)

#s4={[10,20],[30,40]}# TypeError: unhashable type: 'list'
#print(s4)