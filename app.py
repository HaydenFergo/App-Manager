import tkinter as tk
import webbrowser, os
import sub
run = 1
super_important_stat = 0

window = tk.Tk()

class main_screen():

    def window_attrib():
        window.geometry("500x500")
        window.title('Commands')
        window.attributes('-topmost', True)

    def buttons():
        tk.Button(text="Open App", command=sub_screen_1.open_app(window)).pack()
        tk.Button(text="Source Code", command=commands.open_website("https://github.com/HaydenFergo/App-Manager")).pack()

    def other():
        commands.center_window(window)
        window.mainloop()

class sub_screen_1():
    def open_app(root):
        def temp_func():
            global app_menu
            root.destroy()
            app_menu = tk.Tk()
            app_menu.geometry('500x500')
            app_menu.title('App Menu')
            tk.Label(text='Select one of the following apps:').pack()
            tk.Button(text='Visual Studio Code', command=commands.open_app(f'/Applications/', 'Visual\ Studio\ Code.app')).pack()
            tk.Button(text='OBS', command=commands.open_app(f'/Applications/', 'OBS.app')).pack()
            tk.Button(text='Opera GX', command=commands.open_app(f'/Applications/', 'Opera\ GX.app')).pack()
            commands.center_window(app_menu)
            app_menu.mainloop()

            print('App Menu Opened')
        return temp_func

class commands():

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
            os.system(f'open {file_name}')
            commands.quit_app(app_menu)
            run = 0
        return inner_func

    def easter_egg():
        global super_important_stat
        super_important_stat += 1
        if super_important_stat == 15:
            tk.Label(text='hi').pack()

    def open_website(website):
        def inner_func():
            webbrowser.open(website)
            commands.quit_app(window)
        return inner_func

    def quit_app(root):
        global run
        root.destroy()
        run = 0

    def open_window():
        window = tk.Tk()
        commands.center_window(window)

    def uni():
        commands.open_website(f'{sub.private_link_may}')
        commands.open_website(f'{sub.private_link_moo}')
        commands.open_website(f'{sub.private_link_soul}')

def main():
    main_screen.window_attrib()
    main_screen.buttons()
    main_screen.other()


while run == 1:
    main()

