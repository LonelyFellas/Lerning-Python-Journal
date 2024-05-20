# `dict` 类型

`dict` 类型是 Python 中唯一的内置映射类型。它是一个无序的键值对集合，其中每个键都是唯一的，值可以是任意类型。



## 创建空的`dict`
```python
# 使用{}定义
my_dict = {}

# 使用 dict() 函数
my_dict = dict()
```

## 创建一个有元素的`dict` 
```python
# 使用{}定义
my_dict = {
  "key1": "value1",
  "key2": "value2", 
  "key3": "value3"
}
# 使用 dict() 函数
my_dict = dict(key1="value1", key2="value2", key3="value3")
```

## 添加和更新元素到`dict`
```python
my_dict = {}

# 添加元素
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"
my_dict["key3"] = "value3"

# 更新元素
my_dict["key1"] = "new_value1"
```

## 删除元素
```python
# 删除键值对
# 使用del关键字
del my_dict["key1"]

# 使用pop()方法
my_dict.pop("key2")

# 使用popitem()方法
my_dict.popitem()

```

## 检查键是否在`dict`中
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# 使用 in 关键字
if "key1" in my_dict:
  print("key1 is in my_dict")

# 使用 get() 方法
value = my_dict.get("key2")
if value:
  print("key2 is in my_dict and its value is", value)
```


## 遍历`dict`
```python 
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# 遍历键
for key in my_dict:
  print(key)


# 遍历值
for value in my_dict.values():
  print(value)


# 遍历键值对
for key, value in my_dict.items():
  print(key, value)
```

## 获取`dict`的元素
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# 获取键值对数量
print(len(my_dict))

# 获取所有键
print(my_dict.keys())

# 获取所有值
print(my_dict.values())

# 获取所有键值对
print(my_dict.items())

# 获取指定键的值
value = my_dict.get("key2")
print(value) // "value2"

# 获取指定键的值，如果不存在，则返回默认值
value = my_dict.get("key4", "default_value")
print(value) // "default_value"
```

## 合并`dict`
```python
my_dict1 = {"key1": "value1", "key2": "value2"}
my_dict2 = {"key3": "value3", "key4": "value4"}

# 合并
my_dict1.update(my_dict2)
print(my_dict1) // {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
```

## 字典推导式

字典推导式是一种简洁的创建字典的方法。

```python
# 字典推导式
my_dict = {x: x**2 for x in range(1, 6)}
print(my_dict) // {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 字典推导式嵌套
my_dict = {x: {y: y**2 for y in range(1, 4)} for x in range(1, 4)}
print(my_dict) // {1: {1: 1, 2: 4, 3: 9}, 2: {1: 1, 2: 4, 3: 9}, 3: {1: 1, 2: 4, 3: 9}}
```


## 其他方法

- `clear()`：清空`dict`
- `copy()`：复制`dict`
- `fromkeys()`：从指定键值对创建`dict`
- `update()`：更新`dict`
- `setdefault()`：设置默认值
- `pop()`：删除指定键值对
- `popitem()`：随机删除键值对
- `keys()`：获取所有键
- `values()`：获取所有值
- `items()`：获取所有键值对
- `update()`：更新`dict`
- `get()`：获取指定键的值
- `len()`：获取键值对数量
- `str()`：返回`dict`的字符串表示
- `repr()`：返回`dict`的可读字符串表示
- `cmp()`：比较两个`dict`是否相同
- `sorted()`：对`dict`进行排序
- `reversed()`：反转`dict`
- `has_key()`：判断键是否存在
- `iterkeys()`：返回键的迭代器
- `itervalues()`：返回值的迭代器
- `iteritems()`：返回键值对的迭代器
- `viewkeys()`：返回键的视图对象
- `viewvalues()`：返回值的视图对象
- `viewitems()`：返回键值对的视图对象


