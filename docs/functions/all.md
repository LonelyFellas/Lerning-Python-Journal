学习了`all`函数的用法

`all`函数的作用是判断一个可迭代对象中的所有元素是否都为`True`，如果是则返回`True`，否则返回`False`。

```py
var = 1
condition = [
    var == 1,
    type(var) == int,
    var > 0,
    var < 10
]

if all(condition):
    print("All conditions are true") // the output to here and All conditions are true
else:
    print("At least one condition is false")
```