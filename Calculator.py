import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

root = tk.Tk()
ttk.Style().theme_use('clam')

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir,'delete.png')

img = Image.open(icon_path)
img = img.resize((20,20),Image.Resampling.LANCZOS)
delete_icon = ImageTk.PhotoImage(img)

font_size = 14
font_type = "Courier New Bold"
button_bg = "#2C2C2C"
text_color = "#ffffff"

style = ttk.Style()
style.configure("TButton",background=button_bg,foreground=text_color,font=(font_type,font_size),padding=(2,1),relief="flat")
style.map("TButton",background = [("active","#444444")])

style.configure("TEntry",foreground = text_color,fieldbackground='#202020',background='#202020',borderwidth=0,relief='flat',padding=10,font=(font_type,15))

entry = ttk.Entry(root,style = 'TEntry',font=(font_type,20))
entry.grid(row=0,column=0,columnspan=7,padx=5,pady=5, sticky='nsew')

lastnumber = ""
lastfunction = ""

def on_click(char):
    current = entry.get()
    if char in "+-x\u00f7/" and current[-1:] in "+-x\u00f7/":
        return
    entry.delete(0, tk.END)
    entry.insert(0, current + char)


def calculate(event=None):
    global lastnumber, lastfunction
    expression = entry.get()
    expression = expression.replace("x", "*").replace("\u00f7", "/").replace("^","**")
    try:
        if not any(op in expression for op in "+-*/**") and lastfunction and lastnumber:
            expression += lastfunction+lastnumber
        result = eval(expression)
        
        for op in ["+", "-", "*", "/", "**"]:
            if op in expression:
                parts = expression.split(op)
                if len(parts)==2 and parts[1].strip():
                    lastfunction=op
                    lastnumber=parts[1].strip()
                    break
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def valid_input(event):
    allowed_chars = "0123456789+-x\u00f7/().^"
    if event.char not in allowed_chars and event.keysym not in ("BackSpace", "Delete", "Left", "Right"):
        return "break"

def on_enter(event):
    event.widget.config(bg="")
    return

xpad = 2
ypad = 2

button1 = ttk.Button(root, text="1", command=lambda: on_click("1"))
button1.grid(row=4, column=0, padx=xpad, pady=ypad)

button2 = ttk.Button(root, text="2", command=lambda: on_click("2"))
button2.grid(row=4, column=1, padx=xpad, pady=ypad)

button3 = ttk.Button(root, text="3", command=lambda: on_click("3"))
button3.grid(row=4, column=2, padx=xpad, pady=ypad)

button4 = ttk.Button(root, text="4", command=lambda: on_click("4"))
button4.grid(row=3, column=0, padx=xpad, pady=ypad)

button5 = ttk.Button(root, text="5", command=lambda: on_click("5"))
button5.grid(row=3, column=1, padx=xpad, pady=ypad)

button6 = ttk.Button(root, text="6", command=lambda: on_click("6"))
button6.grid(row=3, column=2, padx=xpad, pady=ypad)

button7 = ttk.Button(root, text="7", command=lambda: on_click("7"))
button7.grid(row=2, column=0, padx=xpad, pady=ypad)

button8 = ttk.Button(root, text="8", command=lambda: on_click("8"))
button8.grid(row=2, column=1, padx=xpad, pady=ypad)

button9 = ttk.Button(root, text="9", command=lambda: on_click("9"))
button9.grid(row=2, column=2, padx=xpad, pady=ypad)

button0 = ttk.Button(root, text="0", command=lambda: on_click("0"))
button0.grid(row=5, column=1, padx=xpad, pady=ypad)

button_enter = ttk.Button(root, text="Enter", command=calculate)
button_enter.grid(row=6, column=3, padx=xpad, pady=ypad)

button_clear = ttk.Button(root, text="Clear", command=lambda: entry.delete(0, tk.END))
button_clear.grid(row=1, column=2, padx=xpad, pady=ypad)

CE_frame = ttk.Frame(root,width=130,height=30)
CE_frame.grid(row=1,column=3,padx=xpad,pady=ypad)
CE_frame.grid_propagate(False)
button_clear_entry = ttk.Button(CE_frame, image=delete_icon, command=backspace)
button_clear_entry.image=delete_icon
button_clear_entry.place(x=0,y=0,width=130,height=30)

button_add = ttk.Button(root, text="+", command=lambda: on_click("+"))
button_add.grid(row=2, column=3, padx=xpad, pady=ypad)

button_subtract = ttk.Button(root, text="-", command=lambda: on_click("-"))
button_subtract.grid(row=3, column=3, padx=xpad, pady=ypad)

button_multiply = ttk.Button(root, text="x", command=lambda: on_click("x"))
button_multiply.grid(row=4, column=3, padx=xpad, pady=ypad)

button_divide = ttk.Button(root, text="\u00f7", command=lambda: on_click("\u00f7"))
button_divide.grid(row=5, column=3, padx=xpad, pady=ypad)

button_exp = ttk.Button(root,text='exp',command=lambda:on_click('^'))
button_exp.grid(row=6,column=1,padx=xpad,pady=ypad)

par_frame = ttk.Frame(root, width=135,height=30)  # Set height
par_frame.configure(style='Custom.TFrame')
style.configure('Custom.TFrame',background='#202020')
par_frame.grid(row=6, column=0, columnspan=1, padx=xpad, pady=ypad)  # Use appropriate row
par_frame.grid_propagate(False)

par_frame.grid_columnconfigure(0, weight=1)
par_frame.grid_columnconfigure(1, weight=1)

button_lpar = ttk.Button(par_frame, text="(", command=lambda: on_click("("))
button_lpar.grid(row=0, column=0, sticky='nsew', ipadx=xpad, ipady=ypad, padx=(0, 1.5))

button_rpar = ttk.Button(par_frame, text=")", command=lambda: on_click(")"))
button_rpar.grid(row=0, column=1, sticky='nsew', ipadx=xpad, ipady=ypad,padx=(1.5,0))

button_decimal = ttk.Button(root,text=".",command=lambda:on_click("."))
button_decimal.grid(row=5,column=2,padx=xpad, pady=ypad)


root.bind("<Return>", calculate)
entry.bind("<Return>", valid_input)

root.title("Calc (short for calculator I'm just using slang)")
for i in range(5):
    root.columnconfigure(i,weight=1)

for i in range(7):
    root.rowconfigure(i,weight=1)

root.resizable(False,False)
root.config(bg="#202020")
root.mainloop()