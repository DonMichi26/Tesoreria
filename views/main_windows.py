import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Mi Aplicación")
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self.master, text="¡Bienvenido a la App!", font=("Arial", 16))
        label.pack(pady=20)

class ScrollBar(tk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Scrollbar")
        self.create_widgets()

    def create_widgets(self):
        self.combo = ttk.Combobox(self, state="readonly", values=["Opción 1", "Opción 2", "Opción 3", "Opción 4"])
        self.combo.pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)
        