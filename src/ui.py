import customtkinter as tk
from main import Sleepnow, start_threading, stop_scheduler
from datetime import datetime, timedelta, time
import threading

def lancer_ui():

    tk.set_appearance_mode("Dark")

    app=tk.CTk()
    app.title("Sleepnow")
    app.geometry("1000x800")

    label=tk.CTkLabel(app, text="Choisi tes horaires", font=("Arial", 45))
    label.pack(pady=10)

    heures = [f"{i:2}" for i in range(24)]
    minutes= [f"{i:02}" for i in range(61)]

    label=tk.CTkLabel(app, text="heures :", font=("Arial", 25))
    label.pack(pady=5)

    dropdown_h = tk.CTkOptionMenu(app, values=heures,width=200, height = 60,font=("Arial", 20))
    dropdown_h.pack(pady=20)

    label=tk.CTkLabel(app, text="minutes :", font=("Arial", 25))
    label.pack(pady=5)

    dropdown_m = tk.CTkOptionMenu(app, values=minutes, width=200, height = 60,font=("Arial", 20))
    dropdown_m.pack(pady=20)


    #start threading
    def on_click_start(): 
        heures=dropdown_h.get()
        minutes=dropdown_m.get()
        limite=time(int(heures),int(minutes))
        status_label.configure(text=f"Scheduler lancé avec limite :{heures}h{minutes}")
        start_threading(limite)

    def on_click_stop():
        stop_scheduler()
        status_label.configure(text="Scheduler arrêté")

    button_frame = tk.CTkFrame(app)
    button_frame.pack(pady=10)

    button_start = tk.CTkButton(button_frame , text="Start", command=on_click_start, width=300, height = 100, font=("Arial", 40))
    button_start.grid(row=0, column=0, padx=15, pady=20)

    button_stop = tk.CTkButton(button_frame , text="Stop", command=on_click_stop, width=300, height = 100, font=("Arial", 40))
    button_stop.grid(row=0, column=1, padx=15, pady=20)

    status_label = tk.CTkLabel(app, text="",font=("Arial", 35))
    status_label.pack(pady=10)

    def toggle_info():
        if info_label.winfo_viewable():
            info_label.pack_forget()  # Masquer
        else:
            info_label.pack(pady=10, padx=10)  # Afficher

    mode_nuit_btn = tk.CTkButton(app, text="Mode nuit", command=toggle_info,width=120, height=40, font=("Helvetica", 18))
    mode_nuit_btn.pack(pady=20)

    info_label = tk.CTkLabel(app, text="Si vous choisissez une horaire avant 6h, l’application activera automatiquement le mode nuit. Les programmes sélectionnés seront bloqués jusqu’au lendemain matin pour vous aider à respecter votre temps de repos.",
        font=("Helvetica", 30),
        justify="left",  
        wraplength=400  
    )

    app.mainloop()