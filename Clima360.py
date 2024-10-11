import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime, timedelta, timezone
from PIL import Image, ImageTk

# Carregar as variáveis do arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY") 
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_weather_data(city):
    weather_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    
    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        return weather_response.json(), forecast_response.json()
    else:
        return None, None

def update_weather():
    city = city_entry.get()
    weather_data, forecast_data = get_weather_data(city)
    
    if not weather_data:
        messagebox.showerror("Erro", "Não foi possível obter os dados do clima.")
        return

    temperature = round(weather_data['main']['temp'])
    condition = weather_data['weather'][0]['description'].capitalize()
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    timezone_offset = weather_data['timezone']
    current_utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    local_time = current_utc_time + timedelta(seconds=timezone_offset)
    local_time_str = local_time.strftime('%Y-%m-%d %H:%M:%S')
    
    hour = local_time.hour

    if 6 <= hour < 18:
        root.configure(bg='lightblue')
        text_color = 'black'
    else:
        root.configure(bg='#2c3e50')
        text_color = 'white'

    temp_label.config(text=f"{temperature}°C", fg=text_color, bg=root.cget('bg'))
    condition_label.config(text=condition, fg=text_color, bg=root.cget('bg'))
    local_time_label.config(text=f"Última atualização: {local_time_str}", fg=text_color, bg=root.cget('bg'))

    icon_response = requests.get(icon_url, stream=True)
    if icon_response.status_code == 200:
        try:
            image = Image.open(icon_response.raw)
            icon_image = ImageTk.PhotoImage(image)
            icon_label.config(image=icon_image, bg=root.cget('bg'))
            icon_label.image = icon_image
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o ícone: {e}")
    
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    pressure = weather_data['main']['pressure']
    info_label.config(text=f"Umidade: {humidity}% | Vento: {wind_speed} m/s | Pressão: {pressure} hPa", fg=text_color, bg=root.cget('bg'))
    
    forecast_text = ""
    for entry in forecast_data['list'][:5]:
        utc_time = datetime.utcfromtimestamp(entry['dt']).replace(tzinfo=timezone.utc)
        local_forecast_time = utc_time + timedelta(seconds=timezone_offset)
        local_forecast_time_str = local_forecast_time.strftime('%Y-%m-%d %H:%M')
        temp_forecast = round(entry['main']['temp'])
        condition_forecast = entry['weather'][0]['description'].capitalize()
        forecast_text += f"{local_forecast_time_str}: {temp_forecast}°C, {condition_forecast}\n"
    
    forecast_label.config(text=forecast_text, fg=text_color, bg=root.cget('bg'))
    city_entry.delete(0, tk.END)

def on_enter(event):
    update_weather()

root = tk.Tk()
root.title("Clima 360")
root.configure(bg='#03396c')
root.geometry("400x600")

city_entry = tk.Entry(root, font=("Helvetica", 16))
city_entry.pack(pady=10)
city_entry.bind("<Return>", on_enter)

search_button = tk.Button(root, text="Buscar Clima", command=update_weather, font=("Helvetica", 14))
search_button.pack(pady=10)

icon_label = tk.Label(root, bg='#03396c')
icon_label.pack(pady=10)

temp_label = tk.Label(root, font=("Helvetica", 32), bg='#03396c')
temp_label.pack()

condition_label = tk.Label(root, font=("Helvetica", 16), bg='#03396c')
condition_label.pack()

local_time_label = tk.Label(root, font=("Helvetica", 10), bg='#03396c')
local_time_label.pack(pady=5)

info_label = tk.Label(root, font=("Helvetica", 12), bg='#03396c')
info_label.pack(pady=5)

forecast_label = tk.Label(root, font=("Helvetica", 10), bg='#03396c', justify="left")
forecast_label.pack(pady=10)

root.mainloop()


