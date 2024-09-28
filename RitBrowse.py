import webview
import tkinter as tk
from tkinter import simpledialog, Menu

browser_window = None

def enter_url():
    global browser_window
    root = tk.Tk()
    root.withdraw()
    url = simpledialog.askstring("Enter URL", "Please enter a URL to load:")
    if url:
        if browser_window is not None:
            browser_window.load_url(url)

def setup_menu():
    root = tk.Tk()
    root.withdraw()
    
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Enter URL", command=enter_url)

    root.mainloop()

def start_browser():
    global browser_window
    browser_window = webview.create_window('RitBrowse', 'https://www.example.com')
    webview.start()

if __name__ == '__main__':
    setup_menu()
    start_browser()
