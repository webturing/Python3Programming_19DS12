from tkinter import *

def add(va, vb, vc):
    vc.set(va.get() + vb.get())

def quit(root):
    root.destroy()

window = Tk() ## Window
frame = Frame(window)
frame.pack()

va = DoubleVar()
va.set(0.0)
vb = DoubleVar()
vb.set(0.0)
vc = DoubleVar()
vc.set(0.0)

entry = Entry(frame, textvariable=va)
entry.pack()
label = Label(frame, text="+")
label.pack()
entry = Entry(frame, textvariable=vb)
entry.pack()
button = Button(frame, text='=', command=lambda: add(va, vb, vc))
button.pack()
label = Label(frame, textvariable=vc)
label.pack()
exit = Button(frame, text='Quit', command=lambda: quit(window))
exit.pack()


window.mainloop()
