import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from PIL import ImageEnhance
import win32api
import win32con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import cv2
import numpy as np
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"
image_path = "inverted_image.jpg"
img = Image.open(image_path)
sharpness = ImageEnhance.Sharpness(img)
img = sharpness.enhance(2.0)
img = img.resize((1535, 865), Image.Resampling.LANCZOS)
RADIUS = 15
class ElectrotherapyGUI:
    def __init__(self, root):
        self.is_running = False
        self.root = root
        root.overrideredirect(True)
        root.configure(bg="black")
        root.geometry(resolution)
        root.state('zoomed')
        root.title("Body Region Selector")
        self.data = [0] * 10
        self.init_main_screen()
    def infor(self):
        messagebox.showinfo("Therapy is effective for","\N{BULLET} Cervical Spine\n \N{BULLET} Shoulder \n \N{BULLET} Elbow \n \N{BULLET} Wrist \n \N{BULLET} Low Back – Lumbar Spine \n \N{BULLET} Hamstring – Muscular  \n \N{BULLET} Ankle \n \N{BULLET} TMJ \n \N{BULLET} Hip \n \N{BULLET} Knee \n \N{BULLET} Foot \n \N{BULLET} Aesthetic")
    def init_main_screen(self):
        root.grid_rowconfigure(0, weight=0, minsize=screen_height / 5.4)
        root.grid_rowconfigure(1, weight=0, minsize=screen_height / 5.4)
        root.grid_rowconfigure(2, weight=0, minsize=screen_height / 5.4)
        root.grid_rowconfigure(3, weight=0, minsize=screen_height / 3.3)
        root.grid_rowconfigure(4, weight=0, minsize=100)
        root.grid_columnconfigure(0, weight=0, minsize=screen_width / 4)
        root.grid_columnconfigure(1, weight=0, minsize=screen_width / 4.4)
        root.grid_columnconfigure(2, weight=0, minsize=screen_width / 7.4)
        root.grid_columnconfigure(3, weight=0, minsize=screen_width / 7.4)
        root.grid_columnconfigure(4, weight=0, minsize=screen_width / 8)
        root.grid_columnconfigure(5, weight=0, minsize=screen_width / 8)
        photo = ImageTk.PhotoImage(img)
        canvas_frame = tk.Frame(self.root, width=img.width, height=img.height)
        canvas_frame.grid(row=0, column=0, rowspan=5,columnspan=6, sticky="nsew", padx=5, pady=5)
        canvas = tk.Canvas(canvas_frame,bg="black", width=img.width, height=img.height,highlightthickness=0)
        canvas.pack()
        canvas.create_image(20, 20, anchor=tk.NW, image=photo)
        self.canvas_image = photo
        canvas.create_text(img.width // 3.8, 40, text="Endogenous Thermo Therapy".upper(), fill="silver", font=("", 34))
        canvas.create_text(img.width // 3.8, 750, text="TECAR Ultra".upper(), fill="silver", font=("", 34))
        icon = Image.open("C:/Users/yashs/OneDrive/Desktop/Project Delhi/Icons - Copy/Picture1.png").resize((80, 80))
        btn_img = ImageTk.PhotoImage(icon)
        icon2 = Image.open("C:/Users/yashs/OneDrive/Desktop/Project Delhi/Icons - Copy/History.png").resize((80, 80))
        btn_img2 = ImageTk.PhotoImage(icon2)
        icon3 = Image.open("C:/Users/yashs/OneDrive/Desktop/Project Delhi/Icons - Copy/Info.png").resize((20, 20))
        btn_img3 = ImageTk.PhotoImage(icon3)
        btn1 = tk.Button(
                            root,
                            image=btn_img,
                            text="Settings",
                            compound="top",
                            font=("Arial", 12,"bold"),
                            bg="black",
                            fg="white",
                            border=0
                        )
        btn2 = tk.Button(
                            root,
                            image=btn_img2,
                            text="History",
                            compound="top",      
                            font=("Arial", 12,"bold"),
                            bg="black",
                            fg="white",
                            border=0
                        )
        btn3 = tk.Button(
                            root,
                            image=btn_img3,
                            text="Info",
                            compound="top",      
                            font=("Arial", 12,"bold"),
                            bg="black",
                            fg="white",
                            border=0,command=self.infor
                        )
        btn1.place(x=1205, y=680)
        btn2.place(x=1350, y=680)
        btn3.place(x=1500, y=700)
        btn1.image = btn_img
        btn2.image = btn_img2
        btn3.image = btn_img3
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ElectrotherapyGUI(root)
    root.mainloop()
