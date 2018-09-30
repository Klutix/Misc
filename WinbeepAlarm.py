import time
import winsound
import threading

class WinBeepAlarm:
    
    def __init__(self):
        self.stop_alarm = False
        self.b = None
        self.f = None
        
    def start(self):
        b = threading.Thread(name='background', target=self.background)
        f = threading.Thread(name='foreground', target=self.foreground)
        b.start()
        f.start()

    def alarm(self):
        while True:
            if self.stop_alarm==True:
                break
            winsound.Beep(400,200)
            time.sleep(.1)

    def background(self):
        self.alarm()


    def foreground(self):
        val = input("Press Any Key To Stop\n")
        if val != "":
            self.stop_alarm = True
            

