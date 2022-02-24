from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
root.title('Register Vaksin')
root.resizable(FALSE,FALSE)


file = sqlite3.connect('DatabaseVaksin.db')
c = file.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tabel(
    Nama_depan text,
    Nama_belakang text,
    NIK integer,
    umur integer,
    email text  
)''')

def submit():
    file = sqlite3.connect('DatabaseVaksin.db')
    c = file.cursor()

    c.execute('INSERT INTO tabel VALUEs(:Nama_depan,:Nama_belakang,:NIK,:umur,:email)',
        {
            'Nama_depan':enamadepan.get(),
            'Nama_belakang':enamabelakang.get(),
            'NIK':enik.get(),
            'umur': eumur.get(),
            'email':eemail.get()    
        }
    )
    

    file.commit()
    file.close()
    enamadepan.delete(0,END)
    enamabelakang.delete(0,END)
    enik.delete(0,END)
    eumur.delete(0,END)
    eemail.delete(0,END)
    messagebox.showinfo('Register vaksin','Register berhasil. Data anda disimpan dengan aman')
    

enamadepan=Entry()
enamabelakang=Entry()
enik=Entry()
eumur=Entry()
eemail=Entry()

enamadepan.grid(row=0,column=1)
enamabelakang.grid(row=1,column=1)
enik.grid(row=2,column=1)
eumur.grid(row=3,column=1)
eemail.grid(row=4,column=1)

namadepan=Label(root,text='Nama Depan :').grid(row=0,column=0)
namabelakang=Label(root,text='Nama Belakang :').grid(row=1,column=0)
nik=Label(root,text='NIK :').grid(row=2,column=0)
umur=Label(root,text='Umur :').grid(row=3,column=0)
email=Label(root,text='Email').grid(row=4,column=0)

btn=Button(root,text='Submit',command=submit).grid(row=7,columnspan=2)





file.commit()
file.close()

root.mainloop()