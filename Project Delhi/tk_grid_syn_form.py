import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32api
import win32con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random  # Simulate Arduino data

# Set full screen resolution
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
resolution = f"{screen_width}x{screen_height}"

class ElectrotherapyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Electrotherapy System")
        self.root.geometry(resolution)

        self.data = [0] * 50  # Simulated data list

        self.init_main_screen()

    def init_main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="LF 00", font=("Arial", 16, "bold"), bg='blue', fg='white').grid(row=0, column=0, columnspan=3, sticky="ew")

        # ----- Left Panel -----
        left_frame = tk.Frame(self.root)
        left_frame.grid(row=1, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        tk.Label(left_frame, text="143 Hz\nCC\n0%", font=("Arial", 12)).pack(pady=5)
        tk.Label(left_frame, text="Parameters", font=("Arial", 10)).pack()

        self.intensity = tk.Scale(left_frame, from_=0, to=100, orient=tk.VERTICAL, label="Intensity")
        self.intensity.pack()

        tk.Button(left_frame, text="Stop", command=self.stop).pack(pady=10)

        # ----- Center Image -----
        center_image_frame = tk.Frame(self.root)
        center_image_frame.grid(row=1, column=1, sticky="n", padx=10, pady=5)

        image = Image.open("BodyPartPointer-1.png")
        image = image.resize((400, 600), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(center_image_frame, image=self.photo)
        image_label.pack()

        # ----- Graph Below Image -----
        graph_frame = tk.Frame(self.root)
        graph_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

        self.figure, self.ax = plt.subplots(figsize=(5, 2), dpi=100)
        self.line, = self.ax.plot(self.data)
        self.ax.set_title("Arduino Frequency Input")
        self.ax.set_ylim(0, 1024)
        self.canvas = FigureCanvasTkAgg(self.figure, master=graph_frame)
        self.canvas.get_tk_widget().pack()

        self.update_graph()

        # ----- Right Navigation Buttons -----
        right_frame = tk.Frame(self.root)
        right_frame.grid(row=1, column=2, rowspan=2, sticky="n", padx=10, pady=10)

        for text in ["Favourites", "Programmes", "Indications", "Memory", "Back"]:
            cmd = self.show_indications if text == "Indications" else self.init_main_screen if text == "Back" else None
            tk.Button(right_frame, text=text, width=15, command=cmd).pack(pady=2)

    def update_graph(self):
        # Simulated data
        value = random.randint(0, 1024)

        self.data.append(value)
        self.data.pop(0)

        self.line.set_ydata(self.data)
        self.line.set_xdata(range(len(self.data)))
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

        self.root.after(200, self.update_graph)

    def show_indications(self):
        self.clear_screen()

        tk.Label(self.root, text="Indications", font=("Arial", 16, "bold"), bg='blue', fg='white').grid(row=0, column=0, columnspan=3, sticky="ew")

        left = tk.Frame(self.root)
        left.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        indication_text = tk.Text(left, height=20, width=80)
        indication_text.insert(tk.END, "Indication: Chronic Pain\nProgramme: Traebert Current 2/5 ms 143 Hz\n")
        indication_text.insert(tk.END, "Primary Therapy Purpose: Analgesia\n")
        indication_text.insert(tk.END, "Further Therapy Purposes: Muscle relaxation, elasticity improvement\n")
        indication_text.insert(tk.END, "Treatment Recommendation: Clear sensation, 5 min\n")
        indication_text.pack()

        tk.Button(left, text="Back", command=self.init_main_screen).pack(pady=5)

        right = tk.Frame(self.root)
        right.grid(row=1, column=2, sticky="n", padx=10, pady=10)
        for text in ["Favourites", "Programmes", "Indications", "Memory", "Back"]:
            cmd = self.init_main_screen if text == "Back" else None
            tk.Button(right, text=text, width=15, command=cmd).pack(pady=2)

    def stop(self):
        messagebox.showinfo("Stop", "Therapy stopped")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectrotherapyGUI(root)
    root.mainloop()
