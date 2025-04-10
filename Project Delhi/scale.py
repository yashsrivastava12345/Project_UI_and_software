
import tkinter as tk

root = tk.Tk()

scale = tk.Scale(root, from_=0, to=100, length=300, resolution=5, orient=tk.VERTICAL)
scale.pack()

root.mainloop()

"""import tkinter as tk

def on_scale_change(val):
    label.config(text=f"Current Value: {val}")

root = tk.Tk()
root.title("Scale Demo")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_change)
scale.pack(padx=20, pady=20)

label = tk.Label(root, text="Current Value: 0")
label.pack()

root.mainloop()"""
