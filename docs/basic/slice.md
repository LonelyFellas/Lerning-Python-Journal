# 关于 List 的切片


在Python中，切片是一种强大的工具，可以用来访问序列（如列表、元组和字符串）中的一部分。切片语法在Python 3中依然沿用了Python 2中的语法，但Python 3对某些操作的行为和性能进行了改进。下面是Python 3中切片的基本用法和一些示例

## 基础语法

```python3
sequence[start:stop:step]
```

* `start` 是切片的起始索引（包含）
* `stop`  是切片的结束索引（不包含）
* `stop`  是步长，默认为 1

## 示例
1. 基础切片操作

```py3
# 示例列表
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 从索引2到索引5的元素（不包含索引5）
sub_list = numbers[2:5]
print(sub_list)  # 输出: [2, 3, 4]

# 从索引0到索引5的元素，每隔一个取一个
sub_list_step = numbers[0:6:2]
print(sub_list_step)  # 输出: [0, 2, 4]

# 从索引3到列表末尾的所有元素
sub_list_from_3 = numbers[3:]
print(sub_list_from_3)  # 输出: [3, 4, 5, 6, 7, 8, 9]

# 从列表开头到索引4的所有元素
sub_list_to_4 = numbers[:5]
print(sub_list_to_4)  # 输出: [0, 1, 2, 3, 4]

```