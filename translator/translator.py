from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator


root=Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(bg="#cccccc")

def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1.capitalize())
    label2.configure(text=c2.capitalize())
    root.after(1000,label_change)

def translate_now():
    
    try: 
        text_=text1.get(1.0,END)
        t1=Translator()
        trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
        trans_text=trans_text.text

        text2.delete(1.0,END)
        text2.insert(END,trans_text)

    except Exception as e:
        messagebox.showerror("googletranslator","please try again")

#icon
image_icon=PhotoImage(file="google.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_image,width=150,bg="#cccccc")
image_label.place(x=460,y=150)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=100,y=20)
combo1.set("english")

label1=Label(root,text="english",font="segoe 30 bold",bg="#2a84eb",fg="black",width=18,bd=0,relief=GROOVE)
label1.place(x=10,y=50)

##############

combo2=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("select language")

label2=Label(root,text="english",font="segoe 30 bold",bg="#2a84eb",fg="black",width=18,bd=0,relief=GROOVE)
label2.place(x=620,y=50)

##############

f1=Frame(root,bg="#2a84eb",bd=4)
f1.place(x=10,y=110,width=440,height=210)

text1=Text(f1,font="Robote 20",bg="#cccccc",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f1)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

###############

f2=Frame(root,bg="#2a84eb",bd=4)
f2.place(x=620,y=110,width=440,height=210)

text2=Text(f2,font="Robote 20",bg="#cccccc",fg="black",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate1=Button(root,text="Translate",font=("Roboto",15),activebackground="#78b0f0",cursor="hand2",bd=0,width=10, height=2,bg="#2a84eb",fg="black",command=translate_now)
translate1.place(x=476,y=320)

label_change()

root.mainloop()
