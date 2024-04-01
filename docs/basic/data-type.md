# 检测类型

最直接和简单的方法就是用 `type`

```py
# int 
number = 1
print(type(number)) # <class 'int'>
# float
floatNum = 1.222
print(type(floatNum)) # <class 'float'>
# str
strs = "Hello World"
print(type(strs)) # <class, 'str'>
# list
a = [1, 2, 3]
print(type(a)) # <class, 'list>
# tuple
c = {1, 2, 3}
print(type(c)) # <class, 'tuple'>
# 'dict'
d = {"name": "Alice", 'age': 25}
print(type(d)) # <class, 'dict'>
# bool
e = True
print(type(e)) # <class, 'bool'>
```

 此外，如果想判断一个变量是否是特定的数据类型，可以使用`isinstance`函数：
 ```py
x = 5
if isinstance(x, int):
  print("x is a int type")
else:
  print("x is not a int type")
 ```