import tkinter as tk
from tkinter import ttk

def start():
    root = tk.Tk()
    root.geometry("500x800")
    # Pack a big frame so, it behaves like the window background
    big_frame = ttk.Frame(root)
    big_frame.pack(fill="both", expand=True)
    root.title('BensonAssKicker')

    # Set the initial theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")
    
    def move_window(event):
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def create_titlebar():
        root.overrideredirect(True) # turns off title bar, geometry
        root.geometry('400x100+200+200') # set new geometry

        # make a frame for the title bar
        title_bar = tk.Frame(root, bg='white', relief='raised', bd=2)

        # put a close button on the title bar
        close_button = tk.Button(title_bar, text='X', command=root.destroy)

        # a canvas for the main area of the window
        window = tk.Canvas(root, bg='black')

        # pack the widgets
        title_bar.pack(expand=1, fill='x')
        close_button.pack(side='right')
        window.pack(expand=1, fill='both')

        # bind title bar motion to the move window function
        title_bar.bind('<B1-Motion>', move_window)

    def change_theme():
        # NOTE: The theme's real name is sun-valley-mode
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            # Set light theme
            root.tk.call("set_theme", "light")
        else:
            # Set light theme
            root.tk.call("set_theme", "dark")

    # Remember, you have to use ttk widgets

    button = ttk.Button(big_frame, text="change theme!", command=change_theme)
    button.pack()

    #TopMenu
    #menu1_master = tk.Tk()
    variable = tk.StringVar(root)
    variable.set("one") # default value
    menu1 = ttk.OptionMenu(root, variable, "one", "two", "three")
    menu1.pack()

    root.mainloop()

if __name__ == '__main__':
    start()