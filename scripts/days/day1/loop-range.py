"""
用for循环实现1~100求和

Version: 0.1
Author: Darwish 
"""

def demo():
  sum = 0
  for x in range(101):
    sum += x
  print(sum)

def demo1():
  sum = 0
  for x in range(100, 2, -2):
    sum += x
  print(sum)

demo1()