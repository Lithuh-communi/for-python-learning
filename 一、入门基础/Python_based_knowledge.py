#数值类型
name = "小明"      # 字符串
age = 18           # 整数
height = 1.75      # 浮点数
is_student = True  # 布尔值
score = None       # 空值

#类型	英文名	       示例
#整数	int	           42, -10, 0
#浮点数	float	       3.14, -0.5, 1e3
#字符串	str	           "你好", 'Python'
#布尔值	bool	       True, False
#空值	NoneType	   None
#复数	complex	       3+4j

print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hi"))      # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>

int("42")       # 42         字符串 → 整数
float("3.14")   # 3.14       字符串 → 浮点数
str(100)        # "100"      整数 → 字符串
bool(1)         # True       非零 → True
bool(0)         # False      零 → False
bool("")        # False      空字符串 → False
bool("abc")     # True       非空字符串 → True

# ⚠️ 常见错误：字符串内不是合法数字会报错
int("hello")    # ValueError: invalid literal for int()

#end


#输入与输出

print("Hello")                # 基本输出
print(1, 2, 3)               # 1 2 3 （默认空格分隔）
print(1, 2, 3, sep="-")      # 1-2-3 （自定义分隔符）
print("A", end="")            # 不换行
print("B")                    # AB

#f-string
name = "Alice"
age = 25
print(f"我叫{name}，今年{age}岁。")
# 输出：我叫Alice，今年25岁。

#input()  
# 等待用户输入，返回字符串
name = input("请输入你的名字：")   # 返回字符串
age = input("请输入年龄：")        # 也是字符串！

#⚠️ input() 永远!!!返回字符串!!!，需要数值必须手动转换
age_str = input("年龄：")
age = int(age_str)
# 或一步到位：
age = int(input("年龄："))

#算术运算符
a = 10
b = 3
a + b   # 13    加
a - b   # 7     减
a * b   # 30    乘
a / b   # 3.333...  除（结果总是 float）
a // b  # 3     整除（向下取整）
a % b   # 1     取余
a ** b  # 1000  幂运算

#比较运算符（结果：True / False）
a = 5
b = 10
a == b   # False   等于
a != b   # True    不等于
a < b    # True    小于
a > b    # False   大于
a <= b   # True    小于等于
a >= b   # False   大于等于

#逻辑运算符
True and True     # True   且（两边都真才真）
True and False    # False
True or False     # True   或（一边真就真）
False or False    # False
not True          # False  非（取反）
not False         # True

#运算符	   等价于
x = 5    ;x = 5
x += 3	;x = x + 3
x -= 3	;x = x - 3
x *= 3	;x = x * 3
x /= 3	;x = x / 3
x //= 3	;x = x // 3
x %= 3	;x = x % 3
x **= 3	;x = x ** 3

# ┌─────────────────────────────────────────────┐
# │            🐍 Python 基础速查                │
# ├─────────────────────────────────────────────┤
# │ 类型     type(x)     示例                    │
# │ ─────── ───────────  ─────                  │
# │ int     整数         42, -10                │
# │ float   浮点数       3.14, 1e5              │
# │ str     字符串       "Hi", 'Python'         │
# │ bool    布尔值       True, False            │
# │ None    空值         None                   │
# ├─────────────────────────────────────────────┤
# │ 转换：int(x) float(x) str(x) bool(x)       │
# │ input() 永远返回 str                        │
# │ f-string:  f"值={x:.2f}"                   │
# ├─────────────────────────────────────────────┤
# │ 算术: + - * / // % **                      │
# │ 比较: == != < > <= >=                      │
# │ 逻辑: and or not                           │
# │ 赋值: = += -= *= /= //= %= **=             │
# └─────────────────────────────────────────────┘