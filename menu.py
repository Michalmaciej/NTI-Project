import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Menu")
root.geometry("500x600+100+200")
root.resizable(False, False)
root.configure(bg = "#484649")

photo_calc_off = ImageTk.PhotoImage(Image.open("images/Group 1.png"))
photo_calc_on = ImageTk.PhotoImage(Image.open("images/Group 3.png")) 
photo_tex_off = ImageTk.PhotoImage(Image.open("images/Group 9.png"))
photo_tex_on = ImageTk.PhotoImage(Image.open("images/Group 12.png"))
photo_weat_off = ImageTk.PhotoImage(Image.open("images/Group 5.png"))
photo_weat_on = ImageTk.PhotoImage(Image.open("images/Group 8.png"))

def on_calc(e):
    button_calc['image'] = photo_calc_on
        
def off_calc(e):
    button_calc['image'] = photo_calc_off
        
def on_tex(e):
    button_tex['image'] = photo_tex_on
        
def off_tex(e):
    button_tex['image'] = photo_tex_off
        
def on_weat(e):
    button_weat['image'] = photo_weat_on
        
def off_weat(e):
    button_weat['image'] = photo_weat_off

def calculator():
    root.destroy()
    import calculator      

def speech():
    root.destroy()
    import speech
        
        
def weather():
    root.destroy()
    import weather

button_calc = Button(root, image = photo_calc_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_calc.bind("<Enter>", on_calc)
button_calc.bind("<Leave>", off_calc)
button_calc.place(x = 60, y = 80)

button_tex = Button(root, image = photo_tex_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: speech(), relief = SUNKEN)
button_tex.bind("<Enter>", on_tex)
button_tex.bind("<Leave>", off_tex)
button_tex.place(x = 60, y = 240)

button_weat= Button(root, image = photo_weat_off, border = 0, activebackground="#484649",cursor = 'hand2', bg = "#484649", command = lambda: weather(), relief = SUNKEN)
button_weat.bind("<Enter>", on_weat)
button_weat.bind("<Leave>", off_weat)
button_weat.place(x = 60, y = 400)



root.mainloop()
