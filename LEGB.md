# Python作用域

## 作用域法则
函数定义本子作用域，模块定义的全局作用域。这两个作用域有如下关系：

* 内嵌的模块是全局作用域，每个模块都是一个全局作用域。对于模块外部来说，该模块的全局变量就成为了这个模块对象的属性，但是这个模块中能够像简单的变量一样使用。
* 全局作用域的作用范围仅限于单个文件，这里的全局指的是在一个文件的顶层的变量名仅对于这个文件内部的代码而言是全局的。在python中是没有基于一个单个的、无所不包的情景文件的全局作用域的。
* 每次对函数的调用都创建了一个新的本地作用域
* 赋值的变量名除非生命为全局变量或非局部变量，否则均为局部变量
* 所有的变量名都可以归纳为本地、全局或者内置的

## LEGB原则
Python的变量名解析机制有时称为LEGB法则，当在函数中使用未认证的变量名时，Python搜索四个作用域

* 本地作用域(L)
* 上一层结构中def 或 lambda的本地作用域(E)
* 全局作用域(G)
* 最后是内置作用域(B)

Python按顺序在上面4个作用域中查找变量，并且在第一个能够找到这个变量名的地方停下来，如果在这4个作用域中都没有找到，Python会报错。

上面4个作用域是函数中代码的搜索过程，也就是说，在函数中能直接使用上一层中的变量！

```Python
s = 10
    def time(x,y):
    x=s
    return x*y

time(3,4) # return 40 not 12
```

## 内置作用域

内置作用域是通过一个名为builtin的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量：

```Python
import builtins
dir(builtins)
```

因此，事实上有两种方法可以引用一个内置函数：通过LEGB法则带来的好处，或者手动导入builtin模块。其中第二种方法在一些复杂的任务里是很有用的，因为一些局部变量有可能会覆盖内置的变量或函数。在此强调的是，LEGB法则只使它找到的第一处变量名的地方生效！

# global语句

global语句是一个命名空间的生命，它告诉python解释器打算生成一个或多个全局变量，也就是说，存在这个模块内部作用域(命名空间)的变量名。关于全局变量名：

* 全局变量是位于模块文件内部顶层的变量名。
* 全局变量如果是在函数内部被赋值的话，必须经过生命，
* 全局变量名在函数的内部不经过生命也可以被引用。

global语句包含了关键字global，其后跟着一个或多个由逗号分开的变量名。当在函数主题被赋值或者引用时，所有列出来的变量名将被影射到整个模块的作用域内。

```Python
X = 88
def func():
    global X
    x = 99
func()
print(x) # prints 99
```

# 作用域和嵌套函数

这部分内容是关于LEGB查找法则中E这一层的，它包括了任意嵌套函数内部的本地作用域。嵌套作用域有时也叫做静态嵌套作用域。实际上，嵌套是一个语法上嵌套的作用域，它是对应于程序源代码的物理结构上的嵌套结构。

## 嵌套作用域的细节

对于一个函数来说：

* 一个引用(x)首先在本地(函数内)作用域查找变量名x;之后会在代码的语法上嵌套了的函数中的本地作用域，从内到外查找；只有查找当前的全局作用域(模块文件)；最后在内置作用域内(模块builtin)。全局生命将会直接从全局(模块文件)作用域进行搜索。其实就是从引用x的地方开始，一层一层往上搜索，直到找到的第一个x。
* 在默认情况下，一个赋值(x=value)创建或修改了变量名x的当前作用域。如果x在函数内部声明为全局变量，它将会创建或改变变量名x为整个模块的作用域。另一方面，如果x在函数内部声明为nonlocal，赋值会修改最近的嵌套函数的本地作用域中的名称x。

## 嵌套作用域举例

```Python
x = 99
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1() # prints 88
```

```Python
x = 99
def f1():
    x = 88
    def f2()
        print(x)
    return f2
action = f1()
achtion() # print 88
```

工厂函数

上述这些行为有时叫做闭合(closure)或者工厂函数--一个能够记住嵌套作用域的变量值的函数，即使那个作用域也许已经不存在了。通常来说，使用类来记录状态信息时更好的选择，但是像这样的工厂函数也提供了一种替代方案。具体的例子：

```Python
def maker(N):
    def action(N):
        return X ** N
    return action
f = maker(2) # pass 2 to N
f(3) # pass 3 to X, N remembers 2: 3**2,Return 9
f(4) # return 4 ** 2

g = maker(3) # g remembers 3, femembers 2
g(3) # return 27
f(3) # return 9
```

f和g函数分别记录了不同的N值，也就是记录了不同的状态，每一次对这个工厂函数进行赋值，都会得到一个状态信息的集合，每个函数都有自己的状态信息，由maker中的变量N保持。

作用域与带有循环变量的默认参数相比较

在已给出的法则中有一个值得注意的特例：如果lambda或者def在函数中定义，嵌套在一个循环之中，并且嵌套的函数引用了一个上层作用域的变量，该变量被循环所改变，所有在这个循环中产生的函数都将会有相同的值--在最后一次循环中完成被引用变量的值。具体的例子：

```Python
def makeActions():
    acts=[]
    for i in range(5):
        acts.append(lambda x,i=i: i**x)
    return acts
```

# nonlocal语句

在python3.0中，我们也可以修改嵌套作用域变量，只要我们在一条nonlocal语句中声明它们。使用这条语句，嵌套的def可以对嵌套函数中的名称进行读取和写入访问。nonlocal应用于一个嵌套的函数的作用域中的一个名称，而不是所有def之外的全局模块作用域--它们可能只存在于一个嵌套的函数中，并且不能由一个嵌套的def中第一次赋值创建。
换句话说，nonlocal即允许对嵌套的函数作用域中的名称变量赋值，并且把这样的名称作用域查找限制在嵌套的def。

```Python
def func():
    nonlocal name1,name2...
```


