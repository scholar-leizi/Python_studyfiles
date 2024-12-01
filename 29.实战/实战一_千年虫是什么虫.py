'''
实战一：
    需求：
        已知一个列表中存储的是员工的出生年份[88,89,90,98,00,99]，由于时间比较久，出生的年份均为2位整数，现需要2位年份前加19，
        如果年份是00，将需要加上200
    运行效果：
        原列表：[88,89,90,98,00,99]
        ['1988','1989','1990','1998','2000','1099']
'''
lst=[88,89,90,98,00,99]#表示员工的两位整数出生年份
print(lst)
#遍历列表的方式
for index in range(len(lst)):#按照列表长度循环（员工年份的个数）
    if str(lst[index])!='0':
        lst[index]='19'+str(lst[index])#拼接年份，载赋值
    else:
        lst[index]='200'+str(lst[index])
print('修改后的年份列表：',lst)

#使用enumeratr()遍历
lst1=[88,89,90,98,00,99]
for index,value in enumerate(lst1):
    if str(value) != '0':
        lst1[index] = '19' + str(value)  # 拼接年份，载赋值
    else:
        lst1[index] = '200' + str(value)
print('修改后的年份列表：', lst1)