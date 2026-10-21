from hashlib import algorithms_available

import customtkinter as ctk

app = ctk.CTk()
app.title("OXAlarm")
app.geometry("600*600")
tab_view =ctk.CTkTabview(master= app)
tab_view.pack(padx =20, pady =20, expand=True, fill="both")
tab_view.add("Alarm")
tab_view.add("Timer")
tab_view.add("Focus")
tab_view.add("Task")
tab_view.add("Sound Maker")
alarm_label =ctk.CTkLabel(master=tab_view.tab("Alarm"), text="This is my alarm")
alarm_label.pack(pady= 50)
sound_label = ctk.CTkLabel(master=tab_view.tab("Sound Maker"), text="    ")
sound_label.pack(pady=50)
app.mainloop()