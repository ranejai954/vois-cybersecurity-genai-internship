import tkinter as tk
from datetime import datetime

LOG_FILE = "keylogs.txt"
logging_active = False

def log_key(event):
    if not logging_active:
        return

    key = event.keysym

    if key == "space":
        key = " "
    elif key == "Return":
        key = "[ENTER]\n"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif len(key) > 1:
        key = f"[{key}]"

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} : {key}\n")

def start_logging():
    global logging_active
    logging_active = True
    status_label.config(text="Keylogger is RUNNING", fg="green")

def stop_logging():
    global logging_active
    logging_active = False
    status_label.config(text="Keylogger is STOPPED", fg="red")

root = tk.Tk()
root.title("Educational Keylogger Demo")
root.geometry("520x320")
root.resizable(True, True)

title = tk.Label(
    root,
    text="Keylogger Demonstration (Educational Purpose)",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

info = tk.Label(
    root,
    text="Press START to begin keylogging.\nOnly keystrokes in this window are recorded.",
    font=("Arial", 11)
)
info.pack(pady=5)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=15)
entry.focus()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_btn = tk.Button(
    button_frame,
    text="Start",
    command=start_logging,
    width=12,
    font=("Arial", 10)
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(
    button_frame,
    text="Stop",
    command=stop_logging,
    width=12,
    font=("Arial", 10)
)
stop_btn.grid(row=0, column=1, padx=10)

status_label = tk.Label(
    root,
    text="Press Start to begin logging",
    font=("Arial", 11),
    fg="orange"
)
status_label.pack(pady=15)

root.bind("<Key>", log_key)

root.mainloop()
