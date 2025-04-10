import tkinter as tk
import win32api
import win32con

screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"

root = tk.Tk()
root.geometry(resolution)
root.state('zoomed')

# Grid Configuration
root.grid_rowconfigure(0, weight=0,minsize=screen_height/1.5)
root.grid_rowconfigure(1, weight=0,minsize=screen_height/4)
root.grid_rowconfigure(2, weight=0,minsize=50)
root.grid_columnconfigure(0, weight=0,minsize=screen_width/5)
root.grid_columnconfigure(1, weight=0,minsize=screen_width/1.7)
root.grid_columnconfigure(2, weight=0,minsize=screen_width/5) 


# Widgets
tk.Label(root, text="Top Left", bg="lightblue").grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Top Center", bg="lightgreen").grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom Left", bg="orange").grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom bottom", bg="pink").grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Top Right", bg="green").grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom Right", bg="cyan").grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="All copyrights reserved 2025 \u00A9", bg="blue").grid(row=2, column=0,columnspan=3, sticky="nsew", padx=5, pady=5)

root.mainloop()
