#列表需要使用中括号来创建，元素之间要使用英文的逗号进行分隔
'''
列表的创建方式：
    调用内置函数list()：
        列表名=list([值,值,值,值])
    使用中括号：
        列表名=[值,值,值,值]
'''
lst1=list(['hello',123,3.14,True])
print(lst1)
print(id(lst1))
print(type(lst1))
lst2=['Python',520,13.14,False]
print(lst2)
print(id(lst2))
print(type(lst2))