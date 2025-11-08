import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from time import sleep
from threading import Thread

started = False
time = 1
_passed_time = 1
clicks = 0

def cps_test():
    global clicks
    if started:
        clicks += 1
        cps_label.set(str(clicks))
    else:
        output_string.set("")
        passed_time.set(time)
        cps_label.set("1")
        Thread(target=cps_loop).start()
        clicks += 1

def cps_loop():
    global _passed_time, time, started
    started = True
    _passed_time = time

    while _passed_time != 0:
        sleep(1)
        _passed_time += -1
        passed_time.set(int(_passed_time))
    started = False
    cps = clicks / time
    cps_label.set("Counting...")
    output_string.set(f"cps : {cps}")
    messagebox.showinfo(message=f"Кликов сделано: {clicks}\nТвой CPS: {cps}", title="CPS Test ")
    sleep(0.5)
    reset()

def reset():
    global clicks, started
    cps_label.set("Кликай!")
    clicks = 0
    started = False

def switch(value):
    global time
    passed_time.set(int(value))
    time = value

# window
window = ttk.Window(themename = "darkly")
window.title("CPS Test")
window.geometry("500x350")

#Title
titel_string = ttk.StringVar()
titel_label = ttk.Label(master = window, text = "CPS Test by Nikitich1423", font = "Calibri 24 bold")
titel_label.pack()

#Set Time
input_frame = ttk.Frame(master = window)

time1 = ttk.Button(master = input_frame, text = "1 сек.", command=lambda: switch(1)).pack(side = "left",padx=10)
time2 = ttk.Button(master = input_frame, text = "2 сек.", command=lambda: switch(2)).pack(side = "left",padx=10)
time5 = ttk.Button(master = input_frame, text = "5 сек.", command=lambda: switch(5)).pack(side = "left",padx=10)
time10 = ttk.Button(master = input_frame, text = "10 сек.", command=lambda: switch(10)).pack(side = "left",padx=10)
time30 = ttk.Button(master = input_frame, text = "30 сек.", command=lambda: switch(30)).pack(side = "left",padx=10)
time60 = ttk.Button(master = input_frame, text = "60 сек.", command=lambda: switch(60)).pack(side = "left",padx=10)
time100 = ttk.Button(master = input_frame, text = "100 сек.", command=lambda: switch(100)).pack(side = "left",padx=10)

input_frame.pack(pady=10)

#Display time
passed_time = tk.StringVar()
passed_time.set(f"{_passed_time} сек.")
time_label = tk.Label(master = window, text = "0" + "сек.", font = "Calibri 24 bold", textvariable=passed_time)
time_label.pack()

#click box
cps_label = tk.StringVar()
cps_label.set("Кликай!")
cp = tk.Button(master=window, text="CPS", command=cps_test, font="Calibri 22", width=20, textvariable=cps_label)
cp.pack(pady=20)

#Output
output_string = tk.StringVar()
output_label = tk.Label(master = window, text = "output", font = "Calibri 22", textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()