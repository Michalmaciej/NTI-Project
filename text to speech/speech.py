import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("550x600+200+200")
root.resizable(False,False)
root.configure(bg="#305065")

engine=pyttsx3.init()

def speak():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if (text):
            if (speed=='Fast'):
                engine.setProperty('rate',250)
                
            elif (speed=="Normal"):
                engine.setProperty('rate',150)
                
            else:
                engine.setProperty('rate',60)
                
            if (gender == 'Male'):
                print("dziala")
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                engine.say(text)
                engine.runAndWait()
    
    setvoice()

def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (text):
            if (speed=='Fast'):
                engine.setProperty('rate',250)
                
            elif (speed=="Normal"):
                engine.setProperty('rate',150)
                
            else:
                engine.setProperty('rate',60)
                
            if (gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
        
    setvoice()

#icon 
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#top frame
Top_frame=Frame(root,bg = "white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="logo.png")
Label(Top_frame,image=Logo,bg = "white").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg = "white",fg="#305065").place(x=150,y=40)

####################
text_area=Text(root,font="Robote 20",bg = "white",fg="#305065",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=510,height=260)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=130,y=440)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=310,y=440)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",foreground = "#305065",state='r',width=10)
gender_combobox.place(x=100,y=500)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",foreground = "#305065",state='r',width=10)
speed_combobox.place(x=280,y=500)
speed_combobox.set('Normal')

#buttons
image_icon1=PhotoImage(file="speaking.png")
btn1=Button(root,text="Speak",compound=LEFT, image=image_icon1, width=130,font="arial 14 bold",command=speak)
btn1.place(x=100,y=540)

image_icon2=PhotoImage(file="download.png")
btn2=Button(root,text="save",compound=LEFT, image=image_icon2, width=130,font="arial 14 bold",command=download)
btn2.place(x=280,y=540)

root.mainloop()
