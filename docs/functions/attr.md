在 Python 中， `hasattr`, `getatter`, 和 `setattr` 是用于动态访问和操作对象属性的内置函数。它们可以帮助我们在运行时检查和操作对象的属性。

## `hasattr`
`hasattr`用于检查对象是否具有指定的属性


### 语法
```py
hasattr(object, name)
```
### 参数：
- `object`: 需要检查的对象。
- `name`: 作为字符串的属性名称

### 返回值：
- 如果对象有指定的属性，返回`True`; 否则，返回`False`

```py
class MyClass:
    def __init__(self):
        self.name = "Python"

obj = MyClass()

# 检查对象是否有属性'name'
print(hasattr(obj, 'name'))
# 检查对象是否有属性‘age'
print(hasattr(obj, 'age'))
```


## `getattr`
`getattr` 用于获取对象的属性值，如何属性不存在，还可以提供一个默认值

### 语法
```py
getattr(object, name[,default])
```
### 参数 
- `object`: 需要获取属性的对象
- `name`: 作为字符串的属性名称
- `default`: (可选) 如何属性不存在，返回的默认值
### 返回值
- 返回属性的值。如果属性不存在且提供了默认值，返回默认值；否则抛出 `AttributeError` 异常。
```py
class MyClass:
    def __init__(self):
        self.name = "Python"

obj = MyClass()

# 获取对象的属性 'name'
print(getattr(obj, 'name'))  # 输出: Python

# 尝试获取对象的属性 'age'，并提供默认值
print(getattr(obj, 'age', 25))  # 输出: 25

# 如果属性不存在且未提供默认值，会抛出 AttributeError
print(getattr(obj, 'age'))  # 抛出 AttributeError: 'MyClass' object has no attribute 'age'
```
## `setattr`
`setattr` 用于设置对象的属性值。如果属性不存在，会创建该属性。
### 语法
```py
setattr(object, name, value)
```
### 参数
- `object`: 需要设置属性的对象。
- `name`: 作为字符串的属性名称。
- `value`: 要设置的属性值。
### 返回值
- 无
```py
class MyClass:
    def __init__(self):
        self.name = "Python"

obj = MyClass()

# 设置对象的属性 'name'
setattr(obj, 'name', 'Java')
print(obj.name)  # 输出: Java

# 设置新的属性 'age'
setattr(obj, 'age', 30)
print(obj.age)  # 输出: 30
```