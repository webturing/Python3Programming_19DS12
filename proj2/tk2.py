#示例2：按钮

import tkinter as tk

class APP:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.hi_there = tk.Button(frame, text='打招呼', bg='black', fg='white', command=self.say_hi)#Button按钮, command中调用定义的方法
        self.hi_there.pack()
    def say_hi(self):
        print('Wow，居然打了个招呼！~')


root = tk.Tk()

app = APP(root)
if __name__ == '__main__':
    root.mainloop()
