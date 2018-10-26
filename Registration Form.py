# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:23:12 2018

@author: Mahesh
"""

from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("SRM Student Enrollment Form")


Fullname=StringVar()
Reg=StringVar()
Yr = IntVar()
Sec=StringVar()
Campus=StringVar()
Dept= StringVar()



def database():
   name=Fullname.get()
   regno=Reg.get()
   year=Yr.get()
   sec=Sec.get()
   dept=Dept.get()
   campus=Campus.get()
   print(name,regno,year,sec,dept,campus)
   conn = sqlite3.connect('Form.db')
   with conn:
      print("Done")
      cursor=conn.cursor()
   #cursor.execute('CREATE TABLE IF NOT EXISTS StudentEnroll ( Name TEXT, RegNo TEXT, Year INTEGER, Sec TEXT, Dept TEXT, Campus TEXT )')
   cursor.execute('INSERT INTO StudentEnroll ( Name, RegNo, Year, Sec, Dept, Campus) VALUES(?,?,?,?,?,?)',(name,regno,year,sec,dept,campus))
   conn.commit()
   
   
             
label_0 = Label(root, text="Student Enrollment Form",width=20,font=("bold", 20))
label_0.place(x=90,y=50)


label_1 = Label(root, text="Full Name:",width=20,font=("bold", 10))
label_1.place(x=70,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Registration Number:",width=20,font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root,textvar=Reg)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Year:",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="1",padx = 5, variable=Yr, value=1).place(x=240,y=230)
Radiobutton(root, text="2",padx = 20, variable=Yr, value=2).place(x=275,y=230)
Radiobutton(root, text="3",padx = 20, variable=Yr, value=3).place(x=325,y=230)
Radiobutton(root, text="4",padx = 20, variable=Yr, value=4).place(x=375,y=230)

label_4 = Label(root, text="Section:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

entry_3 = Entry(root,textvar=Sec)
entry_3.place(x=240,y=280)

label_5 = Label(root, text="Department:",width=20,font=("bold", 10))
label_5.place(x=70,y=330)

list1 = ['CSE','ECE','MECH','IT','EEE','CIVIL'];

droplist=OptionMenu(root,Dept, *list1)
droplist.config(width=20)
Dept.set('Select Your Department')
droplist.place(x=240,y=330)

label_6 = Label(root, text="Campus:",width=20,font=("bold", 10))
label_6.place(x=70,y=370)

Radiobutton(root, text="VDP", variable=Campus,value='VDP').place(x=240,y=370)

Radiobutton(root, text="KTR", variable=Campus,value='KTR').place(x=300,y=370)

Radiobutton(root, text="RMP", variable=Campus,value='RMP').place(x=350,y=370)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)

root.mainloop()
