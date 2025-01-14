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
        tk.Button(text="Open Website", command=sub_screen_1.open_website(window)).pack()
        tk.Button(text="Source Code", command=commands.open_website("https://github.com/HaydenFergo/App-Manager", window)).pack()

    def other():
        commands.center_window(window)
        window.mainloop()

class sub_screen_1():
    def open_app(root):
        def temp_func():
            root.destroy()
            commands.menus(root, 'App', 3, 'Application', 
                           'Visual Studio Code', 'Visual\ Studio\ Code', 
                           'OBS', 'OBS', 
                           'Opera GX', 'Opera\ GX', 
                           None, None,
                           None, None)
            print('App Menu Opened')
        return temp_func

    def open_website(root):
        def temp_func():
            global website_menu
            root.destroy()
            website_menu = tk.Tk()
            website_menu.geometry('500x500')
            website_menu.title('Website Menu')
            tk.Label(text='Select one of the following categories:').pack()
            tk.Button(text='Games', command=sub_screen_2.games(website_menu)).pack()
            tk.Button(text='School', command=...).pack()
            tk.Button(text='University', command=...).pack()
            commands.center_window(website_menu)
            website_menu.mainloop()
        return temp_func
    
class sub_screen_2():
    def games(root):
        def temp_func():
            global game_menu
            root.destroy()
            game_menu = tk.Tk()
            game_menu.geometry('500x500')
            game_menu.title('Game Menu')
            tk.Label(text='Select one of the following games:').pack()
            tk.Button(text='Chess', command=commands.open_website("https://chess.com", website_menu)).pack()
            commands.center_window(website_menu)
            game_menu.mainloop()
        return temp_func
    def school(root):
        global school_menu

class commands():
    def menus(root, menu_name, num_buttons, type_of_button, name1, button1, name2, button2, name3, button3, name4, button4, name5, button5):
        global menu
        menu = tk.Tk()
        menu.geometry('500x500')
        menu.title(f'{menu_name} Menu')
        tk.Label(text=f'Select one of the following:')
        match type_of_button:
            case 'Application':
                for i in range(num_buttons):
                    match i:
                        case 0:
                            print('case 0')
                            tk.Button(text=name1, command=commands.open_app(f'/Applications/', f'{button1}.app')).pack()
                        case 1:
                            tk.Button(text=name2, command=commands.open_app(f'/Applications/', f'{button2}.app')).pack()
                        case 2:
                            tk.Button(text=name3, command=commands.open_app(f'/Applications/', f'{button3}.app')).pack()
                        case 3:
                            tk.Button(text=name4, command=commands.open_app(f'/Applications/', f'{button4}.app')).pack()
                        case 4:
                            tk.Button(text=name5, command=commands.open_app(f'/Applications/', f'{button5}.app')).pack()
            case _:
                print(None)
        commands.center_window(menu)
        menu.mainloop()

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
            run = 0
        return inner_func

    def open_website(website, root):
        def inner_func():
            webbrowser.open(website)
            commands.quit_app(root)
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
    global run
    try:
        main_screen.window_attrib()
        main_screen.buttons()
        main_screen.other()
    except:
        run = 0


while run == 1:
    main()

