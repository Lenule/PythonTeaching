
import tkinter
from bulb import Bulb
import threading

class Semaphore(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def callback(self):
        self.root.quit()

    def run(self):
        top = tkinter.Tk()
        top.protocol("WM_DELETE_WINDOW", self.callback)
        top.geometry('80x240')

        self.red = Bulb(top, (0,0), 'red', 'off')
        self.yellow = Bulb(top, (0,80), 'yellow', 'off')
        self.green = Bulb(top, (0,160), 'green', 'off')

        def animate(bulbs):
            for bulb in bulbs:
                bulb.update()
            
            top.after(120, animate, bulbs)

        top.after(100, animate, [self.red, self.yellow, self.green])
        self.root = top

        self.root.mainloop()
