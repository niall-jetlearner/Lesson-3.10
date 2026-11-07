import tkinter as tk
import random

root = tk.Tk()
root.title("Color Magic")
root.geometry("400x300")

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

def change_color():
    random_color = random.choice(colors)
    root.configure(bg=random_color)

button = tk.Button(
    root,
    text= "Change Color",)