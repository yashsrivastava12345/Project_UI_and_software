import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32api
import win32con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import serial
import time
import random


# Define body part points with labels (x, y, label)
points = [
    (180, 70, "Head"),
    (225, 155, "Left Shoulder"),
    (95, 245, "Right Elbow"),
    (195, 290, "Abdomen"),
    (80, 335, "Right Hand"),
    (140, 445, "Right Knee"),
    (175, 575, "Left Foot"),
    (417, 90, "Neck (Back)"),
    (413, 180, "Back"),
    (420, 265, "Lower Back")
]

RADIUS = 15

# Function to handle click event
def on_click(event):
    for x, y, label in points:
        if (event.x - x) ** 2 + (event.y - y) ** 2 <= RADIUS ** 2:
            messagebox.showinfo("Body Part", f"You clicked on: {label}")
            break

# Screen resolution
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# Main Window
root = tk.Tk()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')
root.title("Body Region Selector")

# Grid Configuration
root.grid_rowconfigure(0, weight=0, minsize=screen_height/3)
root.grid_rowconfigure(1, weight=0, minsize=screen_height/5.5)
root.grid_rowconfigure(2, weight=0, minsize=50)
root.grid_columnconfigure(0, weight=0, minsize=screen_width/5)
root.grid_columnconfigure(1, weight=0, minsize=screen_width/4.8)
root.grid_columnconfigure(2, weight=0, minsize=screen_width/4.8)
root.grid_columnconfigure(3, weight=0, minsize=screen_width/5)

# Left and right placeholder labels
tk.Label(root, text="Top Left", bg="lightblue").grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Top Right", bg="green").grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom Left", bg="orange").grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom Right", bg="cyan").grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="top center", bg="red").grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="Bottom center", bg="pink").grid(row=1, column=1,columnspan=2, sticky="nsew", padx=5, pady=5)
tk.Label(root, text="All copyrights reserved 2025 \u00A9", bg="blue").grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Image and Canvas in Center Cell
image_path = "WhatsApp Image 2025-04-07 at 12.36.31.jpeg"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

canvas_frame = tk.Frame(root)
canvas_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

canvas = tk.Canvas(canvas_frame, width=img.width, height=img.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Draw points
for x, y, _ in points:
    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, outline="Blue", width=2)

canvas.bind("<Button-1>", on_click)

root.mainloop()
