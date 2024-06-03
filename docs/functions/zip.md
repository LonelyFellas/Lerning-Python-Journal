# `zip`

`zip` 函数在 python 中用于将多个可迭代对象（如列表，元组，字符串等）“压缩” 在一起，生成一个由元组组成的迭代器，每个元组包含来自每个输入迭代对象的一个元素。


## 基本用法
假设我们有两个列表：

```py
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]


# 多个可迭代的对象
list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))  # [(1, 'a', True), (2, 'b', False), (3, 'c', True)]


# 长度不同时的行为
list4 = [10, 20]
zipped = zip(list1, list4)
print(list(zipped))  # [(1, 10), (2, 20)] 

# 解压缩
zipped = zip(list1, list2, list3)
list1_unzipped, list2_unzipped, list3_unzipped = zip(*zipped)
print(list1_unzipped)
print(list2_unzipped)
print(list3_unzipped)
```

