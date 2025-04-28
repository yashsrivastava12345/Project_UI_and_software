import tkinter as tk
import win32api
import win32con

screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"

root = tk.Tk()
root.geometry(resolution)
root.state('zoomed')

# Adjust grid configuration to add more columns and rows
root.grid_rowconfigure(0, weight=0, minsize=screen_height / 4.2)  # Half of original row 0
root.grid_rowconfigure(1, weight=0, minsize=screen_height / 2.3)  # Other half of original row 0
root.grid_rowconfigure(2, weight=0, minsize=screen_height / 4.2)  # Original row 1
root.grid_rowconfigure(3, weight=0, minsize=50)                   # Original row 2

# Columns split: old col 2 → new cols 2 and 3, old col 3 → new cols 4 and 5
root.grid_columnconfigure(0, weight=0, minsize=screen_width / 4)
root.grid_columnconfigure(1, weight=0, minsize=screen_width / 4.4)
root.grid_columnconfigure(2, weight=0, minsize=screen_width / 7.4)
root.grid_columnconfigure(3, weight=0, minsize=screen_width / 7.4)
root.grid_columnconfigure(4, weight=0, minsize=screen_width / 8)
root.grid_columnconfigure(5, weight=0, minsize=screen_width / 8)

# Sample labels to show layout
tk.Label(root, text="<Image>", bg="lightblue").grid(row=0, column=0, rowspan=3,columnspan=5,sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=0, column=1, rowspan=2,columnspan=2, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=0, column=4, rowspan=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="<List of therapy and button>", bg="lightblue").grid(row=0, column=5, rowspan=2,sticky="nsew", padx=5, pady=5)

#tk.Label(root, text="Top Left", bg="lightblue").grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="<Empty section>", bg="lightblue").grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

#tk.Label(root, text="Top Left", bg="lightblue").grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=2, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)
#tk.Label(root, text="Top Left", bg="lightblue").grid(row=2, column=4, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="<Home page button>", bg="lightblue").grid(row=2, column=5, sticky="nsew", padx=5, pady=5)

tk.Label(root, text="<Copyright>", bg="lightblue").grid(row=3, column=0, columnspan=6, sticky="nsew", padx=5, pady=5)



"""tk.Label(root, text="Top Right", bg="gold").grid(row=0, column=5, rowspan=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Top Center Left", bg="red").grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Top Center Right", bg="green").grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Mid Center Left", bg="pink").grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Mid Center Right", bg="purple").grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom Left", bg="orange").grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(root, bg="cyan").grid(row=2, column=5, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="All copyrights reserved 2025 \u00A9", bg="blue").grid(row=3, column=0, columnspan=6, sticky="nsew", padx=5, pady=5)"""

root.mainloop()
