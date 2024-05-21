import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "0bf27c03971f12b13a42f17b2d84dd62"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather_desc}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

# Create main window
root = tk.Tk()
root.title("Weather App")

# Labels and Entry fields
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

# Start GUI main loop
root.mainloop()
