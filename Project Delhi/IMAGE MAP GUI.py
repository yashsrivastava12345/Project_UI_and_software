import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define body part points with labels (x, y, label)
# Coordinates might need adjustment based on image scaling
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

# Detection radius in pixels for clicks
RADIUS = 15

# Function to handle click event
def on_click(event):
    for x, y, label in points:
        if (event.x - x) ** 2 + (event.y - y) ** 2 <= RADIUS ** 2:
            messagebox.showinfo("Body Part", f"You clicked on: {label}")
            break

# Set up main window
root = tk.Tk()
root.title("Body Region Selector")

# Load the image
image_path = "WhatsApp Image 2025-04-07 at 12.36.31.jpeg"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

# Create a canvas and add the image
canvas = tk.Canvas(root, width=img.width, height=img.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Draw circles at the specified points
for x, y, _ in points:
    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, outline="Blue", width=2)

# Bind mouse click
canvas.bind("<Button-1>", on_click)

# Run the GUI loop
root.mainloop()
