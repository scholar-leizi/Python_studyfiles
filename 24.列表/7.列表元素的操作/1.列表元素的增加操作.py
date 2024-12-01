'''
增加操作：
    append()：
        在列表的末尾添加一个元素
    extend()：
        在列表的末尾至少添加一个元素
    insert()：
        在指定索引位置上添加一个元素
    切片：
        在列表的任意位置至少添加一个元素
'''
lst1=[1,2,3]
lst1.append(4)#在列表的末尾添加一个元素
print(lst1)

lst2=[5,6]
#lst1.append(lst2)#将列表lst2看作一个整体添加到列表lst1的末尾
#print(lst1)
lst1.extend(lst2)#在列表的末尾至少添加一个元素
print(lst1)

lst1.insert(-4,7)#在列表的任意位置添加一个元素；第一个数是插入数，第二个数是要插入的元素
print(lst1)
#插入数是正数时，元素插入的位置会取代原列表中元素的位置，插入元素的右边的所有元素都会向右移一位；反之同理

lst3=[8,9]
lst1[1:]=lst3
print(lst1)#在列表的任意位置至少添加一个元素
#实际是是从插入数开始顺着正方向（负方向）从新存储新的元素
