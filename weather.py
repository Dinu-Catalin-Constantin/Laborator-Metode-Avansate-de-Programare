from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import json
import tkinter as tk

class Main(tk.Tk):

        def __init__(self):
            tk.Tk.__init__(self)
            self.title("The Weather")
            self.geometry("400x300")
            self.config(bg="#1f1e1e")

            self.title_label = Label(self, text="The Weather", bg="#1f1e1e", fg="white", font=("Tahoma", 20), relief="sunken")
            self.title_label.place(x=200, y=35, anchor="center")

            self.city_label = Label(self, text="Enter the city here: ", bg="#1f1e1e", fg="white", font=("Arial", 15))
            self.city_label.place(x=200, y=80, anchor="center")

            self.city_entry = Entry(self)
            self.city_entry.config(width=15, font=("Calibri", 14), justify='center')
            self.city_entry.place(x=200, y=110, anchor="center")

            self.weather_details_label = Label(self, text="Weather details: ", bg="#1f1e1e", fg="white", font=("Arial", 15))
            self.weather_details_label.place(x=200, y=200, anchor="center")

            self.weather_button = Button(self, text="Check weather", bg="white", fg="black", font=("Arial", 12), command=self.ReadWeather)
            self.weather_button.place(x=200, y=150, anchor="center", height=25)

            self.weather_result = Label(self, text='', bg="#1f1e1e", fg="white", font=("Arial", 15), justify='center')
            self.weather_result.place(x=200, y=220, anchor="center", width=300, height=80)
            

        def ReadWeather(self):

            API_KEY = "11cef3f9331406e51eeb5b055b07919b"
            BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
            city = str(self.city_entry.get())
            request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
            rasp = requests.get(request_url)
            data = json.loads(rasp.text)
            if rasp.status_code == 200:
                data = rasp.json()
                vremea = data["weather"][0]["description"]
                temp = round(data["main"]["temp"] -273.15, 2)
                vant_viteza = data["wind"]["speed"]
                vant_unghi = data["wind"]["deg"]
                self.weather_result.config(text=f"Weather = {vremea}\nTemperature = {temp}°C\nWind = {vant_viteza} m/s & {vant_unghi}°")
            else:
                self.weather_result.config(text="Error, incorrect city entered")

if __name__ == "__main__":
    Main()
    mainloop()