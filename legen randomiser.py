import random 
from tkinter import messagebox 
from tkinter import *
test = Tk()
test.geometry("400x200")
test.title("Randomiser")
import random

canvasscreen = Canvas(test, width = 400, height = 500)
canvasscreen.pack()

entrybox = Entry (test)
canvasscreen.create_window(200, 50,window=entrybox)


def game():
    inputs = entrybox.get()
    if inputs == "apex" :
        Apcharacters = ("octane", "wraith", "gibraltor", "mirage", "pathfinder" "bloodhound", "lifeline", "wattson", "caustic", "crypto", "loba", "revenant", "horizon", "bangalore", "valkarie", "seer", "fuse", "vantage", "ash", "catalyst", "mad maggie", "rampart", "new castle", "ballistic")
        import tkinter
        from tkinter import messagebox
        import ttk
        window = tkinter.Tk()
        window.wm_withdraw()
        window.geometry("1x1+"+str(window.winfo_screenwidth())
                +"+"+str(window.winfo_screenheight()))
        messagebox.showinfo(title="your character",message= random.choice(Apcharacters))
            

button = Button(text='randomise', command=game)

canvasscreen.create_window(200, 100, window=button)
test.mainloop()