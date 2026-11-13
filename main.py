import customtkinter as ctk
import time
import datetime
import threading
import json_manage


alarm_time = None
alarm_active =False

def updateClock():
    current_time= datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    app.after(1000,updateClock)

def checkAlarm():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time in json_manage.alarm_list:
            print("Alarm Ring:"+ current_time)
            json_manage.alarm_list.remove(current_time)
            json_manage.saveAlarm()
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
# sound_label = ctk.CTkLabel(master=tab_view.tab("Sound Maker"), text="    ")
# sound_label.pack(pady=50)
alarm_instruction =ctk.CTkLabel(master=tab_view.tab("Alarm"),text="Enter Time (HH:MM:SS):")
alarm_instruction.pack(pady=(40,10))
alarm_entry =ctk.CTkEntry(master=tab_view.tab("Alarm"), width=150)
alarm_entry.pack(pady =10)
def setAlarm():
    new_alarm = alarm_entry.get()
    if new_alarm != "":
        json_manage.alarm_list.append(new_alarm)
        alarm_display.insert("end",new_alarm + "\n")
        alarm_entry.delete(0, "end")
        json_manage.saveAlarm()
        print ("Alarm set for" + new_alarm)
set_button = ctk.CTkButton(master=tab_view.tab("Alarm"), text="Set Alarm", command=setAlarm)
set_button.pack(pady =20)

alarm_display= ctk.CTkTextbox(master=tab_view.tab("Alarm"),width=200, height=140)
alarm_display.pack(pady = 20)

wave_label= ctk.CTklabel(master=tab_view.tab("Sound Maker"), text="Waveform:")
wave_label.pack(pady=(20,0))
wave_dropdwon =ctk.CTkComboBox(master= tab_view.tab("Sound Maker"))
json_manage.load_alarm(alarm_display)
app.mainloop()