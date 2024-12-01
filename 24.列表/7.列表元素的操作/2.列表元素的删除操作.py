'''
删除操作：
    remove()：
        一次删除一个元素
        重复元素只删除一个
        元素不存在会返回ValueError
    pop()：
        删除一个指定索引上的元素
        指定索引不存在会返回IndexError
        不指定索引时，会删除列表中的最后一个元素
    切片：
        一次删除至少一个元素：
            生成新列表：
                “新列表名=原列表名[start:stop:step]"
            不生成新列表：
                ”原列表名[start:stop:step]=[]（用空列表替换）
    clear()：
        清空列表
    del：
        删除列表
'''
lst1=[10,20,30,40,50,60,70,30,]
lst1.remove(10)#一次删除一个元素
print(lst1)
lst1.remove(30)#重复元素只删除一个
print(lst1)

lst1.pop(0)#删除一个指定索引上的元素
print(lst1)
lst1.pop()#不指定索引时，会删除列表中的最后一个元素
print(lst1)

lst2=lst1[:3]#一次删除至少一个元素
print(lst2)
#会创建一个新的列表对象

lst1.clear()#清空列表
print(lst1)

#del lst1：删除列表
#print(lst1)