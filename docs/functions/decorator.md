在Python中，**装饰器(decorator)** 是一种高级功能，允许开发者在不修改函数或方法本身的情况下，向其添加额外的功能。
装饰器的本质上是一个高阶函数，接受一个函数作为参数，并返回一个新的函数


## 理解装饰器的基础概念
### 1. 高阶函数
高阶函数是指可以接受其他函数作为参数，或者返回一个函数的函数。装饰器利用了这一特性
### 2. 闭包
闭包是指一个函数在其词法作用域之外的引用仍然存在。装饰器通常利用闭包保存被装饰函数的上下文
## 基本装饰器的结构
装饰器通常由三个部分组成：
1. 一个接受函数作为参数的函数
2. 在内部定义一个新函数，包装了原函数并添加额外功能。
3. 返回这个新函数

以下是一个简单的装饰器实例：
```py
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
输出：
```vbnet
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### 带参数的函数--装饰器
装饰器也可以处理带参数的函数。为此，wrapper 函数需要接受参数，并传递给被装饰函数：

示例：
```py
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
输出：
```vbnet
Something is happening before the function is called.
Hello, Alice!
Something is happening after the function is called.
```

### 带参数的函数--装饰器同样也带参数
示例：
```py
def dec(name: str):
    def super_f(f):
        def mini_f(n: str):
            res = f(n)
            return f'{res}, i am {name}'
        return mini_f
    return super_f


@dec('cat')
def print_hi(name):
    return f'Hi, {name}'


@dec('darwish')
def print_hell0(name):
    return f'Hello, {name}'


print(print_hi('PyCharm'))
print(print_hell0("Javascript"))
```
输出：
```vbnet
Hi, PyCharm, i am cat
Hello, Javascript, i am darwish
```

## 装饰器应用实例
### 1.记录函数调用日志
示例：
```py
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 3))
```
输出：
```vbnet
Calling function add
Function add finished
8
```
### 2.计算函数执行时间
示例：
```py
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()
```
输出：
```vbnet
slow_function executed in 2.002 seconds
```

