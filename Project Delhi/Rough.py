import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32api
import win32con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"

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

class ElectrotherapyGUI:
    def __init__(self, root):
        self.root = root
        root.geometry(resolution)
        root.state('zoomed')
        root.title("Body Region Selector")
        self.data = [0] * 50
        self.init_main_screen()
        
    def on_click(self, event):
        for x, y, label in points:
            if (event.x - x) ** 2 + (event.y - y) ** 2 <= RADIUS ** 2:
                messagebox.showinfo("Body Part", f"You clicked on: {label}")
                break

    def update_graph(self):
        value = random.randint(0, 1024)
        self.data.append(value)
        self.data.pop(0)
        self.line.set_ydata(self.data)
        self.line.set_xdata(range(len(self.data)))
        self.ax.relim()
        self.ax.autoscale_view()
        self.graph_canvas.draw()
        self.root.after(200, self.update_graph)
    
    def init_main_screen(self):
        # Static layout
        self.root.grid_rowconfigure(0, weight=0, minsize=screen_height / 1.6)
        self.root.grid_rowconfigure(1, weight=0, minsize=screen_height / 2.3)
        self.root.grid_rowconfigure(2, weight=0, minsize=50)
        self.root.grid_columnconfigure(0, weight=0, minsize=screen_width / 4)
        self.root.grid_columnconfigure(1, weight=0, minsize=screen_width / 2.8)
        self.root.grid_columnconfigure(2, weight=0, minsize=screen_width / 2.8)
        self.root.grid_columnconfigure(3, weight=0, minsize=screen_width / 4)

        tk.Label(self.root, text="Top Left", bg="lightblue").grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        tk.Label(self.root, text="Top Right", bg="green").grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        tk.Label(self.root, text="Bottom Left", bg="orange").grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        tk.Label(self.root, text="Bottom Right", bg="cyan").grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
        tk.Label(self.root, text="top center", bg="red").grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        tk.Label(self.root, text="All copyrights reserved 2025 \u00A9", bg="blue").grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Center image
        image_path = "WhatsApp Image 2025-04-07 at 12.36.31.jpeg"
        img = Image.open(image_path)
        #img = img.resize((int(screen_width / 4.8), int(screen_height / 3)), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        canvas_frame = tk.Frame(self.root, width=img.width, height=img.height)
        canvas_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        canvas = tk.Canvas(canvas_frame, width=img.width, height=img.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        for x, y, _ in points:
            canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, outline="Blue", width=2)

        canvas.bind("<Button-1>", self.on_click)
        self.canvas_image = photo  # keep image reference

        # Graph
        self.figure, self.ax = plt.subplots(figsize=(5, 2), dpi=100)
        self.line, = self.ax.plot(self.data)
        self.ax.set_title("Arduino Frequency Input")
        self.ax.set_ylim(0, 1024)

        self.graph_canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.graph_canvas.get_tk_widget().grid(row=1, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

        self.update_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectrotherapyGUI(root)
    root.mainloop()
