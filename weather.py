from tkinter import Tk, Canvas, Text, PhotoImage, font
from pathlib import Path
import requests
from datetime import datetime

# Function to fetch weather data
def fetch_weather_data(city_name="bishkek", api_key="b9cd298593ba9f5db898d737ff3107bd"):
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(weather_url)
    weather_info = response.json()

    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        humidity = weather_info['main']['humidity']
        description = weather_info['weather'][0]['description']
        return temp, humidity, description.capitalize()
    else:
        return None, None, "Weather data not found!"

# Function to fetch air pollution data
# Function to fetch air pollution data
def fetch_air_pollution_data(lat=42.8746, lon=74.5698, api_key="b9cd298593ba9f5db898d737ff3107bd"):
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("list"):
        pm25_concentration = data["list"][0]["components"]["pm2_5"]
        return round(pm25_concentration)  # Ensure the return value is a float
    else:
        return 0.0

# Function to calculate AQI from PM2.5 - make sure to handle cases where data might not be available
def calculate_aqi_pm25(concentration):
    try:
        concentration = float(concentration)  # Ensure concentration is treated as a float
    except ValueError:
        return "Invalid data for AQI calculation"

    if concentration <= 12:
        return "Poor"
    elif concentration <= 35.4:
        return "Moderate"
    elif concentration <= 55.4:
        return "Unhealthy for Sensitive Groups"
    else:
        return "Unhealthy"


# GUI setup
window = Tk()
window.geometry("800x480")

canvas = Canvas(window, height=480, width=800, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Load and display the background image
ASSETS_PATH = Path(r"assets\frame0")
background_image = PhotoImage(file=ASSETS_PATH / "image_1.png")
canvas.create_image(400, 240, image=background_image)  # Assuming 800x480 is the size of your image

customFont = ("Open Sans", 35, "bold")  # Example: Arial, 12pt, bold

entry_1 = Text(window, bd=0, bg="light gray", fg="#000716", highlightthickness=0, font=customFont)
entry_1.place(x=50.0, y=50.0, width=300.0, height=168.0)

entry_2 = Text(window, bd=0, bg="light gray", fg="#000716", highlightthickness=0, font=customFont)
entry_2.place(x=438.0, y=50.0, width=300.0, height=168.0)

entry_3 = Text(window, bd=0, bg="light gray", fg="#000716", highlightthickness=0, font=customFont)
entry_3.place(x=50.0, y=275.0, width=300.0, height=168.0)

entry_4 = Text(window, bd=0, bg="light gray", fg="#000716", highlightthickness=0, font=customFont)
entry_4.place(x=438.0, y=275.0, width=300.0, height=168.0)

entry_time = Text(window, bd=0, bg="light gray", fg="#000716", highlightthickness=0, font=customFont)
entry_time.place(x=50.0, y=50.0, width=300.0, height=168.0)


def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    entry_time.delete("1.0", "end")  # Clear the previous time
    entry_time.insert("end", f"Local Time: \n{current_time}")  # Insert the current time
    window.after(1000, update_time)


def update_gui():
    temp, humidity, weather_description = fetch_weather_data()
    pm25 = fetch_air_pollution_data()
    aqi_description = calculate_aqi_pm25(pm25)

    entry_1.delete("1.0", "end")
    entry_1.insert("end", f"{update_time()}")

    entry_2.delete("1.0", "end")
    entry_2.insert("end", f"Temperature \n{temp}°C")

    entry_3.delete("1.0", "end")
    entry_3.insert("end", f"Humidity \n{humidity}%")

    entry_4.delete("1.0", "end")
    entry_4.insert("end", f"Air Quality \n{aqi_description} AQ 165")

update_gui()

window.resizable(False, False)
window.mainloop()
