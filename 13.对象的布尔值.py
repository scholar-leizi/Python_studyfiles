#Python中一切皆为对象，所有对象都有一个布尔值；可以使用内置函数bool()获取
#以下对象的布尔值均为False：False、数值0、None、空字符串、空列表、空元组、空字典、空集合
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合

#除以上对象以外，其他对象的布尔值均为True