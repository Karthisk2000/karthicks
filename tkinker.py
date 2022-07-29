from tkinter import *
master = Tk()
def callback():
    a = input('Enter the number:')
    b = input('Enter the number:')
    sum = int(a) + int(b)
    print(sum)
   # print('you have clicked the button ')


btn = Button(master,text='ADD VALUE',command = callback)

btn.pack()
mainloop()


