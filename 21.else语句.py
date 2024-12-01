'''else的搭配：
    1.if。。。：
        。。。
      else：
        。。。
    2.while。。。：
        。。。
      else：
        。。。
    3.for。。。：
        。。。
      else：
        。。。'''
#第一种在if条件表达式不成立时执行else；第二和第三种在没有碰到break时执行else
a=0
while a<3:
    pwd=int(input('请输入您的密码：'))
    if pwd==8888:
        print('密码正确！')
        break
    else:
        print('密码错误！')
    a+=1
else:
    print('对不起！三次密码均输入错误！')