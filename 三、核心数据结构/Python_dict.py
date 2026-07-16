#📖 Python 字典（dict）完全指南
#——————————————————————————————————————————————————————————————————————————————————————————————————
#一、什么是字典？
#字典是 Python 中键值对（key-value）的无序集合，用 {} 花括号表示。
#每个元素由 键: 值 组成，键必须唯一且不可变（字符串、数字、元组），值可以是任意类型。
#——————————————————————————————————————————————————————————————————————————————————————————————————
# 基本示例
student = {"name": "小明", "age": 18, "score": 95.5}
empty = {}                # 空字典
mixed = {1: "one", "two": 2, (1,2): "tuple_key"}

#student 字典结构图：
#┌──────────┬──────────┐
#│  键 Key  │ 值 Value │
#├──────────┼──────────┤
#│# "name"  │ "小明"   │
#│ "age"    │ 18       │
#│ "score"  │ 95.5     │
#└──────────┴──────────┘
#————————————————————————————————————————————————————————————————————————————————————————————————————

#二、增删改查（CRUD）
#📖 查（Read）
#方式一：dict[key] — 直接索引（❌键不存在会报错）
student = {"name": "小明", "age": 18, "score": 95.5}

print(student["name"])    # 小明
print(student["age"])     # 18
# print(student["grade"]) # ❌ KeyError: 'grade'

#方式二：dict.get(key, default) — 安全获取（✅推荐）
print(student.get("name"))           # 小明
print(student.get("grade"))          # None（不报错！）
print(student.get("grade", "未知"))  # "未知"（指定默认值）
# 为什么推荐 get()？ 避免程序因 KeyError 崩溃
#检查键是否存在：
print("name" in student)     # True
print("grade" in student)    # False

#——————————————————————————————————————————————————————————————————————————————————————————————
#✏️ 改（Update）
student = {"name": "小明", "age": 18, "score": 95.5}

student["age"] = 19         # 修改已有键的值
print(student)              # {'name': '小明', 'age': 19, 'score': 95.5}

# update() — 批量更新/合并
student.update({"score": 98, "grade": "A"})
print(student)              # {'name': '小明', 'age': 19, 'score': 98, 'grade': 'A'}

#➕ 增（Create / Add）
student = {"name": "小明", "age": 18}

# 直接赋值 — 键不存在就是新增
student["score"] = 95.5     # 新增键 "score"
print(student)              # {'name': '小明', 'age': 18, 'score': 95.5}

# setdefault(key, default) — 键不存在才插入
student.setdefault("gender", "男")
print(student)              # {'name': '小明', 'age': 18, 'score': 95.5, 'gender': '男'}
# 如果键已存在，setdefault 不会覆盖
student.setdefault("gender", "女")
print(student["gender"])    # 还是"男"

#————————————————————————————————————————————————————————————————————————————————————————

#🗑️ 删（Delete）
student = {"name": "小明", "age": 18, "score": 95.5, "grade": "A"}

# 1. pop(key) — 弹出并返回指定键的值
score = student.pop("score")
print(score)               # 95.5
print(student)             # {'name': '小明', 'age': 18, 'grade': 'A'}

# pop() 可以设默认值防止报错
# student.pop("xxx")       # ❌ KeyError
print(student.pop("xxx", "不存在"))  # "不存在" ✅

# 2. del 语句 — 删除指定键
del student["grade"]
print(student)             # {'name': '小明', 'age': 18}

# 3. popitem() — 弹出并返回 (键, 值) 对（Python 3.7+ 返回最后插入的）
student["score"] = 98
pair = student.popitem()
print(pair)                # ('score', 98)

# 4. clear() — 清空所有键值对
student.clear()
print(student)             # {}

#————————————————————————————————————————————————————————————————————————————————



#三、遍历字典
#——————————————————————————————————————————————————————————————————————————————————
#🔄 三种遍历方式
student = {"name": "小明", "age": 18, "score": 95.5}

# 1. 遍历键（默认）
for key in student:              # 等同于 for key in student.keys():
    print(key, end=" ")          # name age score

print()

# 2. 遍历值
for value in student.values():
    print(value, end=" ")        # 小明 18 95.5

print()

# 3. 遍历键值对（最常用！）
for key, value in student.items():
    print(f"{key} → {value}")

# 输出：
# name → 小明
# age → 18
# score → 95.5

#————————————————————————————————————————————————————————————————————————————————————

#🌟 items() 详解
#items() 返回一个视图对象，包含所有 (key, value) 元组：
student = {"name": "小明", "age": 18}
items = student.items()
print(items)            # dict_items([('name', '小明'), ('age', 18)])

# 可以转成列表
print(list(items))      # [('name', '小明'), ('age', 18)]

# 视图是动态的 → 修改原字典，视图也会变
student["score"] = 98
print(list(items))      # [('name', '小明'), ('age', 18), ('score', 98)]

#————————————————————————————————————————————————————————————————————————————————————




#四、字典推导式（Dict Comprehension）
#📐 语法：{key_expr: value_expr for item in iterable if condition}
# 1. 基础：平方数字典
squares = {x: x**2 for x in range(1, 6)}
print(squares)          # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. 带条件：只保留偶数
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)     # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 3. 键值互换（要求值是可哈希的）
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)          # {1: 'a', 2: 'b', 3: 'c'}

# 4. 字符串处理：统计单词长度
words = ["apple", "banana", "cat", "dog"]
word_len = {w: len(w) for w in words}
print(word_len)         # {'apple': 5, 'banana': 6, 'cat': 3, 'dog': 3}

# 5. 从两个列表创建字典
keys = ["name", "age", "score"]
vals = ["小红", 20, 92]
student = {k: v for k, v in zip(keys, vals)}
print(student)          # {'name': '小红', 'age': 20, 'score': 92}

#————————————————————————————————————————————————————————————————————————————————————



#                           五、常用方法速查卡
#     方法	                   说明	                              示例
# dict.get(k, d)	    安全取值，键不存在返回默认值 d	        d.get("x", 0)
# dict.items()	        返回 (键, 值) 视图	                  for k,v in d.items()
# dict.keys()	        返回所有键的视图	                   list(d.keys())
# dict.values()	        返回所有值的视图	                   list(d.values())
# dict.update(d2)	    合并另一个字典	                       d.update({"a":1})
# dict.pop(k, d)	    弹出指定键的值	                       d.pop("x", None)
# dict.popitem()	    弹出最后一个键值对	                   k, v = d.popitem()
# dict.setdefault(k, v)	键不存在则插入	                       d.setdefault("x", 0)
# dict.clear()	        清空字典	                           d.clear()
# key in dict	        检查键是否存在	                       "name" in d
# len(dict)	            获取键值对数量	                        len(d)
#——————————————————————————————————————————————————————————————————————————————————————





#六、字典 vs 列表 对比
# 特性	    列表 list	            字典 dict
# 结构	    有序索引序列	         键值对映射
# 访问方式	 list[0]（整数索引）	  dict["key"]（键访问）
# 查找速度	 O(n) 线性查找	          O(1) 哈希查找 ✅
# 元素顺序	 ✅ Python 3.7+ 有序	    ✅ Python 3.7+ 有序
# 可变性	 ✅	                    ✅
# 适用场景	  有序集合、堆栈、队列	    映射关系、配置文件、缓存