import tkinter as tk

def show_notification():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    # Yeni boyut: 600x240 (önceki 300x120 idi)
    popup_width = 600
    popup_height = 240

    x = (screen_width // 2) - (popup_width // 2)
    y = (screen_height // 2) - (popup_height // 2)

    popup = tk.Toplevel()
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.title("Health Services")

    # Font boyutu 12 → 24 yapıldı
    label = tk.Label(
        popup,
        text="🐋Water Yourself!🐋\nWhen did you drink water last time?",
        font=("Arial", 24),
        justify="center"
    )
    label.pack(expand=True)

    popup.after(5000, popup.destroy)

def schedule_notifications():
    show_notification()
    root.after(3600000, schedule_notifications)  # 1 saat sonra tekrar

root = tk.Tk()
root.withdraw()  # Ana pencereyi gizle

schedule_notifications()

root.mainloop()