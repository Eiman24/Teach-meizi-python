# 给妹子讲python
# S01E18

# 1.变量的四种作用域
# 2.函数变量的LEGB作用域搜索机制
# 3.利用global关键字进行全局变量修改

#--------------------------------------------------#

# 变量的作用域完全是由变量在程序文件中源代码的位置而决定，而不是由函数调用决定。
# 全局变量
x = 99
def func():
	# 本地变量
	x = 88
	print(x)

func()
print(x)

# LEGB，即L本地作用域，E内嵌作用域，G全局作用域和B内置作用域。
# 全局作用域的作用范围仅限于单个文件，变量名由模块文件隔开，
# 并且必须精确的导入一个模块文件才能够使用这个文件中使用的变量名。

# 不需要全局变量声明
x = 99
def func(y):
	z = x + y
	return z

print(func(1))

# 当在python中使用某个变量名时，python按照L-E-G-B的顺序依次搜索四个作用域
def func():
	open = 1
	open('test.txt')
# 本地作用域中的变量名open就覆盖了内置作用域中的变量名open，报错
# func()

# 声明变量命名空间，可以在函数内部修改全局变量
x = 88
def func():
	global x
	x = 99

func()
print(x)

# x,y,z都是全局变量
x, y, z = 1, 2, 3

def all_global():
	global x
	x = y + z

all_global()
print(x)


#--------------------------------------------------#
