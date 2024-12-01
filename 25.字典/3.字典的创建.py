'''
创建：
    使用花括号：
        字典名={'键':值,'键':值,'键':值}
    使用内置函数dict()：
        dict(键=值,键=值)
    通过映射函数创建：
        zip(lst1,lst2)
        lst1与lst2一一对应，前者为键，后者为值
'''
print('-----花括号-----')
scores={'张三':100,'李四':98,'王五':45}
print(scores,type(scores))
print('-----dict()-----')
student=dict(name='Jack',age=20)
print(student,type(student))
print('-----使用映射函数zip()-----')
lst1=[10,20,30,40]
lst2=['cat','dog','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)#<zip object at 0x0000025F770A5740>
#print(list(zipobj))#[(10, 'cat'), (20, 'dog'), (30, 'zoo'), (40, 'car')] 元组
d=dict(zipobj)
print(d)
