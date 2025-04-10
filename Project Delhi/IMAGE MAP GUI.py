import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define body part points with labels (x, y, label)
# Coordinates might need adjustment based on image scaling
image_path = "WhatsApp Image 2025-04-07 at 12.36.31.jpeg"
img = Image.open(image_path)
widthimg, heightimg = img.size

points = [
    (widthimg/3.3, heightimg/8.7, "Head"),
    (widthimg/2.63, heightimg/4, "Left Shoulder"),
    (widthimg/6.4, heightimg/2.5, "Right Elbow"),
    (widthimg/3, heightimg/2.1, "Abdomen"),
    (widthimg/7.5, heightimg/1.8, "Right Hand"),
    (widthimg/4.2, heightimg/1.38, "Right Knee"),
    (widthimg/3.4, heightimg/1.065, "Left Foot"),
    (widthimg/1.41, heightimg/6.8, "Neck (Back)"),
    (widthimg/1.415, heightimg/3.4, "Back"),
    (widthimg/1.395, heightimg/2.3, "Lower Back")
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
