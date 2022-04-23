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

    def change_theme():
        # NOTE: The theme's real name is sun-valley-mode
        if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            # Set light theme
            root.tk.call("set_theme", "light")
        else:
            # Set light theme
            root.tk.call("set_theme", "dark")

    def donothing():
        print('Command not implemented')

    menubar = tk.Menu(root)
    #file menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    #edit menu
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    #options Menu
    optionmenu = tk.Menu(menubar,tearoff=0)
    optionmenu.add_command(label="Change Theme",command=change_theme)
    menubar.add_cascade(label="Options",menu=optionmenu)
    #help menu
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    #add menu to root
    root.config(menu=menubar)
    ## start
    root.mainloop()

if __name__ == '__main__':
    start()