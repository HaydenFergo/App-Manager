import tkinter as tk
from tkinter import messagebox
import webbrowser, os
run = 1

window = tk.Tk()
window.geometry("500x500")
window.title('Commands')
window.attributes('-topmost', True)
def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

def open_app(path, file_name):
    def inner_func():
        global run
        os.chdir(path)
        print(os.listdir())
        os.system(f'open {file_name}')
        app_menu.destroy()
        run = 0

    return inner_func

def quit_app(root):
    root.quit()

def open_window():
    window = tk.Tk()
    center_window(window)

class prompts_window():
    def open_app(root):
        def temp_func():
            global window, app_menu
            root.destroy()
            app_menu = tk.Tk()
            app_menu.geometry('500x500')
            app_menu.title('App Menu')
            tk.Label(text='Select one of the following apps:').pack()
            tk.Button(text='Visual Studio Code', command=open_app(f'/Applications/', 'Visual\ Studio\ Code.app')).pack()
            tk.Button(text='OBS', command=open_app(f'/Applications/', 'OBS.app')).pack()
            tk.Button(text='Opera GX', command=open_app(f'/Applications/', 'Opera\ GX.app')).pack()
            center_window(app_menu)
            app_menu.mainloop()

            print('App Menu Opened')
        return temp_func

while run == 1:
    tk.Label(text = 'Welcome!').pack()
    tk.Button(text="Open App", command=(prompts_window.open_app(window))).pack()
    tk.Button(text="UOW", command=...).pack()
    ...
    
    center_window(window)
    window.mainloop()