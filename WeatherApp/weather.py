from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


# API
def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")


# Weather
api = 'https://api.openweathermap.org/data/2.5/weather?q= + city + &appid=9b4997813c1177390454c54d3a612e09'

json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
description = json_data['weather'][0]['description']
temp = int(json_data['main']['temp'] - 273.15)
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['main']['wind']

t.config(text=(temp, "°"))
c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

w.config(text=wind)
h.config(text=humidity)
p.config(text=pressure)
d.config(text=description)

# Search Box
Search_image = PhotoImage(file="Search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("times new roman", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("ariel", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label
label1 = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=140, y=400)

label2 = Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=310, y=400)

label3 = Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=505, y=400)

label4 = Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=700, y=400)

t = Label(font=("ariel", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("ariel", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("ariel", 20, "bold"), bg="#1ab5ef")
w.place(x=145, y=430)
h = Label(text="...", font=("ariel", 20, "bold"), bg="#1ab5ef")
h.place(x=330, y=430)
d = Label(text="...", font=("ariel", 20, "bold"), bg="#1ab5ef")
d.place(x=535, y=430)
p = Label(text="...", font=("ariel", 20, "bold"), bg="#1ab5ef")
p.place(x=725, y=430)

root.mainloop()
