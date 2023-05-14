
from tkinter import *


root = Tk()
root.title('chamoy')
root.geometry('600x400')


inputName = Entry(root) 
inputName.grid(row=2 ,column=0,columnspan=4, )
inputName.config(font=('tahoma','20' ))

inputName1 = Entry(root) 
inputName1.grid(row=3 ,column=0,columnspan=4,)
inputName1.config(font=('tahoma','20' ))

btn1 = Button(root,text='+',width=10)
btn1.grid(row=4, column=0, padx=5, pady=5)

btn2 = Button(root,text='-',width=10)
btn2.grid(row=4, column=1, padx=5, pady=5)

btn3 = Button(root,text='*',width=10)
btn3.grid(row=4, column=2, padx=5, pady=5)

btn4 = Button(root,text='/',width=10)
btn4.grid(row=4, column=3, padx=5, pady=5)


Label1 = Label (root,text= 'panqueso')
Label1.grid(row=5,column=0,columnspan=4)
Label1.config(font=('tahoma','20' ))





root.mainloop()

