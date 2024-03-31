最近发现了一个小track

比较一下当前两段代码的输出
```py
print("program start ....")
n = 1

while n < 10:
  n += 1
  print("n: ", n)
else:
  print("program accoss 'else' end ...")

"""
output:
program start ....
n:  2
n:  3
n:  4
n:  5
n:  6
n:  7
n:  8
n:  9
n:  10
program accoss 'else' end ...
"""
```

```py
print("program start ...")
n = 1

while n < 10:
  n += 1
  print("n: ", n)
  if n > 8:
    break
else:
  print("progam accoss 'else' end ...")
"""
program start ...
n:  2
n:  3
n:  4
n:  5
n:  6
n:  7
n:  8
n:  9
"""
```
区别在于这个`break`, 如果是中断的`break`或者`continue`, 则程序不会走`else`的区域的语句
