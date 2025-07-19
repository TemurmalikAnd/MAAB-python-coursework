import requests

API_KEY = "86844e53063f89fdef6444648f418af4"
ROOT_URL = "https://api.openweathermap.org/data/2.5/weather?"


def get_weather_data(city_name):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    url = f"{ROOT_URL}appid={API_KEY}&q={city_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def kelvin_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return round(kelvin_temp - 273.15, 2)


def display_weather_info(city_name, data):
    """Display formatted weather information."""
    temp_kelvin = data['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description'].title()
    wind_speed = data['wind']['speed']

    print(f"\n--- Weather Information for {city_name.title()} ---")
    print(f"Weather Condition: {description}")
    print(f"Temperature: {temp_celsius}°C ({temp_kelvin} K)")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def main():
    """Main function to run the weather program."""
    print("This program gives your weather data for the city you search for")

    while True:
        city_name = input("\nEnter city name (or 'quit' to exit): ").strip()

        if city_name.lower() == 'quit':
            print("Thank you for using the weather app!")
            break

        if not city_name:
            print("Please enter a valid city name.")
            continue

        data = get_weather_data(city_name)

        if data is None:
            continue

        if data['cod'] == 200:
            display_weather_info(city_name, data)
        else:
            error_message = data.get('message', 'Unknown error')
            print(f"Error: {error_message}. Please try a different city.")


if __name__ == "__main__":
    main()