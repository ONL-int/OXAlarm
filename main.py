import customtkinter as ctk
import time
import datetime
import threading
import json
import os


alarm_list = []
alarm_time = None
alarm_active =False
def saveAlarm():
    with open("alarmlist.json", "w") as file:
        json.dump(alarm_list,file)
def load_alarm():
    global alarm_list
    if os.path.exists("alarmlist.json"):
        with open("alarmlist.json" ,"r") as file:
            alarm_list = json.load(file)
            for alarm in alarm_list:
                alarm_display.insert("end", alarm + "\n")
def updateClock():
    current_time= datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    app.after(1000,updateClock)

def checkAlarm():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time in alarm_list:
            print("Alarm Ring:"+ current_time)
            alarm_list.remove(current_time)
            saveAlarm()
        time.sleep(1)

app = ctk.CTk()
app.title("OXAlarm")
app.geometry("600x600")
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
alarm_thread = threading.Thread(target=checkAlarm, daemon=True)
alarm_thread.start()
sound_label = ctk.CTkLabel(master=tab_view.tab("Sound Maker"), text="    ")
sound_label.pack(pady=50)
alarm_instruction =ctk.CTkLabel(master=tab_view.tab("Alarm"),text="Enter Time (HH:MM:SS):")
alarm_instruction.pack(pady=(40,10))
alarm_entry =ctk.CTkEntry(master=tab_view.tab("Alarm"), width=150)
alarm_entry.pack(pady =10)
def setAlarm():
    new_alarm = alarm_entry.get()
    if new_alarm != "":
        alarm_list.append(new_alarm)
        alarm_display.insert("end",new_alarm + "\n")
        alarm_entry.delete(0, "end")
        saveAlarm()
        print ("Alarm set for" + new_alarm)
set_button = ctk.CTkButton(master=tab_view.tab("Alarm"), text="Set Alarm", command=setAlarm)
set_button.pack(pady =20)

alarm_display= ctk.CTkTextbox(master=tab_view.tab("Alarm"),width=200, height=140)
alarm_display.pack(pady = 20)
load_alarm()
app.mainloop()