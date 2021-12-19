from tkinter import *
from array import *
import random
import time

now_humidity = random.randint(0, 100)
now_temp = random.randint(-10, 40)

array_humidity = [now_humidity]
array_temp = [now_temp]

#создание окна    
window = Tk()
window.geometry('510x260')
window.title("Система регистрации температуры и влажности")
window["bg"] = "lightblue"

#работа увлажнителя воздуха
def humidityDown(valve):
    if valve < 100 and valve > 0:
        valve -= 1
        humidity = Label(window, text=valve,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve)
        print (array_humidity)
    elif valve == 100:
        humidity = Label(window, text=valve - 1,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve - 1)
        print (array_humidity)
        return (valve)
    elif valve == 0:
        humidity = Label(window, text=valve + 1,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve+1)
        print (array_humidity)
        return (valve)
    else:
        return (valve)

def humidityUp(valve):
    if valve < 100 and valve > 0:
        valve += 1
        humidity = Label(window, text=valve,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve)
        print (array_humidity)
    elif valve == 100:
        humidity = Label(window, text=valve - 1,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve - 1)
        print (array_humidity)
        return (valve)
    elif valve == 0:
        humidity = Label(window, text=valve + 1,font=("Arial Bold", 20),  background = "lightblue")
        humidity.grid(column=0, row=1)
        window.update()
        array_humidity.append(valve+1)
        print (array_humidity)
        return (valve)
    else:
        return(valve)
    
#работа кондиционера\нагревателя
def tempDown(valve):
    if valve < 40 and valve > -10:
        valve -= 1
        state_vent = Label(window, text=valve,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve)
        print (array_temp)
    elif valve == 40:
        state_vent = Label(window, text=valve - 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve - 1)
        print (array_temp)
        return (valve)
    elif vavle == -10:
        state_vent = Label(window, text=valve + 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve + 1)
        print (array_temp)
        return (valve)
    else:
        return (valve)

def tempUp(valve):
    if valve < 40 and valve > -10:
        valve += 1
        state_vent = Label(window, text=valve,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve)
        print (array_temp)
    elif valve == 40:
        state_vent = Label(window, text=valve - 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve - 1)
        print (array_temp)
        return (valve)
    elif vavle == -10:
        state_vent = Label(window, text=valve + 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve + 1)
        print (array_temp)
        return (valve)
    else:
        return (valve)

def tempStandart(valve):
    if valve < 40 and valve > -10:
        valve -= 1
        state_vent = Label(window, text=valve,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve)
        print (array_temp)
    elif valve == 40:
        state_vent = Label(window, text=valve - 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve - 1)
        print (array_temp)
        return (valve)
    elif vavle == -10:
        state_vent = Label(window, text=valve + 1,font=("Arial Bold", 20),  background = "lightblue")
        state_vent.grid(column=3, row=1)
        window.update()
        array_temp.append(valve + 1)
        print (array_temp)
        return (valve)
    else:
        return (valve)
    
#совместная работа систем
def work_together():
    try:
        while option.get() == 0 and selected.get() == 0:
            tempStandart(array_temp.pop())
            time.sleep(7)
            humidityDown(array_humidity.pop())
            time.sleep(7)
        while option.get() == 1 and selected.get() == 0:
            tempDown(array_temp.pop())
            time.sleep(3)
            humidityDown(array_humidity.pop())
            time.sleep(7)
        while option.get() == 2 and selected.get() == 0:
            tempUp(array_temp.pop())
            time.sleep(3)
            humidityDown(array_humidity.pop())
            time.sleep(7)
        while option.get() == 0 and selected.get() == 1:
            tempStandart(array_temp.pop())
            tome.sleep(7)
            humidityUp(array_humidity.pop())
            time.sleep(3)
        while option.get() == 1 and selected.get() == 1:
            tempDown(array_temp.pop())
            time.sleep(3)
            humidityUp(array_humidity.pop())
            time.sleep(3)
        while option.get() == 2 and selected.get() == 1:
            tempUp(array_temp.pop())
            time.sleep(3)
            humidityUp(array_humidity.pop())
            time.sleep(3)
    except Exception as E:
        return (0)

#влажность воздуха в окне
name_humidity = Label(window, text="Влажность \n воздуха.",font=("Arial Bold", 25), fg="blue4",  background = "lightblue")
name_humidity.grid(column=0, row=0)

humidity = Label(window, text=now_humidity,font=("Arial Bold", 20),  background = "lightblue")
humidity.grid(column=0, row=1)

divice_humidity = Label(window, text="Увлажнитель воздуха.",font=("Arial Bold", 10),  background = "lightblue")
divice_humidity.grid(column=0, row=2)

selected = IntVar()

rad_h1 = Radiobutton(window,text='Включить', variable=selected, value=1,  background = "lightblue")
rad_h2 = Radiobutton(window,text='Выключить', variable=selected, value=0,  background = "lightblue")
rad_h1.grid(column=0, row=3)
rad_h2.grid(column=0, row=4)

#температура воздуха на окне
name_temp = Label(window, text="Температура \n воздуха",font=("Arial Bold", 25), fg="blue4",  background = "lightblue")
name_temp.grid(column=3, row=0)

temp = Label(window, text=now_temp,font=("Arial Bold", 20), background = "lightblue")
temp.grid(column=3, row=1)

option = IntVar()

rad_t1 = Radiobutton(window,text='Включить кондиционер', variable=option, value=1,  background = "lightblue")
rad_t1.grid(column=3, row=2)
rad_t2 = Radiobutton(window,text='Включить нагреватель', variable=option, value=2,  background = "lightblue")
rad_t2.grid(column=3, row=3)
rad_t3 = Radiobutton(window,text='Выключить систему', variable=option, value=0,  background = "lightblue")
rad_t3.grid(column=3, row=4)

btn1 = Button(window, text="Принять команду", command =lambda: [temp.grid_forget(), humidity.grid_forget(), work_together()])
btn1.grid(column=2, row=7)
btn2 = Button(window, text="Выход", command=lambda: [window.quit(), window.destroy()])
btn2.grid(column=2, row=8)

window.mainloop()
