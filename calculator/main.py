import tkinter
from tkinter import *
from PIL import ImageTk, Image

equation = ""

def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

def show(value):
    global equation
    equation += value
    label_result.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = str(result)
        except:
            result = "error"
            equation = ""
    label_result.config(text = result)

root = Tk()
root.title("Calculator")
root.geometry("620x600+100+200")
root.resizable(False, False)
root.configure(bg = "#484649")

photo_0_off = ImageTk.PhotoImage(Image.open("images/0_off.png"))
photo_0_on = ImageTk.PhotoImage(Image.open("images/0_on.png")) 
photo_1_off = ImageTk.PhotoImage(Image.open("images/1_off.png"))
photo_1_on = ImageTk.PhotoImage(Image.open("images/1_on.png"))
photo_2_off = ImageTk.PhotoImage(Image.open("images/2_off.png"))
photo_2_on = ImageTk.PhotoImage(Image.open("images/2_on.png"))
photo_3_off = ImageTk.PhotoImage(Image.open("images/3_off.png"))
photo_3_on = ImageTk.PhotoImage(Image.open("images/3_on.png"))
photo_4_off = ImageTk.PhotoImage(Image.open("images/4_off.png"))
photo_4_on = ImageTk.PhotoImage(Image.open("images/4_on.png"))
photo_5_off = ImageTk.PhotoImage(Image.open("images/5_off.png"))
photo_5_on = ImageTk.PhotoImage(Image.open("images/5_on.png"))
photo_6_off = ImageTk.PhotoImage(Image.open("images/6_off.png"))
photo_6_on = ImageTk.PhotoImage(Image.open("images/6_on.png"))
photo_7_off = ImageTk.PhotoImage(Image.open("images/7_off.png"))
photo_7_on = ImageTk.PhotoImage(Image.open("images/7_on.png"))
photo_8_off = ImageTk.PhotoImage(Image.open("images/8_off.png"))
photo_8_on = ImageTk.PhotoImage(Image.open("images/8_on.png"))
photo_9_off = ImageTk.PhotoImage(Image.open("images/9_off.png"))
photo_9_on = ImageTk.PhotoImage(Image.open("images/9_on.png"))
photo_open_off = ImageTk.PhotoImage(Image.open("images/(_off.png"))
photo_open_on = ImageTk.PhotoImage(Image.open("images/(_on.png"))
photo_close_off = ImageTk.PhotoImage(Image.open("images/)_off.png"))
photo_close_on = ImageTk.PhotoImage(Image.open("images/)_on.png"))
photo_dot_off = ImageTk.PhotoImage(Image.open("images/dot_off.png"))
photo_dot_on = ImageTk.PhotoImage(Image.open("images/dot_on.png"))
photo_slash_off = ImageTk.PhotoImage(Image.open("images/slash_off.png"))
photo_slash_on = ImageTk.PhotoImage(Image.open("images/slash_on.png"))
photo_minus_off = ImageTk.PhotoImage(Image.open("images/minus_off.png"))
photo_minus_on = ImageTk.PhotoImage(Image.open("images/minus_on.png"))
photo_plus_off = ImageTk.PhotoImage(Image.open("images/plus_off.png"))
photo_plus_on = ImageTk.PhotoImage(Image.open("images/plus_on.png"))
photo_proc_off = ImageTk.PhotoImage(Image.open("images/proc_off.png"))
photo_proc_on = ImageTk.PhotoImage(Image.open("images/proc_on.png"))
photo_st_off = ImageTk.PhotoImage(Image.open("images/st_off.png"))
photo_st_on = ImageTk.PhotoImage(Image.open("images/st_on.png"))
photo_C_off = ImageTk.PhotoImage(Image.open("images/c_off.png"))
photo_C_on = ImageTk.PhotoImage(Image.open("images/c_on.png"))
photo_eq_off = ImageTk.PhotoImage(Image.open("images/eq_off.png"))
photo_eq_on = ImageTk.PhotoImage(Image.open("images/eq_on.png"))

def on_0(e):
    button_0['image'] = photo_0_on
    
def off_0(e):
    button_0['image'] = photo_0_off
    
def on_1(e):
    button_1['image'] = photo_1_on
    
def off_1(e):
    button_1['image'] = photo_1_off
    
def on_2(e):
    button_2['image'] = photo_2_on
    
def off_2(e):
    button_2['image'] = photo_2_off
    
def on_3(e):
    button_3['image'] = photo_3_on
    
def off_3(e):
    button_3['image'] = photo_3_off
    
def on_4(e):
    button_4['image'] = photo_4_on
    
def off_4(e):
    button_4['image'] = photo_4_off
    
def on_5(e):
    button_5['image'] = photo_5_on
    
def off_5(e):
    button_5['image'] = photo_5_off

def on_6(e):
    button_6['image'] = photo_6_on
    
def off_6(e):
    button_6['image'] = photo_6_off

def on_7(e):
    button_7['image'] = photo_7_on
    
def off_7(e):
    button_7['image'] = photo_7_off

def on_8(e):
    button_8['image'] = photo_8_on
    
def off_8(e):
    button_8['image'] = photo_8_off
    
def on_9(e):
    button_9['image'] = photo_9_on

def off_9(e):
    button_9['image'] = photo_9_off

def on_open(e):
    button_open['image'] = photo_open_on

def off_open(e):
    button_open['image'] = photo_open_off

def on_close(e):
    button_close['image'] = photo_close_on

def off_close(e):
    button_close['image'] = photo_close_off

def on_c(e):
    button_c['image'] = photo_C_on

def off_c(e):
    button_c['image'] = photo_C_off

def on_eq(e):
    button_eq['image'] = photo_eq_on

def off_eq(e):
    button_eq['image'] = photo_eq_off

def on_dot(e):
    button_dot['image'] = photo_dot_on

def off_dot(e):
    button_dot['image'] = photo_dot_off

def on_st(e):
    button_st['image'] = photo_st_on

def off_st(e):
    button_st['image'] = photo_st_off

def on_slash(e):
    button_slash['image'] = photo_slash_on

def off_slash(e):
    button_slash['image'] = photo_slash_off

def on_proc(e):
    button_proc['image'] = photo_proc_on

def off_proc(e):
    button_proc['image'] = photo_proc_off

def on_minus(e):
    button_minus['image'] = photo_minus_on

def off_minus(e):
    button_minus['image'] = photo_minus_off

def on_plus(e):
    button_plus['image'] = photo_plus_on

def off_plus(e):
    button_plus['image'] = photo_plus_off

label_result = Label(root, width = 27, height = 2, text = "", font = ("Arial", 30), fg = "#484649", bg = "#727272")
label_result.pack()

button_c = Button(root, image = photo_C_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: clear(), relief = SUNKEN)
button_c.bind("<Enter>", on_c)
button_c.bind("<Leave>", off_c)
button_c.place(x = 10, y = 100)

button_slash = Button(root, image = photo_slash_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("/"), relief = SUNKEN)
button_slash.bind("<Enter>", on_slash)
button_slash.bind("<Leave>", off_slash)
button_slash.place(x = 160, y = 100)

button_proc = Button(root, image = photo_proc_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("%"), relief = SUNKEN)
button_proc.bind("<Enter>", on_proc)
button_proc.bind("<Leave>", off_proc)
button_proc.place(x = 310, y = 100)

button_st = Button(root, image = photo_st_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("*"), relief = SUNKEN)
button_st.bind("<Enter>", on_st)
button_st.bind("<Leave>", off_st)
button_st.place(x = 460, y = 100)

button_7 = Button(root, image = photo_7_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("7"), relief = SUNKEN)
button_7.bind("<Enter>", on_7)
button_7.bind("<Leave>", off_7)
button_7.place(x = 10, y = 200)

button_8 = Button(root, image = photo_8_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("8"), relief = SUNKEN)
button_8.bind("<Enter>", on_8)
button_8.bind("<Leave>", off_8)
button_8.place(x = 160, y = 200)

button_9 = Button(root, image = photo_9_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("9"), relief = SUNKEN)
button_9.bind("<Enter>", on_9)
button_9.bind("<Leave>", off_9)
button_9.place(x = 310, y = 200)

button_minus = Button(root, image = photo_minus_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("-"), relief = SUNKEN)
button_minus.bind("<Enter>", on_minus)
button_minus.bind("<Leave>", off_minus)
button_minus.place(x = 460, y = 200)

button_4 = Button(root, image = photo_4_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("4"), relief = SUNKEN)
button_4.bind("<Enter>", on_4)
button_4.bind("<Leave>", off_4)
button_4.place(x = 10, y = 300)

button_5 = Button(root, image = photo_5_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("5"), relief = SUNKEN)
button_5.bind("<Enter>", on_5)
button_5.bind("<Leave>", off_5)
button_5.place(x = 160, y = 300)

button_6 = Button(root, image = photo_6_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("6"), relief = SUNKEN)
button_6.bind("<Enter>", on_6)
button_6.bind("<Leave>", off_6)
button_6.place(x = 310, y = 300)

button_plus = Button(root, image = photo_plus_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("+"), relief = SUNKEN)
button_plus.bind("<Enter>", on_plus)
button_plus.bind("<Leave>", off_plus)
button_plus.place(x = 460, y = 300)

button_1 = Button(root, image = photo_1_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("1"), relief = SUNKEN)
button_1.bind("<Enter>", on_1)
button_1.bind("<Leave>", off_1)
button_1.place(x = 10, y = 400)

button_2 = Button(root, image = photo_2_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("2"), relief = SUNKEN)
button_2.bind("<Enter>", on_2)
button_2.bind("<Leave>", off_2)
button_2.place(x = 160, y = 400)

button_3 = Button(root, image = photo_3_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("3"), relief = SUNKEN)
button_3.bind("<Enter>", on_3)
button_3.bind("<Leave>", off_3)
button_3.place(x = 310, y = 400)

button_dot = Button(root, image = photo_dot_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("."), relief = SUNKEN)
button_dot.bind("<Enter>", on_dot)
button_dot.bind("<Leave>", off_dot)
button_dot.place(x = 460, y = 400)

button_0 = Button(root, image = photo_0_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("0"), relief = SUNKEN)
button_0.bind("<Enter>", on_0)
button_0.bind("<Leave>", off_0)
button_0.place(x = 10, y = 500)

button_open = Button(root, image = photo_open_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show("("), relief = SUNKEN)
button_open.bind("<Enter>", on_open)
button_open.bind("<Leave>", off_open)
button_open.place(x = 160, y = 500)

button_close = Button(root, image = photo_close_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: show(")"), relief = SUNKEN)
button_close.bind("<Enter>", on_close)
button_close.bind("<Leave>", off_close)
button_close.place(x = 310, y = 500)

button_eq = Button(root, image = photo_eq_off, border = 0, cursor = 'hand2', bg = "#484649", command = lambda: calculate(), relief = SUNKEN)
button_eq.bind("<Enter>", on_eq)
button_eq.bind("<Leave>", off_eq)
button_eq.place(x = 460, y = 500)

root.mainloop()

