# Họ và tên sinh viên   : Lê Sỹ Anh Tấn
# Mã số sinh viên       : B2113342
# STT                   : 38

from tkinter import *

window = Tk()
window.title("Tạo Tài Khoản")

label1 = Label(window , text=" " ,font=("Arial Bold", 10) )
label1.grid(column= 0 , row= 0)
title = Label(window , text="Tạo Tài Khoản" ,font=("Arial Bold", 20) )
title.grid(column=1 , row= 0)

label2 = Label(window , text="Tài Khoản" ,font=("Arial Bold", 15) )
label2.grid(column= 0 , row= 1)
username = Entry(window , width= 15)
username.grid(column=1 , row= 1)

label3 = Label(window , text="Mật Khẩu" ,font=("Arial Bold", 15) )
label3.grid(column= 0 , row= 2)
password = Entry(window , width= 15)
password.grid(column=1 , row= 2)

btn = Button(window , text="Tạo Tài Khoản" , command= window.quit)
btn.grid(column= 1 , row=3)

window.geometry('500x500')
window.mainloop()