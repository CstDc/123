import tkinter as tk
from tkinter import messagebox

# 创建窗口对象
window = tk.Tk()
window.title("输入名字和密码")

# 创建标签和输入框
name_label = tk.Label(window, text="名字:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

password_label = tk.Label(window, text="密码:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# 定义按钮点击事件处理函数
def on_submit():
    name = name_entry.get()
    password = password_entry.get()
    message = "您输入的名字是：" + name + "\n您输入的密码是：" + password
    messagebox.showinfo("提示", message)

# 创建提交按钮
submit_button = tk.Button(window, text="提交", command=on_submit)
submit_button.pack()

# 运行主循环
window.mainloop()
