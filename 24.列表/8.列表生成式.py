#列表生成式是列表生成公式的简称
#语法格式：[表示列表元素的表达式 for 自定义变量 in 可迭代对象]
#注意事项：“表示列表元素的表达式”中通常包含自定义变量
lst1=[i for i in range(1,10)]
print('lst1：i   ',lst1)
lst2=[i*i for i in range(1,10)]
print('lst2：i*i ',lst2)
lst3=[i+1 for i in range(1,10)]
print('lst3：i+1 ',lst3)
lst4=[i-1 for i in range(1,10)]
print('lst4：i-1 ',lst4)
lst5=[i*5 for i in range(1,10)]
print('lst5：i*5 ',lst5)
lst6=[i/5 for i in range(1,10)]
print('lst6：i/5 ',lst6)
'''
规律：
    lst1：1      2       3       4       5       6       7       8       9   
    lst2：1      4       9       16      25      36      49      64      81
    lst3：2      3       4       5       6       7       8       9       10
    lst4：0      1       2       3       4       5       6       7       8
    lst5：5      10      15      20      25      30      35      40      45
    lst6：0.2    0.4     0.6     0.8     1.0     1.2     1.4     1.6     1.8
性质：
    运算数不是列表本身时：
        遵循算术运算法则
    运算数时列表本身时：
        遵循分配律（一一对位）
'''
