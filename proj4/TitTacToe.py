from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("X O")

# 棋盘现况
chessboard = ['', '', '', '', '', '', '', '', '']
# 胜局数组
winchess = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


# 判断胜负
def judge():
    print(chessboard)

    w = 0
    for c in chessboard:
        if c.strip():
            w += 1
    if w < 3: return

    for win in range(0, len(winchess)):
        if chessboard[winchess[win][0]] == chessboard[winchess[win][1]] == chessboard[winchess[win][2]] and chessboard[
            winchess[win][0]].strip():
            messagebox.showinfo(title='结果', message='%s胜' % chessboard[winchess[win][0]])
            return
        elif w == 9:
            messagebox.showinfo(title='结果', message='平局')
            return


# 更新棋盘 ,先手为“X”后手为“O”
def rebtn_1():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_1['text'] = 'O'
    else:
        button_1['text'] = 'X'
    button_1['state'] = 'disabled'
    chessboard[0] = button_1['text']
    judge()


def rebtn_2():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_2['text'] = 'O'
    else:
        button_2['text'] = 'X'
    button_2['state'] = 'disabled'
    chessboard[1] = button_2['text']
    judge()


def rebtn_3():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_3['text'] = 'O'
    else:
        button_3['text'] = 'X'
    button_3['state'] = 'disabled'
    chessboard[2] = button_3['text']
    judge()


def rebtn_4():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_4['text'] = 'O'
    else:
        button_4['text'] = 'X'
    button_4['state'] = 'disabled'
    chessboard[3] = button_4['text']
    judge()


def rebtn_5():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_5['text'] = 'O'
    else:
        button_5['text'] = 'X'
    button_5['state'] = 'disabled'
    chessboard[4] = button_5['text']
    judge()


def rebtn_6():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_6['text'] = 'O'
    else:
        button_6['text'] = 'X'
    button_6['state'] = 'disabled'
    chessboard[5] = button_6['text']
    judge()


def rebtn_7():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_7['text'] = 'O'
    else:
        button_7['text'] = 'X'
    button_7['state'] = 'disabled'
    chessboard[6] = button_7['text']
    judge()


def rebtn_8():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_8['text'] = 'O'
    else:
        button_8['text'] = 'X'
    button_8['state'] = 'disabled'
    chessboard[7] = button_8['text']
    judge()


def rebtn_9():
    num = 0
    for i in chessboard:
        if i == '':
            num += 1
    if (num % 2) == 0:
        button_9['text'] = 'O'
    else:
        button_9['text'] = 'X'
    button_9['state'] = 'disabled'
    chessboard[8] = button_9['text']
    judge()


# 创建棋盘
button_1 = Button(root, width=13, height=5, cursor='hand2')
button_1['text'] = ''
button_1['command'] = rebtn_1
button_1.grid(row=0, column=0)

button_2 = Button(root, width=13, height=5, cursor='hand2')
button_2['text'] = ''
button_2['command'] = rebtn_2
button_2.grid(row=0, column=1)

button_3 = Button(root, width=13, height=5, cursor='hand2')
button_3['text'] = ''
button_3['command'] = rebtn_3
button_3.grid(row=0, column=2)

button_4 = Button(root, width=13, height=5, cursor='hand2')
button_4['text'] = ''
button_4['command'] = rebtn_4
button_4.grid(row=1, column=0)

button_5 = Button(root, width=13, height=5, cursor='hand2')
button_5['text'] = ''
button_5['command'] = rebtn_5
button_5.grid(row=1, column=1)

button_6 = Button(root, width=13, height=5, cursor='hand2')
button_6['text'] = ''
button_6['command'] = rebtn_6
button_6.grid(row=1, column=2)

button_7 = Button(root, width=13, height=5, cursor='hand2')
button_7['text'] = ''
button_7['command'] = rebtn_7
button_7.grid(row=2, column=0)

button_8 = Button(root, width=13, height=5, cursor='hand2')
button_8['text'] = ''
button_8['command'] = rebtn_8
button_8.grid(row=2, column=1)

button_9 = Button(root, width=13, height=5, cursor='hand2')
button_9['text'] = ''
button_9['command'] = rebtn_9
button_9.grid(row=2, column=2)

root.resizable(width='false', height='false')
root.mainloop()
