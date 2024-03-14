# Họ và tên sinh viên   : Lê Sỹ Anh Tấn
# Mã số sinh viên       : B2113342
# STT                   : 38

from tkinter import *
from Handle.Code import *

 
window = Tk()
window.title("Welcome To ATBMTT")

label1 = Label(window , text=" " ,font=("Arial Bold", 10) )
label1.grid(column= 0 , row= 0)
title = Label(window , text="Chương Trình Băm" ,font=("Arial Bold", 20) )
title.grid(column=1 , row= 0)

label2 = Label(window , text="Văn Bản" ,font=("Arial Bold", 15) )
label2.grid(column= 0 , row= 1)
text = Entry(window , width= 15)
text.grid(column=1 , row= 1)

radioLabel = LabelFrame(window , text="Hàm Băm")
radioLabel.grid(column=1 , row=2)
hashmode = IntVar()
hashmode.set(-1)

MD5_function = Radiobutton(
    radioLabel ,
    text= "Hash MD5" ,
    font= ("Arial Bold", 10) , 
    variable= hashmode ,
    value= 0 ,
    width= 15 , 
    command= lambda : hasing(text , hash , hashmode= hashmode.get())
    )
MD5_function.grid(column=0 , row= 0)

SHA1_function = Radiobutton(
    radioLabel ,
    text= "Hash SHA1" ,
    font= ("Arial Bold", 10) , 
    variable= hashmode ,
    value= 1 ,
    width= 15 ,
    command= lambda : hasing(text , hash , hashmode= hashmode.get())
    )
SHA1_function.grid(column=0 , row= 1)

SHA256_function = Radiobutton(
    radioLabel ,
    text= "Hash SHA256" ,
    font= ("Arial Bold", 10) , 
    variable= hashmode ,
    value= 2 ,
    width= 15 , 
    command= lambda : hasing(text , hash , hashmode= hashmode.get())
    )
SHA256_function.grid(column=0 , row= 2)

SHA512_function = Radiobutton(
    radioLabel ,
    text= "Hash SHA512" ,
    font= ("Arial Bold", 10) , 
    variable= hashmode ,
    value= 3 ,
    width= 15 ,
    command= lambda : hasing(text , hash , hashmode= hashmode.get())

    )
SHA512_function.grid(column=0 , row= 3)

label3 = Label(window , text="Giá Trị Băm" ,font=("Arial Bold", 15) )
label3.grid(column= 0 , row= 3)
hash = Entry(window , width= 15)
hash.grid(column=1 , row= 3)

title = Button(window , text="Quit" , command=window.quit)
title.grid(column=1 , row= 10)

window.geometry("500x500")
window.mainloop()
