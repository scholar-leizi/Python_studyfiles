'''
元组的创建：
    直接使用小括号：
        元组名=(元素,元素,元素)
    使用内置函数tuple()：
        元组名=tuple((元素,元素,元素))
    只包含一个元组元素需要使用逗号和小括号：
        元组名=(元素,)
'''
t=('hello',123,True,3.14)
print(t,type(t))
t1='hello',123,True,3.14#省略小括号
print(t1,type(t1))

u=tuple(('world',False,520,13.14))
print(u,type(u))

p=(30,)
print(p,type(p))
p1=(30)
print(p1,type(p1))
#如果元组中只有一个元素，元素后面必须加逗号

'''空列表'''
lst=[]
lst1=list()
print('空列表',lst,lst1)
'''空字典'''
dic={}
dic1=dict()
print('空字典',dic,dic1)
'''空元组'''
tup=()
tup1=tuple()
print('空元组',tup,tup1)