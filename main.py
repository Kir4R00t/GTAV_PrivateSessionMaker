from tkinter import *
from tkinter import ttk
from time import sleep
import psutil

# Initializing window GUI
root = Tk()
root.title('Private Session Maker')
root.iconbitmap('gta 5.ico')
height = 140
width = 500
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)


# Suspending game process, thus "kicking" all players from your session
def privatesessionmaker():
    p_name = "GTA5.exe"
    pid = None

    for proc in psutil.process_iter():
        if p_name in proc.name():
            pid = proc.pid
            break

    p = psutil.Process(pid)
    p.suspend()
    for i in range(10):
        progress['value'] += 10
        root.update_idletasks()
        sleep(1)
    p.resume()
    button.config(state="disabled", text="    Everything is Done :)    ")


# Create a style for the progress bar to increase its height
style = ttk.Style(root)
style.configure("TProgressbar", thickness=30)

# Enlarged progress bar
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="TProgressbar")
progress.pack(pady=20)

# Button
button = Button(root, text="Create a private session", command=privatesessionmaker, font=("Comic Sans", 14), pady=10,
                state=ACTIVE)
button.pack()

root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.mainloop()
