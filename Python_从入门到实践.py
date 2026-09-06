# 第一部分 基础知识
# 第1章 起步
# 1.1 搭建编程环境
# 1.1.1 Python 2和Python 3
# 1.1.2 运行Python 代码片段
# 1.1.3 Hello World 程序
# 1.2 在不同操作系统中搭建Python 编程环境
# 1.2.1 在Linux 系统中搭建Python 编程环境
# 1.2.2 在OS X 系统中搭建Python 编程环境
# 1.2.3 在Windows 系统中搭建Python 编程环境
# 1.3 解决安装问题
# 1.4 从终端运行Python 程序
# 1.4.1 在Linux 和 OS X 系统中从终端运行Python 程序
# 1.4.2 在Windows 心态中从终端运行Python 程序
# 1.5 小结

# 第2章 变量和简单数据类型
# 2.1 运行 hello_world.py 时发生的情况
# 变量
# 2.2.1 变量的命名和使用
# 2.2.2 使用变量时避免命名错误

# 动手试一试
# 2-1 简单消息：将一条消息存储到变量中，再将其打印出来。
message = "Hello, Python!"
print(message)

# 2-2 多条简单消息：将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。
message = "Hello, Python!"
print(message)
message = "Hello again, Python!"
print(message)

# 字符串
# 2.3.1 使用方法修改字符串的大小写
# 2.3.2 合并（拼接）字符串
# 2.3.3 使用制表符或换行符来添加空白
# 2.3.4 删除空白
# 2.3.5 使用字符串时避免语法错误    
# 2.3.6 Python 2 中的print 语句

# 动手试一试
# 2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如"Hello Eric, would you like to learn some Python today?"。
name = "Eric"
print("Hello " + name + ", would you like to learn some Python today?")

# 2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name = "ada lovelace"
print(name.lower()) # 小写
print(name.upper()) # 大写
print(name.title()) # 首字母大写

# 2-5 名言：找一句你敬佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似语下名这样（包括引号）：
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(famous_person + " once said, \"" + quote + "\"")

# 追加：牛顿名言示例
# 牛顿三大定律：
# 1. 惯性定律：物体保持静止或匀速直线运动状态不变，除非受到外力作用。
#    这说明物体具有惯性，不容易改变原来的运动状态。
# 2. 加速度定律：物体的加速度与所受合外力成正比，与质量成反比。
#    公式为 F = ma，表示力越大，物体越容易加速；质量越大，越难加速。
# 3. 作用力与反作用力定律：两个物体之间的作用力和反作用力大小相等、方向相反。
#    例如，跳跃时脚向地面向下施力，地面向上推脚，人才能离开地面。

famous_person = "牛顿"
quote = (
    "惯性定律：物体保持静止或匀速直线运动状态不变，除非受到外力作用。\n"
    "加速度定律：物体的加速度与所受合外力成正比，与质量成反比。\n"
    "作用力与反作用力定律：两个物体之间的作用力和反作用力大小相等、方向相反。"
)
print(famous_person + "说：\n\"" + quote + "\"")

# 2-6 名言2：重复练习2-5，但将名人的姓名存储在变量中，再创建一个名言变量，并将两者相连。
famous_person = "牛顿"  
quote = (
    "重力加速度公式：g = G * M / r^2\n"
    "其中：G 是万有引力常数，M 是天体质量，r 是距离中心的半径"   
)
g = "g = G * M / r^2"

print(famous_person + "说：\n" + quote + "\n")
print(g)      

# 2-7 剔除人名中的空白：存储一个人的姓名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。
#     打印该人名，以显示其开头和末尾的空白。然后，使用剔除函数lstrip()、rstrip()和strip()，并将结果打印出来。
name = "  Ada Lovelace  "
print("原始格式：" + repr(name))
print("剔除开头的空白后：" + name.lstrip())
print("剔除末尾的空白后：" + name.rstrip())
print("剔除开头和末尾的空白后：" + name.strip())    
print("原始格式：" + "\t" + repr(name))    
print("原始格式：" + "\n" + repr(name))   
print("原始格式：" + name)

# 2.4 数字
# 2.4.1 整数
# 2.4.2 浮点数
# 2.4.3 使用函数str()避免类型错误
# 2.4.4 Python 2 中的整数

# 动手试一试
# 2-8 数字8：编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。
# 为使用print语句来显示结果，务必将这些表达式用括号括起来，也就是说，你应该编写4行类似于下名的代码：
print(5 + 3)
print(10 - 2)
print(4 * 2)    
print(16 / 2)  
print(16//2) # 整除，结果为8
# 输出应为4行，其中每行都只包含一个数字8。

# 2-9 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用该变量创建一条消息，指出你最喜欢的数字。打印这条消息。
favorite_number = 7 
print("我的最喜欢的数字是：" + str(favorite_number))
print("我最喜欢的数字是：" + str(favorite_number) + "，它是一个幸运的数字。")   

# 2.5 注释
# 2.5.1 如何编写注释
# 2.5.2 该编写什么样的注释

# 动手试一试
# 2-10 添加注释：选择你在本章编写的两个程序，在每个程序中都至少添加一条注释。确保每条注释都能清楚地说明该行的作用。
name = "  yule chen  "
print(name.lower()) # 小写
print(name.upper()) # 大写
print(name.title()) # 首字母大写
print(100//20) # 整除，结果为5

# 2-6 Python 之禅
# 2.7 小结

# 第3章 列表简介
# 3.1 列表是什么
# 3.1.1 访问列表元素
# 3.1.2 索引从0而不是从1开始
# 3.1.3 使用列表中的各个值

# 动手试一试
# 3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，并将其打印出来。
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name) 
# 3-2 问候语：继续使用练习3-1中的列表，为其中的每个朋友打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for name in names:
    print("Hello, " + name + "! How are you today?")    
    print("I hope you are doing well, " + name + "!")   
# 3-3 自定义列表：想出你喜欢的通勤方式，并将其存储在一个列表中，再使用该列表打印一条消息，说明你喜欢的通勤方式。
commute_methods = ["bicycle", "bus", "train", "car"]
print("我喜欢的通勤方式有：")
for method in commute_methods:
    print(method)
