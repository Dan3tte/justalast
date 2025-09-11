import customtkinter as tk
from main import Sleepnow, start_threading, stop_scheduler
from datetime import datetime, timedelta, time
import threading



def lancer_ui():
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("blue")

    app = tk.CTk()
    app.title("JustaLast")
    app.geometry("600x700")
    app.iconbitmap("JaL.ico")  

    # --- Gradient background ---
    canvas = tk.CTkCanvas(app, width=600, height=700, highlightthickness=0, bg="#0d1b2a")
    canvas.pack(fill="both", expand=True)

    steps = 100
    for i in range(steps):
        color_value = int(13 + (30 - 13) * (i / steps))  # from #0d1b2a → #1e2a38
        color = f"#{color_value:02x}{color_value:02x}{(42 + i // 2):02x}"
        canvas.create_rectangle(0, i * 7, 600, (i + 1) * 7, outline="", fill=color)

    # --- Main card ---
    main_frame = tk.CTkFrame(app, corner_radius=20, fg_color="#1b263b")
    canvas.create_window(300, 350, window=main_frame, width=500, height=600)

    # --- Scrollable content inside the card ---
    content = tk.CTkScrollableFrame(main_frame, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=10, pady=10)

    # Title
    title = tk.CTkLabel(content, text="JustaLast",
                        font=("Arial Rounded MT Bold", 40, "bold"))
    title.pack(pady=(30, 5))

    subtitle = tk.CTkLabel(content, text="Gaming stays fun. Sleep stays safe",
                           font=("italic_font", 15, "italic"))
    subtitle.pack(pady=(0, 30))

    # Time selectors
    heures = [f"{i:02}" for i in range(24)]
    minutes = [f"{i:02}" for i in range(60)]

    frame_time = tk.CTkFrame(content, corner_radius=15, fg_color="#24344d")
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
    time_display = tk.CTkLabel(content, text="--:--",
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
    button_frame = tk.CTkFrame(content, fg_color="transparent")
    button_frame.pack(pady=20)

    tk.CTkButton(button_frame, text="▶ Start", command=on_click_start,
                 width=160, height=60, font=("Arial Rounded MT Bold", 22),
                 fg_color="green", hover_color="#2eb82e").grid(row=0, column=0, padx=20)

    tk.CTkButton(button_frame, text="■ Stop", command=on_click_stop,
                 width=160, height=60, font=("Arial Rounded MT Bold", 22),
                 fg_color="gray30", hover_color="gray45").grid(row=0, column=1, padx=20)

    # Status
    status_label = tk.CTkLabel(content, text="", font=("Arial", 20))
    status_label.pack(pady=10)

    # Info label (hidden at start)
    info_label = tk.CTkLabel(
        content,
        text="If you select a time between 00:00 and 06:00, "
             "Night Mode will automatically activate for the next day.",
        font=("Arial", 16), justify="center", wraplength=400
    )
    info_visible = False

    def toggle_info():
        nonlocal info_visible
        if info_visible:
            info_label.pack_forget()
            info_visible = False
        else:
            info_label.pack(pady=15, padx=20)
            info_visible = True

    # Info button
    tk.CTkButton(content, text="ℹ", width=40, height=40,
                 font=("Arial", 20), command=toggle_info).pack(pady=(5, 10))

    app.mainloop()


if __name__ == "__main__":
    lancer_ui()
