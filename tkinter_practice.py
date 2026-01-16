import tkinter as tk

root = tk.Tk()
root.title("Tkinter Practice")

def on_click():
    print("Test butto")
    

label = tk.Label(root, text="label 1")
label.grid()

btn = tk.Button(root, text="Our Button", command=on_click)
btn.grid()

root.mainloop()

#Button code

import tkinter as tk

root = tk.Tk()
root.title("Click this red button")

def on_click():
    print("Morena - The Country")

label = tk.Label(root, text="Morena:")
label.grid()

btn = tk.Button(root, text="Morena", bg= "red", command=on_click)
btn.grid()

root.mainloop()



