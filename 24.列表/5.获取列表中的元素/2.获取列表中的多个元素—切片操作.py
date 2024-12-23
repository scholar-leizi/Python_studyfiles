#语法格式：列表名[start:stop:step]
'''
切片操作：
    切片的结果：
        原列表片段的拷贝
    切片的范围：
        [start,stop)
    step默认为1：
        简写为[start:stop]
    step为正负数：
        step为正数：
            [:stop:step]：
                切片的第一个元素默认是原列表的第一个元素
            [start::step]：
                切片的最后一个元素默认是原列表的最后一个元素
        从start开始往后计算切片

        step为负数：
            [:stop:step]：
                切片的第一个元素默认是原列表的最后一个元素
            [start::step]：
                切片的第一个元素默认是原列表的第一个元素
        从start开始往前计算切片
'''
lst=[10,20,30,40,50,60,70,80,90]
print(lst[1:6])
print(lst[:9:3])
print(lst[3::3])
print(lst[:1:-2])
print(lst[6::-3])