import customtkinter as tk
from main import Sleepnow, start_threading, stop_scheduler
from datetime import datetime, timedelta, time
import threading

import customtkinter as tk
from datetime import time
from main import start_threading, stop_scheduler


def lancer_ui():
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("blue")

    app = tk.CTk()
    app.title("JustaLast - Modern Time Scheduler")
    app.geometry("600x700")
    app.configure(fg_color="#0d1b2a")  # solid dark background

    # --- Main frame (the "card") ---
    main_frame = tk.CTkFrame(app, corner_radius=20, fg_color="#1b263b")
    main_frame.pack(pady=40, padx=40, fill="both", expand=True)

    # Title
    title = tk.CTkLabel(main_frame, text="JustaLast",
                        font=("Arial Rounded MT Bold", 40, "bold"))
    title.pack(pady=(30, 5))

    subtitle = tk.CTkLabel(main_frame, text="Modern Time Scheduler",
                           font=("Arial", 18))
    subtitle.pack(pady=(0, 30))

    # Time selectors
    heures = [f"{i:02}" for i in range(24)]
    minutes = [f"{i:02}" for i in range(60)]

    frame_time = tk.CTkFrame(main_frame, corner_radius=15, fg_color="#24344d")
    frame_time.pack(pady=20, padx=20)

    label_h = tk.CTkLabel(frame_time, text="Hours", font=("Arial", 20))
    label_h.grid(row=0, column=0, padx=20, pady=10)

    dropdown_h = tk.CTkOptionMenu(frame_time, values=heures,
                                  width=120, height=40, font=("Arial", 18))
    dropdown_h.grid(row=1, column=0, padx=20, pady=10)

    label_m = tk.CTkLabel(frame_time, text="Minutes", font=("Arial", 20))
    label_m.grid(row=0, column=1, padx=20, pady=10)

    dropdown_m = tk.CTkOptionMenu(frame_time, values=minutes,
                                  width=120, height=40, font=("Arial", 18))
    dropdown_m.grid(row=1, column=1, padx=20, pady=10)

    # Time display
    time_display = tk.CTkLabel(main_frame, text="--:--",
                               font=("Arial Rounded MT Bold", 36, "bold"))
    time_display.pack(pady=20)

    # Start/Stop logic
    def on_click_start():
        h, m = dropdown_h.get(), dropdown_m.get()
        limite = time(int(h), int(m))
        time_display.configure(text=f"{h}:{m}")
        status_label.configure(text=f"Started at {h}:{m}", text_color="green")
        start_threading(limite)

    def on_click_stop():
        stop_scheduler()
        status_label.configure(text="Stopped", text_color="red")

    # Buttons
    button_frame = tk.CTkFrame(main_frame, fg_color="transparent")
    button_frame.pack(pady=20)

    tk.CTkButton(button_frame, text="▶ Start", command=on_click_start,
                 width=160, height=60, font=("Arial Rounded MT Bold", 22),
                 fg_color="green", hover_color="#2eb82e").grid(row=0, column=0, padx=20)

    tk.CTkButton(button_frame, text="■ Stop", command=on_click_stop,
                 width=160, height=60, font=("Arial Rounded MT Bold", 22),
                 fg_color="gray30", hover_color="gray45").grid(row=0, column=1, padx=20)

    # Info label (hidden)
    info_label = tk.CTkLabel(
        main_frame,
        text="If you select a time between 00:00 and 06:00, "
             "Night Mode will automatically activate for the next day.",
        font=("Arial", 16), justify="center", wraplength=400
    )

    def toggle_info():
        if info_label.winfo_ismapped():
            info_label.pack_forget()
        else:
            info_label.pack(pady=15, padx=20)

    tk.CTkButton(main_frame, text="ℹ", width=40, height=40,
                 font=("Arial", 20), command=toggle_info).pack(pady=(10, 5))

    # Status
    status_label = tk.CTkLabel(main_frame, text="", font=("Arial", 20))
    status_label.pack(pady=15)

    app.mainloop()


if __name__ == "__main__":
    lancer_ui()
