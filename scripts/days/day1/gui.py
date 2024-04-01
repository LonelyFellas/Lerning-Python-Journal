import tkinter as tk
# 创建主窗口
root = tk.Tk()

# 设置窗口标题
root.title("Hello World")

# 创建一个标签
label = tk.Label(root, text="Hello, world!")

# 获取屏幕的尺寸信息
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# 初始化你想设定的窗口尺寸
windowWidth = 800
windowHeight = 600

# 计算 x 和 y 坐标
x = (screenWidth - windowWidth) // 2
y = (screenHeight - windowHeight) // 2

root.geometry(f'{windowWidth}x{windowHeight}+{x}+{y}')
label.pack()

# 进入主事件循环
root.mainloop()