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
import random  # Replace with actual Arduino values

# Screen resolution setup
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"

# Clickable points
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

def on_click(event):
    for x, y, label in points:
        if (event.x - x) ** 2 + (event.y - y) ** 2 <= RADIUS ** 2:
            messagebox.showinfo("Body Part", f"You clicked on: {label}")
            break

class ElectrotherapyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Electrotherapy System")
        self.root.geometry(resolution)

        self.data = [0] * 50  # hold last 50 frequency values

        # self.ser = serial.Serial('COM3', 9600)  # Uncomment when using real Arduino

        self.init_main_screen()

    def init_main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="LF 00", font=("Arial", 16, "bold"), bg='blue', fg='white').pack(fill=tk.X)

        # Left controls
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(left_frame, text="143 Hz\nCC\n0%", font=("Arial", 12)).pack(pady=5)
        tk.Label(left_frame, text="Parameters", font=("Arial", 10)).pack()

        self.intensity = tk.Scale(left_frame, from_=0, to=100, orient=tk.VERTICAL, label="Intensity")
        self.intensity.pack()

        tk.Button(left_frame, text="Stop", command=self.stop).pack(pady=10)

        # Center frame (replaces static image with clickable one)
        center_frame = tk.Frame(self.root)
        center_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Load clickable image
        self.canvas_image = Image.open("WhatsApp Image 2025-04-07 at 12.36.31.jpeg")
        self.tk_image = ImageTk.PhotoImage(self.canvas_image)
        self.canvas = tk.Canvas(center_frame, width=self.canvas_image.width, height=self.canvas_image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Draw points
        for x, y, _ in points:
            self.canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, outline="Blue", width=2)

        self.canvas.bind("<Button-1>", on_click)

        # Graph section
        self.figure, self.ax = plt.subplots(figsize=(5, 2), dpi=100)
        self.line, = self.ax.plot(self.data)
        self.ax.set_title("Arduino Frequency Input")
        self.ax.set_ylim(0, 1024)
        self.canvas_graph = FigureCanvasTkAgg(self.figure, master=center_frame)
        self.canvas_graph.get_tk_widget().pack()

        self.update_graph()

        # Effects and timer
        self.therapy_time = tk.IntVar(value=5)
        tk.Label(center_frame, text="Effects", font=("Arial", 10, "bold")).pack()
        for effect in ["Analgesia", "Hyperemia", "Relaxation", "Strengthening"]:
            tk.Checkbutton(center_frame, text=effect).pack(anchor=tk.W)
        tk.Label(center_frame, textvariable=self.therapy_time, font=("Arial", 24)).pack(pady=10)
        tk.Button(center_frame, text="-", command=lambda: self.adjust_time(-1)).pack(side=tk.LEFT)
        tk.Button(center_frame, text="+", command=lambda: self.adjust_time(1)).pack(side=tk.LEFT)

        # Right navigation
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        for text in ["Favourites", "Programmes", "Indications", "Memory", "Back"]:
            tk.Button(right_frame, text=text, width=15, command=self.show_indications if text == "Indications" else None).pack(pady=2)

    def update_graph(self):
        # Simulated data — replace with actual read from Arduino
        # value = int(self.ser.readline().decode().strip())
        value = random.randint(0, 1024)

        self.data.append(value)
        self.data.pop(0)

        self.line.set_ydata(self.data)
        self.line.set_xdata(range(len(self.data)))
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas_graph.draw()

        self.root.after(200, self.update_graph)

    def show_indications(self):
        self.clear_screen()

        tk.Label(self.root, text="Indications", font=("Arial", 16, "bold"), bg='blue', fg='white').pack(fill=tk.X)

        left = tk.Frame(self.root)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        indication_text = tk.Text(left, height=20, width=50)
        indication_text.insert(tk.END, "Indication: Chronic Pain\nProgramme: Traebert Current 2/5 ms 143 Hz\n")
        indication_text.insert(tk.END, "Primary Therapy Purpose: Analgesia\n")
        indication_text.insert(tk.END, "Further Therapy Purposes: Muscle relaxation, elasticity improvement\n")
        indication_text.insert(tk.END, "Treatment Recommendation: Clear sensation, 5 min\n")
        indication_text.pack(padx=10, pady=10)

        tk.Button(left, text="Back", command=self.init_main_screen).pack()

        right = tk.Frame(self.root)
        right.pack(side=tk.RIGHT, fill=tk.Y)
        for text in ["Favourites", "Programmes", "Indications", "Memory", "Back"]:
            tk.Button(right, text=text, width=15, command=self.init_main_screen if text == "Back" else None).pack(pady=2)

    def adjust_time(self, delta):
        new_time = self.therapy_time.get() + delta
        if 1 <= new_time <= 60:
            self.therapy_time.set(new_time)

    def stop(self):
        messagebox.showinfo("Stop", "Therapy stopped")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectrotherapyGUI(root)
    root.mainloop()
