import tkinter as tk

root = tk.Tk()
root.title("Tkinter Sub Grid Example")

# Main Frame
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Widgets in main grid
tk.Label(main_frame, text="Main Grid - Row 0").grid(row=0, column=0)

# Sub Frame (acts as sub-grid)
sub_frame = tk.Frame(main_frame, borderwidth=2, relief="groove")
sub_frame.grid(row=1, column=0, pady=10)

# Widgets in sub grid
tk.Label(sub_frame, text="Sub Grid - R0C0",bg="red").grid(row=0, column=0)
tk.Label(sub_frame, text="Sub Grid - R0C1",bg="brown").grid(row=0, column=1)
tk.Label(sub_frame, text="Sub Grid - R1C0",bg="blue").grid(row=1, column=0)
tk.Label(sub_frame, text="Sub Grid - R1C1",bg="green").grid(row=1, column=1)

# You can add more widgets to the main frame after the sub-grid
tk.Label(main_frame, text="Main Grid - Row 2").grid(row=2, column=0)

root.mainloop()
