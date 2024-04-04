print(3 * 2)
print("Hello World!" * 3)

def pack(*args): 
  ans = 0
  for arg in args:
    print(arg)
    ans += arg
  print(ans)
pack(1, 2, 3)

list1 = [1, 2, 3, 4, 5, 6]
first, *mid, last = list1
print(first)
print(last)
print(mid)

def pack(**dict):
  print(dict)
pack(name='darwish', age = 22)

print(('darwish', 33) * 3)