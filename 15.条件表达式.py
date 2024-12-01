#条件表达式是if......else的简写
#语法结构：X if 判断条件 else Y
#运算规则：如果判断条件的布尔值为True，条件表达式的返回值为X，反之条件表达式的返回值为Y

#从键盘录入两个整数，比较两个整数的大小
mun_a=int(input('请输入第一个整数：'))
mun_b=int(input('请输入第二个整数：'))
print('这两个整数中'+str(mun_a if mun_a>mun_b else mun_b)+'大！')