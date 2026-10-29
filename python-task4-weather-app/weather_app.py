
import requests

API_KEY = "94556d2ad52366e2e69c2b3ae59e0632"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("Error: City not found. Check the city name.")
            return

        if response.status_code == 401:
           print("API error details:", response.text)
           return 

        response.raise_for_status()
        data = response.json()

        print("\n===== WEATHER REPORT =====")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(
            "Condition:",
            data["weather"][0]["description"].title()
        )

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")

    except requests.exceptions.RequestException:
        print("Error: Unable to retrieve weather information.")

    except (KeyError, TypeError, ValueError):
        print("Error: Unexpected weather data received.")


def main():
    print("===== BASIC WEATHER APP =====")

    if API_KEY == "a91c16ba5882b633d940657ff0946129":
        print("Please add your OpenWeatherMap API key first.")
        return

    city = input("Enter a city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
