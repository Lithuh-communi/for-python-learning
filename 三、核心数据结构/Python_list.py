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
print()
print()
print()
print()
print()
print()
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