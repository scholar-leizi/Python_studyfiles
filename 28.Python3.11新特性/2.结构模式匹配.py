'''
结构模式匹配：
    可以针对整个数据结构进行模式匹配
    语法结构：
        match data:
            case{}:
                pass
            case[]:
                pass
            case():
                pass
            case_:
                pass
'''
data=eval(input('请输入要进行匹配的数据：'))
match data:
    case {'name':'杨淑珍','age':20}:
        print('这个数据类型是字典')
    case [10,20,30]:
        print('这个数据类型是列表')
    case (10,20,40):
        print('这个数据类型是元组')
    case _:
        print('相当于if语句中的else')
#跟if语句相似
