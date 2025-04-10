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

class ElectrotherapyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Electrotherapy System")
        self.root.geometry(resolution)

        # Arduino data list
        self.data = [0] * 50  # hold last 50 frequency values

        # Uncomment when using real Arduino
        # self.ser = serial.Serial('COM3', 9600)

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

        # Center image and graph
        center_frame = tk.Frame(self.root)
        center_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Load image
        image = Image.open("BodyPartPointer-1.png")
        image = image.resize((400, 600), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(center_frame, image=self.photo)
        image_label.pack()

        # Graph section
        self.figure, self.ax = plt.subplots(figsize=(5, 2), dpi=100)
        self.line, = self.ax.plot(self.data)
        self.ax.set_title("Arduino Frequency Input")
        self.ax.set_ylim(0, 1024)
        self.canvas = FigureCanvasTkAgg(self.figure, master=center_frame)
        self.canvas.get_tk_widget().pack()

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
        self.canvas.draw()

        self.root.after(200, self.update_graph)  # update every 200 ms

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
