from tkinter import *
from time import sleep
import psutil


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
    sleep(10)
    p.resume()


def click():
    button.config(state="disabled", text="    Everything is Done :)    ")
    privatesessionmaker()


window = Tk()
window.title('Private Session Maker')
window.iconbitmap('gta 5.ico')

height = 100
width = 640
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)

# Button
button = Button(window,
                text="Click and wait 10 seconds",
                command=click,
                font=("Comic Sans", 40),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                compound='bottom')
button.pack()

window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.mainloop()
