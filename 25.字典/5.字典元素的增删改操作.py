'''
key的判断：
    in：
        指定的key在字典中存在返回True，反之返回False；'键' in 字典名
    not in：
        指定的key在字典中不存在返回True，反之返回False；'键' not in 字典名
字典元素的删除：
    删一个元素：
        del 字典名['键']；删除一整个键值对
    删全部元素：
        字典名.clear()
字典元素的新增：
    字典名['要新增元素的键']=要新增的值
字典元素的修改：
    字典名['要修改值的键']=修改值
'''
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('李四'  not in scores)

del scores['王五']#删除一个键值对
print(scores)
scores.clear()
print(scores)

scores['麻七']=123
print(scores)