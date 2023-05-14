from tkinter import *

root = Tk()
root.title('chamoy')
root.geometry('600x400')
root.config( bg='blue',cursor='umbrella')

# miframe = Frame(root) 
# miframe.grid() 
# miframe.config(
#     width=200,
#     height=200,
#     bg='green',
#     cursor='man'
# )

Labelnombre = Label (root,text= 'ingresa tu nombre')
Labelnombre.grid(row=0,column=0)

Label1 = Label(root)
Label1.grid(row=1,column=1)




imagen = PhotoImage(file = 'IMG/images.png')
Label1.config(image=imagen)


inputName = Entry(root) 
inputName.grid(row=2 ,column=1)
inputName.config(font=('tahoma','20' ))


btnGuardar = Button(root,text='guardar')
btnGuardar.grid(row=3, column=1)

root.mainloop()

#
#
#
#