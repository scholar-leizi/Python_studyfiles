#什么是转义字符？
#就是反斜杠+想要实现的转义功能的首字母

#为什么需要转义字符？
#当字符中包含发斜杠，单引号和双引号等具有特殊用途的字符时，必须使用反斜杠对这些字符转义（转换成另一种含义）
#反斜杠：\\
print("htttp:\\\www.baidu.com")
#单引号：\'
print('老师说：\'大家好！\'')
#双引号：\"
print("老师说：\"大家好！\"")

#当字符串中包含换行、回车、水平制表或退格等无法直接表示的特殊字符时，也可使用转义字符
#换行：\n
print("hello\nworld")#n-->newline的首字母，换行输出
#回车：\r
print("hello\rworld")#r是回车键的缩写，回到原点输出
#水平制表：\t
print("hello\tworld")#t-->tab的首字母，隔一个制表位输出
#退格：\b
print("hello\bworld")#退一个格输出

#原字符：不希望字符串中的转义字符起作用，就用原字符，就是在字符串之前加r或R
print(r'hello\rworld')
#注意事项：字符串最后一个字符不能是一个反斜杠
#print(r'hello\rworld\')
print(r'hello\rworld\\')