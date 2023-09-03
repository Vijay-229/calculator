from tkinter import *
import re

wd=Tk()
wd.title("calci")
wd.geometry("405x435")
wd.config(bg="grey5")


label=Label(wd,fg="magenta",bg="black",height=1,width=20,anchor=E,text='',font=('bold',26))
label.grid(row=0,column=0,columnspan=4)

def look(n):
    s = label.cget("text")
    if(s=='' or s[0] in "0123456789"):
        if n == 'c':
            label.config(text='')
        elif n == 'd':
            label.config(text=s[:-1])
        else:
            label.config(text=s + n)
    else:
        if n in '0123456789':
            label.config(text=n)
        else:
            label.config(text='')

def calc():
    ex=label.cget("text")
    if ex=='':
        label.config(text='')
    num = re.split("[+ / %  ^ x -]",ex)
    sym = re.split("[0-9]", ex)
    if '' in num:
        label.config(text='Invalid Syntax',font=('Arial',20),width=25)
    else:
        for i in range(sym.count('')):
            sym.remove('')
        for i in range(sym.count('.')):
            sym.remove('.')
        try:
            p = float(num[0])
            for i in range(len(sym)):
                s1 = sym[i]
                if (s1 == '+'):
                    p = p + float(num[i + 1])
                elif (s1 == '-'):
                    p = p - float(num[i + 1])
                elif (s1 == 'x'):
                    p = p * float(num[i + 1])
                elif (s1 == '/'):
                    p = p / float(num[i + 1])
                elif (s1 == '^'):
                    p = p ** float(num[i + 1])
                elif (s1 == '%'):
                    p = p % float(num[i + 1])
            st=str(p)
            if len(st[st.index('.')::])==2 and st[st.index('.')+1]=='0':
                label.config(text=str(int(p)))
            else:
                label.config(text=str(p))
        except:
            label.config(text='Math Error',font=('Arial',20),width=25)



button_ac=Button(wd,text='AC',width=6,pady=15,fg="DeepPink",bg="grey5",bd=0,font=("bold",20),activeforeground="DeepPink",activebackground="grey10", command=lambda : look('c'))
button_per=Button(wd,text='%',width=5,pady=10,fg="magenta",bg="grey5",bd=0,font=("bold",25),activeforeground="purple",activebackground="grey10", command=lambda : look('%'))
button_del=Button(wd,text='Del',width=6,pady=15,fg="DeepPink",bg="grey5",bd=0,font=("bold",20),activeforeground="DeepPink",activebackground="grey10", command=lambda : look('d'))
button_div=Button(wd,text='/',width=4,pady=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10", command=lambda : look('/'))

button_7=Button(wd, text='7', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('7'))
button_8=Button(wd, text='8', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('8'))
button_9=Button(wd, text='9', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('9'))
button_x=Button(wd,text='x',width=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10", command=lambda : look('x'))

button_4=Button(wd, text='4', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('4'))
button_5=Button(wd, text='5', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('5'))
button_6=Button(wd, text='6', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('6'))
button_min=Button(wd,text='-',width=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10",command=lambda : look('-'))

button_1=Button(wd, text='1', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('1'))
button_2=Button(wd, text='2', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('2'))
button_3=Button(wd, text='3', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('3'))
button_plus=Button(wd,text='+',width=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10", command=lambda : look('+'))

button_cap=Button(wd,text='^',width=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10", command=lambda : look('^'))
button_0=Button(wd, text='0', width=4, fg="magenta", bg="grey5", bd=0, font=("bold",30), activeforeground="purple", activebackground="grey10", command=lambda : look('0'))
button_dot=Button(wd,text='.',width=4,fg="magenta",bg="grey5",bd=0,font=("bold",30),activeforeground="purple",activebackground="grey10",command=lambda : look('.'))
button_eq=Button(wd,text='=',width=4,fg="DeepPink",bg="grey5",bd=0,font=("bold",30),activeforeground="DeepPink",activebackground="grey10",command=calc)

button_ac.place(x=0,y=46)
button_per.place(x=102,y=46)
button_del.place(x=204,y=46)
button_div.place(x=306,y=46)
button_7.place(x=0,y=127)
button_8.place(x=102,y=127)
button_9.place(x=204,y=127)
button_x.place(x=306,y=127)
button_4.place(x=0,y=203)
button_5.place(x=102,y=203)
button_6.place(x=204,y=203)
button_min.place(x=306,y=203)
button_1.place(x=0,y=279)
button_2.place(x=102,y=279)
button_3.place(x=204,y=279)
button_plus.place(x=306,y=279)
button_cap.place(x=0,y=355)
button_0.place(x=102,y=355)
button_dot.place(x=204,y=355)
button_eq.place(x=306,y=355)


wd.mainloop()
