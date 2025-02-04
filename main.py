from tkinter import Tk
from views.main_windows import MainWindow, ScrollBar

def main():
    root = Tk()
    app = MainWindow(root)
    app.pack()
    app_scrollbar = ScrollBar(root)
    app_scrollbar.pack()
    root.mainloop()

if __name__ == "__main__":
    main()