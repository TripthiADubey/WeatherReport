from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        api = "https://api.openweathermap.org/data/2.5/weather?q= "+city+"&APPID=8fbe8541addd441f586acce77e8c3ace"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)
        d.config(text=description)
    except Exception as e:
        messagebox.showerror("weather App", "Invalid Input")




Search_image = ImageTk.PhotoImage(Image.open('search.png'))
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)
textfield = tk.Entry(root, justify="center", width=17, font=("serif", 25), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = ImageTk.PhotoImage(Image.open('search_icon.png'))
icon = Button(image=Search_icon, borderwidth=0, bg="#404040", command=getWeather)
icon.place(x=400, y=32)

Logo = ImageTk.PhotoImage(Image.open('logo1.png'))
logo = Label(image=Logo, borderwidth=0)
logo.place(x=190, y=100)

Frame = ImageTk.PhotoImage(Image.open('box.png'))
frame = Label(image=Frame)
frame.pack(padx=5, pady=5, side=BOTTOM)

name = Label(root,font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root,font=("arial", 20))
clock.place(x=30, y=130)

#label1
label1 = Label(root, text="WIND", font=("sans-serif", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
#label2
label2 = Label(root, text="HUMIDITY", font=("sans-serif", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=230, y=400)
#label3
label3 = Label(root, text="PRESSURE", font=("sans-serif", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=400, y=400)
#label4
label4 = Label(root, text="DESCRIPTION", font=("sans-serif", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=600, y=400)

#temperature
t = Label(font=("sans-serif", 70, "bold"), fg="#ee666d")
t.place(x=500, y=150)

#condition
c = Label(font=("sans-serif", 15, "bold"))
c .place(x=500, y=250)

w = Label(text="...", font=("sans-serif", 20, "bold"), bg="#1ab5ef")
w.place(x=125, y=430)
h = Label(text="...", font=("sans-serif", 20, "bold"), bg="#1ab5ef")
h.place(x=240, y=430)
p = Label(text="...", font=("sans-serif", 20, "bold"), bg="#1ab5ef")
p.place(x=420, y=430)
d = Label(text="...", font=("sans-serif", 20, "bold"), bg="#1ab5ef")
d.place(x=620, y=430)

root.mainloop()
