#语法结构：
'''if 条件表达式1：
    if 内层条件表达式：
        内层条件执行体1
    else：
        内层条件执行体2
   else：
    条件执行体'''
'''编写一个超市会员打折程序；打折情况如下：
    有会员的情况：
        消费200元（包括200元）打8折
        消费100元（包括100元）打9折
        消费100元以下不打折
    没有会员的情况：
        消费200元（包括200元）打9.5折
        消费200元以下不打折'''

answer=input('您是会员吗？')
money=int(input('请输入您的购物金额：'))
if answer=='是':#是会员
    if money>=200:
        print('你的付款金额为'+str(money*0.8)+'元！')
    elif 100<=money<200:
        print('您的付款金额为'+str(money*0.9)+'元！')
    else:
        print('您的付款金额为'+str(money)+'元！')
else:#不是会员
    if money>=200:
        print('您的付款金额为'+str(money*0.95)+'元！')
    else:
        print('您的付款金额为'+str(money)+'元！')