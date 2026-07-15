#增删改查（CRUD）
#📖 查（Read）
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]

print(fruits[0])    # 苹果
print(fruits[2])    # 橘子
print(fruits[-1])   # 西瓜（负索引从右往左）
print(fruits[-3])   # 橘子

#检查元素是否存在：
print("香蕉" in fruits)    # True
print("榴莲" in fruits)    # False
print("榴莲" not in fruits) # True
#————————————————————————————————————————————————————————
#✏️ 改（Update）
fruits = ["苹果", "香蕉", "橘子"]
fruits[1] = "蓝莓"         # 直接赋值修改
print(fruits)              # ['苹果', '蓝莓', '橘子']
#——————————————————————————————————————————————————————————
#➕ 增（Create / Add）
fruits = ["苹果", "香蕉"]

# 1. append() — 末尾追加单个元素
fruits.append("橘子")
print(fruits)              # ['苹果', '香蕉', '橘子']

# 2. insert() — 指定位置插入
fruits.insert(1, "蓝莓")   # 在索引1处插入
print(fruits)              # ['苹果', '蓝莓', '香蕉', '橘子']

# 3. extend() — 合并另一个列表（批量追加）
more = ["葡萄", "西瓜"]
fruits.extend(more)
print(fruits)              # ['苹果', '蓝莓', '香蕉', '橘子', '葡萄', '西瓜']

# 4. 用 + 合并（生成新列表）
a = [1, 2]
b = [3, 4]
c = a + b
print(c)                   # [1, 2, 3, 4]
#—————————————————————————————————————————————————————————————————
#🗑️ 删（Delete）
fruits = ["苹果", "香蕉", "橘子", "葡萄", "香蕉"]
print(fruits)              # ['苹果', '香蕉', '橘子', '葡萄', '香蕉']
# 1. remove() — 删除第一个匹配的元素（按值）
fruits.remove("香蕉")
print(fruits)              # ['苹果', '橘子', '葡萄', '香蕉']

# 2. pop() — 弹出并删除指定索引（默认末尾）
last = fruits.pop()        # 弹出最后一个
print(last)                # 香蕉
print(fruits)              # ['苹果', '橘子', '葡萄']

item = fruits.pop(1)       # 弹出索引1
print(item)                # 橘子

# 3. del 语句 — 按索引或切片删除
del fruits[0]
print(fruits)              # ['葡萄']

# 4. clear() — 清空所有元素
fruits.clear()
print(fruits)              # []
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#切片操作（Slicing）
#切片是从列表中提取子列表的强力语法：list[start:stop:step]
#🔍 基本切片：
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])     # [2, 3, 4, 5]     索引2→5（不包含6）
print(nums[:4])      # [0, 1, 2, 3]     start省略→从0开始
print(nums[6:])      # [6, 7, 8, 9]     stop省略→到末尾
print(nums[:])       # [0..9] 完整副本   start和stop都省略→整个列表

#🎯 步长切片
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])     # [0, 2, 4, 6, 8]      步长2→偶数
print(nums[1::2])    # [1, 3, 5, 7, 9]      步长2从1开始→奇数
print(nums[::3])     # [0, 3, 6, 9]         步长3

#🔄 反向切片（步长为负）
print(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  经典反转！
print(nums[::-2])    # [9, 7, 5, 3, 1]                  反向跳2
print(nums[7:2:-1])  # [7, 6, 5, 4, 3]                  从7反向到3

#📝 切片高级用法：修改和删除
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 切片赋值（替换一段）
nums[2:5] = [20, 30, 40]
print(nums)          # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
# 切片删除
nums[2:5] = []
print(nums)          # [0, 1, 5, 6, 7, 8, 9]
# 用切片插入（不用替换，直接扩缩容）
nums[2:2] = [100, 200]   # 在索引2处插入
print(nums)          # [0, 1, 100, 200, 5, 6, 7, 8, 9]

#————————————————————————————————————————————————————————————————————————
#核心列表方法详解
#🔧 append(x) — 末尾追加
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)         # [1, 2, 3]
# 经典用法：把列表当栈用

#🔧 sort() — 原地排序
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()               # 升序
print(nums)               # [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)   # 降序
print(nums)               # [9, 5, 4, 3, 2, 1, 1]

# 自定义排序：按字符串长度
words = ["apple", "hi", "banana", "cat"]
words.sort(key=len)
print(words)              # ['hi', 'cat', 'apple', 'banana']

# ⚠️ sort() 是原地修改，不返回新列表
# 如果要保留原列表，用 sorted() 函数：
original = [3, 1, 4]
new = sorted(original)    # 返回新列表
print(original, new)      # [3, 1, 4]  [1, 3, 4]

#🔧 reverse() — 原地反转
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)              # [5, 4, 3, 2, 1]

# 等效于切片反转，但 reverse() 是原地修改
# 切片反转返回新列表：
nums = [1, 2, 3, 4, 5]
rev = nums[::-1]
print(nums)              # [1, 2, 3, 4, 5]  原列表不变
print(rev)               # [5, 4, 3, 2, 1]

#其他常用方法速查
#方法,        说明,       示例
#len(list),获取长度,"len([1,2,3]) → 3"
#list.index(x),查找元素第一次出现的索引,"[1,2,3].index(2) → 1"
#list.count(x),统计元素出现次数,"[1,2,2,3].count(2) → 2"
#list.copy(),浅拷贝（等效于 [:]）,a.copy()
#max(list),最大值,"max([1,5,3]) → 5"
#min(list),最小值,"min([1,5,3]) → 1"
#sum(list),求和（元素须为数字）,"sum([1,2,3]) → 6"


