import json
import os
import customtkinter as ctk

alarm_list =[]
def saveAlarm():
    with open("alarmlist.json", "w") as file:
        json.dump(alarm_list,file)
def load_alarm(alarm_display_widget: ctk.CTkTextbox):
    global alarm_list
    if os.path.exists("alarmlist.json"):
        with open("alarmlist.json" ,"r") as file:
            alarm_list = json.load(file)
            for alarm in alarm_list:
                alarm_display_widget.insert("end", alarm + "\n")