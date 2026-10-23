from hashlib import algorithms_available

import customtkinter as ctk
import time
import datetime

alarm_time = None
alarm_active =False
def updateClock():
    current_time= datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    app.after(1000,updateClock)

def checkAlarm():
    while True:
        if alarm_active and alarm_time:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("Alarm Ring")
                alarm_active =False
        time.sleep(1)
app = ctk.CTk()
app.title("OXAlarm")
app.geometry("600*600")
tab_view =ctk.CTkTabview(master= app)
tab_view.pack(padx =20, pady =20, expand=True, fill="both")
tab_view.add("Clock")
tab_view.add("Alarm")
tab_view.add("Timer")
tab_view.add("Focus")
tab_view.add("Task")
tab_view.add("Sound Maker")
clock_label =ctk.CTkLabel(master=tab_view.tab("Clock"), text="00:00:00")
clock_label.pack(pady=(40,20))
updateClock()

sound_label = ctk.CTkLabel(master=tab_view.tab("Sound Maker"), text="    ")
sound_label.pack(pady=50)
app.mainloop()