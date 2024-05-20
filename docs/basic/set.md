# `set` 类型

`set` 类型是一个无序不重复元素的集合。

## 定义一个空的`set`

```python
# 定义一个空的 set
my_set = set()

# 或者使用大括号
my_set = {}
```

## 定义一个有元素的`set`

```python
# 定义一个有元素的 set
my_set = {1, 2, 3, 4, 5}


# 或者使用 set() 函数
my_set = set([1, 2, 3, 4, 5])
```

## 添加元素到`set`

```python
my_set = {1, 2, 3}
# 添加元素到 set
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
```

## 删除元素

```python
my_set = {1, 2, 3}
# 删除元素
my_set.remove(2)
print(my_set)  # {1, 3}
```

## 检查元素是否在set中

```python
my_set = {1, 2, 3}
# 检查元素是否在 set 中
print(1 in my_set)  # True
print(4 in my_set)  # False
```

## 遍历`set`中的元素

```python
my_set = {1, 2, 3}
# 遍历 set 中的元素
for item in my_set:
    print(item)
```

## 集合操作

```python
# 并集
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # {1, 2, 3, 4}


# 交集
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # {2, 3}


# 差集
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}


# 对称差集
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)  # {1, 4}
```

## 集合推导式

```python
# 集合推导式
my_set = {x for x in range(1, 6) if x % 2 == 0}
print(my_set)  # {2, 4}
```

