#📦 Python 元组（tuple）完全指南

#一、什么是元组？
#元组是 Python 中不可变的序列类型，用 () 圆括号表示，元素用逗号分隔。
# 一旦创建就不能修改（不能增、删、改元素）!
#例子：
# 基本示例
point = (3, 5)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14)
empty = ()                # 空元组

#————————————————————————————————————————————————————————————————————



#二、元组创建
# 1. 用圆括号（最常见）
t1 = (1, 2, 3)
print(t1)                 # (1, 2, 3)

# 2. 省略括号（逗号是关键！）
t2 = 1, 2, 3
print(t2)                 # (1, 2, 3)
print(type(t2))           # <class 'tuple'>

# 3. 单元素元组（必须加逗号！）
t3 = (5,)                 # ✅ 正确的单元素元组
print(t3)                 # (5,)
print(type(t3))           # <class 'tuple'>

not_tuple = (5)           # ❌ 这是整数，不是元组！
print(type(not_tuple))    # <class 'int'>

# 4. tuple() 构造函数
t4 = tuple("hello")
print(t4)                 # ('h', 'e', 'l', 'l', 'o')

t5 = tuple([1, 2, 3])    # 列表→元组
print(t5)                 # (1, 2, 3)

######⚠️ 关键注意：单元素元组必须加逗号！ (5) 是整数 5，(5,) 才是元组。######

#————————————————————————————————————————————————————————————————————————————————


# 三、元组的不可变性
# 🚫 不能修改
t = (1, 2, 3)
# t[0] = 100    # ❌ TypeError: 'tuple' object does not support item assignment
# t.append(4)   # ❌ AttributeError: 'tuple' object has no attribute 'append'
# t.pop()       # ❌ AttributeError

# ✅ 可以查询（和列表一样）
t = (10, 20, 30, 40, 50)

print(t[0])         # 10
print(t[-1])        # 50
print(t[1:4])       # (20, 30, 40)
print(t[::-1])      # (50, 40, 30, 20, 10)
print(len(t))       # 5
print(20 in t)      # True
print(t.index(30))  # 2     index() 方法用于查找指定元素第一次出现的位置（索引）
print(t.count(20))  # 1     count() 方法用于统计指定元素在序列中总共出现了多少次
 
# 🔗 元组可以整体替换（不是修改）
t = (1, 2, 3)
t = (4, 5, 6)       # ✅ 这是重新赋值，不是修改元组本身
print(t)            # (4, 5, 6)

# 但元组内的可变对象可以修改其内容
t = ([1, 2], "hello")
t[0].append(3)      # ✅ 元组本身没变，但列表内容变了
print(t)            # ([1, 2, 3], 'hello')

# 元组不可变性示意图：

#     t = (1, 2, 3)
#          ↓  ↓  ↓
#         [1][2][3]    ← 这些格子不能被改写
    
#     t = ([1, 2], "hello")
#          ↓        ↓
#         [1,2]    "hello"    ← 元组引用不能变
#          ↓
#         [1,2,3]             ← 但列表内部可以变！
  
#————————————————————————————————————————————————————————————————————————————————




# 四、元组解包（Tuple Unpacking）
# 这是元组最强大的特性之一！将元组中的元素一次性赋值给多个变量。

# 🎯 基础解包
# 一对一解包
point = (3, 5)
x, y = point
print(x, y)             # 3 5

# 交换变量（经典一行！）
a, b = 10, 20
a, b = b, a            # 背后就是元组解包
print(a, b)            # 20 10

# 返回多个值
def min_max(lst):
    return min(lst), max(lst)

result = min_max([3, 1, 7, 2, 9])
print(result)          # (1, 9)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)       # 1 9

# 🌟 带星号解包（Python 3+）
# * 收集剩余元素（类似列表）
first, *rest = (1, 2, 3, 4, 5)
print(first)            # 1
print(rest)             # [2, 3, 4, 5]  ← 注意是列表！

# 中间收集
first, *middle, last = (1, 2, 3, 4, 5)
print(first)            # 1
print(middle)           # [2, 3, 4]
print(last)             # 5

# 忽略某些值（用 _）
_, second, _, fourth = (1, 2, 3, 4)
print(second, fourth)   # 2 4

# 🎯 多维解包（嵌套元组）
# 嵌套元组解包
nested = ((1, 2), (3, 4))
(a, b), (c, d) = nested
print(a, b, c, d)      # 1 2 3 4

# 实际应用：遍历字典的 items()
student = {"name": "小明", "age": 18, "score": 95}
for key, value in student.items():   # items() 返回的就是元组
    print(f"{key} = {value}")

# 五、元组 vs 列表 对比
# 特性	    列表 list	   元组 tuple
# 语法	    [1, 2, 3]	   (1, 2, 3)
# 可变性	✅ 可增删改	  ❌ 不可变
# 性能	    较慢	       较快 ✅
# 内存	    较大	       较小 ✅
# 哈希性	❌ 不可哈希	  ✅ 可哈希（可作字典键）
# 适用场景	需要修改的集合	固定数据、字典键、函数返回值

# 💡 为什么要用元组？
# 1. 字典的键 — 元组可哈希，列表不行
locations = {
    (35.68, 139.69): "东京",
    (40.71, -74.01): "纽约",
}
print(locations[(35.68, 139.69)])   # 东京
# locations[[1, 2]] = "test"        # ❌ TypeError: unhashable type: 'list'

# 2. 函数返回多个值（本质是元组）
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder   # 返回元组

q, r = divide(17, 5)
print(q, r)                      # 3 2

# 3. 保护数据不被意外修改
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# DAYS_OF_WEEK[0] = "xxx"        # ❌ 不能修改，安全！
#——————————————————————————————————————————————————————————————————————————————————




# 六、元组常用操作速查
# 操作	       代码	                         结果
# 创建	    t = (1, 2, 3)	              (1, 2, 3)
# 单元素	t = (5,)	                   (5,)
# 索引	    t[0]	                       1
# 切片	    t[1:3]	                      (2, 3)
# 解包	    a, b = (1, 2)	              a=1, b=2
# 拼接	    (1,2) + (3,4)	             (1, 2, 3, 4)
# 重复	    (1,2) * 3	                 (1, 2, 1, 2, 1, 2)
# 成员	     2 in (1,2,3)	               True
# 长度	     len((1,2,3))	               3
# 最小值	 min((3,1,4))	               1
# 最大值	 max((3,1,4))	               4
# 求和	     sum((1,2,3))	               6
# 排序	     sorted((3,1,4))	           [1, 3, 4]（返回列表）
# 计数	     (1,2,2).count(2)	           2
# 索引查找	  (1,2,3).index(2)	            1

