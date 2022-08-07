#GUI-Caluculator.py

from cgitb import text
from struct import pack
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font

GUI = Tk()
GUI.title('โปรแกรมคำนวณปลา รถพุ่มพวงของลุง')
GUI.geometry('700x600')
GUI.iconbitmap('Apathae-Poisson-2-Fish.ico')

bg = PhotoImage(file='ice-cream-icon.png')
BG = Label(GUI,image=bg)
BG.pack()



L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=('Angsana New',20))
L.pack()

v_quantity = StringVar() #ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable=v_quantity, font=('Angsana New',20))
E1.pack()


Pr = Label(GUI,text='กรุณากรอกจำนวนบาทต่อกิโลกรัม',font=('Angsana New',20))
Pr.pack()

v_price = StringVar() #ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI,textvariable=v_price, font=('Angsana New',20))
E2.pack()


def Cal():
    try:
        quan = float(v_quantity.get())
        price = float(v_price.get())
        calc = quan * price
        messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
        v_quantity.set('')
        v_price.set('')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('')
        v_price.set('')
        E1.focus()




B2 = ttk.Button(GUI, text='คำนวณ',command=Cal)
B2.pack(ipadx=30,ipady=20,pady=20)



GUI.mainloop()