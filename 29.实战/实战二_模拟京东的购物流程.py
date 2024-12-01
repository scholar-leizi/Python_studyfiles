'''
实战二：
    需求：
        从键盘录入5个商品信息（1001手机）添加到商品列表中，展示商品信息，提示用户选择的商品，用户选中的商品添加到购物车中（购物车中的商品要逆序），
        用户选中的商品不存在需要有相应提示，当用户输入“q“时结束循环，显示购物车中的商品
'''
#创建一个空列表，存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)
#输出所有的商品信息
for item in lst:
    print('入库的商品编号和名称为：',item)
#创建一个空列表，用作购物车
car=[]
while True:
    flag=False
    num=input('请输入要购买的商品编号：')
    #遍历商品列表，查询要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:#切片操作，从库中比对商品编号
            flag=True#代表商品已找到
            car.append(item)#添加商品到购物车
            print('商品已成功添加到购物车!')
            break#退出的时for循环
    if not flag and num!='q':#not flag等价于flag==False
        print('商品不存在！')
    if num=='q':
        break#推出while循环
print('-'*25)
print('您购物车中选中的商品有：')
car.reverse()
for item in car:
    print(item)