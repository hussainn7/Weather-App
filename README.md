# Weather and Air Quality Monitoring Software
### 🌦️ Features
### 📈 Real-Time Weather Data
- Current Temperature: Displays the current temperature in Celsius for the specified city.
- Humidity Levels: Shows the current humidity percentage.
- Weather Description: Provides a brief description of the current weather conditions.
### 🌍 Air Quality Monitoring
- PM2.5 Concentration: Fetches and displays the current PM2.5 concentration.
- AQI Calculation: Calculates and categorizes the Air Quality Index (AQI) based on PM2.5 levels.
### 🕒 Local Time Display
- Real-Time Clock: Shows the current local time and updates every second.
### 🖼️ User-Friendly Interface
- Intuitive GUI: Easy-to-use graphical interface with clearly labeled sections.
- Custom Fonts and Styling: Uses attractive fonts and colors to enhance readability.
## 🛠️ How to Use
**1. Install Required Libraries:**

    pip install requests
    
**2. Download and Prepare Assets:**
- Place your background image in the assets/frame0/ directory.
- Ensure the image file is named image_1.png.

**3. Update API Keys and City Name:**
- Replace "CITY-NAME" with the desired city in the fetch_weather_data function.
- Replace "YOUR_API_WEATHER" with your actual OpenWeatherMap API key.

**4. Run the Application:**
  
    python your_script.py

# 🔧 Requirements
- Python 3.x
- tkinter
- requests
