'''
实战四：
    要求：
        从键盘录入5位好友的姓名和手机号码，由于通讯录是无序的，所以可以使用集合实现
'''
d=set()
for i in range(1,6):
    hao=input(f'请输入第{i}好友的姓名和手机号码：')
    d.add(hao)
for item in d:
    print(item)