import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Menu")
root.geometry("1000x600+100+200")
root.resizable(False, False)
root.configure(bg = "#484649")

photo_calc_off = ImageTk.PhotoImage(Image.open("images/Group 1.png"))
photo_calc_on = ImageTk.PhotoImage(Image.open("images/Group 3.png")) 
photo_trans_off = ImageTk.PhotoImage(Image.open("images/Group 2.png"))
photo_trans_on = ImageTk.PhotoImage(Image.open("images/Group 4.png"))
photo_pyth_off = ImageTk.PhotoImage(Image.open("images/Group 6.png"))
photo_pyth_on = ImageTk.PhotoImage(Image.open("images/Group 7.png"))
photo_int_off = ImageTk.PhotoImage(Image.open("images/Group 10.png"))
photo_int_on = ImageTk.PhotoImage(Image.open("images/Group 11.png"))
photo_tex_off = ImageTk.PhotoImage(Image.open("images/Group 9.png"))
photo_tex_on = ImageTk.PhotoImage(Image.open("images/Group 12.png"))
photo_weat_off = ImageTk.PhotoImage(Image.open("images/Group 5.png"))
photo_weat_on = ImageTk.PhotoImage(Image.open("images/Group 8.png"))

def on_calc(e):
    button_calc['image'] = photo_calc_on
    
def off_calc(e):
    button_calc['image'] = photo_calc_off
    
def on_trans(e):
    button_trans['image'] = photo_trans_on
    
def off_trans(e):
    button_trans['image'] = photo_trans_off
    
def on_pyth(e):
    button_pyth['image'] = photo_pyth_on
    
def off_pyth(e):
    button_pyth['image'] = photo_pyth_off
    
def on_int(e):
    button_int['image'] = photo_int_on
    
def off_int(e):
    button_int['image'] = photo_int_off
    
def on_tex(e):
    button_tex['image'] = photo_tex_on
    
def off_tex(e):
    button_tex['image'] = photo_tex_off
    
def on_weat(e):
    button_weat['image'] = photo_weat_on
    
def off_weat(e):
    button_weat['image'] = photo_weat_off

def calculator():
    pass

button_calc = Button(root, image = photo_calc_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_calc.bind("<Enter>", on_calc)
button_calc.bind("<Leave>", off_calc)
button_calc.place(x = 60, y = 80)

button_trans = Button(root, image = photo_trans_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_trans.bind("<Enter>", on_trans)
button_trans.bind("<Leave>", off_trans)
button_trans.place(x = 520, y = 80)

button_pyth = Button(root, image = photo_pyth_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_pyth.bind("<Enter>", on_pyth)
button_pyth.bind("<Leave>", off_pyth)
button_pyth.place(x = 60, y = 240)

button_int = Button(root, image = photo_int_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_int.bind("<Enter>", on_int)
button_int.bind("<Leave>", off_int)
button_int.place(x = 520, y = 240)

button_tex = Button(root, image = photo_tex_off, border = 0, activebackground="#484649", cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_tex.bind("<Enter>", on_tex)
button_tex.bind("<Leave>", off_tex)
button_tex.place(x = 60, y = 400)

button_weat= Button(root, image = photo_weat_off, border = 0, activebackground="#484649",cursor = 'hand2', bg = "#484649", command = lambda: calculator(), relief = SUNKEN)
button_weat.bind("<Enter>", on_weat)
button_weat.bind("<Leave>", off_weat)
button_weat.place(x = 520, y = 400)



root.mainloop()
