from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%M/%Y")
        print("The Set Time is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time's up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def error_check(var, min, max):
    a = var.get()
    if a == "":
        return False
    else:
        try:
            a = int(a)
            if a >= min and a <= max:
                return True
            else:
                print("out of range")
                return False
        except:
            print("not a number")

def actual_time():
    if error_check(hour, 0, 23):
        if error_check(min, 0, 59):
            if error_check(sec, 0, 59):
                set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
                alarm(set_alarm_timer)
            else:
                print("Empty sec column")
        else:
            print("Empty min column")
    else:
        print("Empty hour column")

clock = Tk()
clock.title("De Alarm")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24h format", fg="red", bg="black", font="Arial").place(x=60, y= 120)
addTime = Label(clock, text="Hour  Min   Sec", font=60).place(x=110)
setYourAlarm = Label(clock, text="Enter Time:   ", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)
hour = StringVar()
min = StringVar()
sec = StringVar()
hourTime = Entry(clock, textvariable = hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable = min, bg="pink", width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable = sec, bg="pink", width=15).place(x=200, y=30)
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)
clock.mainloop()