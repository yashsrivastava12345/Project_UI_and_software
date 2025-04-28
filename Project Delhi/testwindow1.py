import tkinter as tk

root = tk.Tk()

# Remove title bar and window buttons
root.overrideredirect(True)

# Optional: Set a fixed size and black background
root.geometry("800x600")
root.configure(bg="gray")

# Example widget
label = tk.Label(root, text="Custom Window", fg="white", bg="gray", font=("Arial", 24))
label.pack(expand=True)

root.mainloop()
