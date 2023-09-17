# Import module 
from tkinter import *
import tkinter as tk
import threading
import time
import sys
import os
from PIL import Image, ImageTk
from tkinter import scrolledtext

app = tk.Tk()
app.title("Jarvis Voice Assistant")

# Set the window size and make it resizable
app.geometry("400x400")
app.resizable(True, True)

# Function to update the background image size
def update_bg_size(event):
    bg_label.config(width=event.width, height=event.height)

# Add a background image
bg_image = Image.open('ai.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind the update_bg_size function to window resize
app.bind("<Configure>", update_bg_size)

def run_jarvis():
    # Execute the entire jarvis.py script
    os.system(f"{sys.executable} jarvis.py")

def start_assistant():
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Jarvis is listening...\n")
    output_text.config(state=tk.DISABLED)
    threading.Thread(target=run_jarvis).start()
    

input_label = tk.Label(app, text="Say a command:", font=("Helvetica", 12, "bold"))
input_label.pack(side="top")  # Place at the top


output_text = tk.Text(app, height=20, width=80, state=tk.DISABLED, bg="black", fg="white")
output_text.pack()
# Other parts of your code...


start_button = tk.Button(app, text="Start Jarvis", command=start_assistant)
start_button.pack(pady=10)  # Add vertical padding of 10

exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.pack(pady=5)  # Add vertical padding of 5

app.mainloop()

