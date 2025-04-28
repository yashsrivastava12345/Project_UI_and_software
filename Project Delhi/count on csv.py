import tkinter as tk
from tkinter import messagebox
import csv
import os

CSV_FILE = 'count.csv'

# Function to read the current count from the CSV file
def read_count():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    return int(row[0])
    return 0

# Function to write the new count to the CSV file
def write_count(count):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([count])
def error_message(error):
    messagebox.showwarning("Time to service",error)
# Button click handler
def on_button_click():
    global count
    count += 1
    count_label.config(text=f"Count: {count}")
    write_count(count)
    if(count<15):
        pass
    elif(count < 20 and count >= 15):
        error_message("Critical Error found machine will stop working after "+str(20-count)+" iterations.")
    else:
        count_button.config(state="disable")
        error_message("Critical error encountered please contact service center.")
        pass

# GUI Setup
root = tk.Tk()
root.title("Click Counter")

# Read existing count if present
count = read_count()

count_label = tk.Label(root, text=f"Count: {count}", font=('Arial', 16))
count_label.pack(pady=10)

count_button = tk.Button(root, text="Click Me!", font=('Arial', 14), command=on_button_click)
count_button.pack(pady=10)


root.mainloop()
