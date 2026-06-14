import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        weather = data["current_condition"][0]["weatherDesc"][0]["value"]

        print("\n===== Weather Report =====")
        print("City:", city.title())
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

    else:
        print("Unable to fetch weather data.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
except KeyError:
    print("Unexpected data received from the API.")