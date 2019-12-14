# 示例1：主窗口及标题

import tkinter as tk

app = tk.Tk()  # 根窗口的实例(root窗口)

app.title('Tkinter root window')  # 根窗口标题

theLabel = tk.Label(app, text='我的第1个窗口程序！')  # label组件及文字内容

theLabel.pack()  # pack()用于自动调节组件的尺寸

app.mainloop()  # 窗口的主事件循环，必须的。
