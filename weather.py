import requests

city = input("Enter city name: ")

url = (
    "https://api.openweathermap.org/data/2.5/weather?&appid=bbbb876ef25804a91d2cb9aa35496dd7&q="
    + city
)

try:
    data = requests.get(url).json()

    print(
        f"{data["name"]}, {data["sys"]["country"]} \nWind Speed: {data["wind"]["speed"]}m/s\nWeather: {data["weather"][0]["description"]}\n"
    )

    print("__________________________________________\n")
    print(
        f"Temprature: {data["main"]['temp'] - 273.15:.2f}C\nFeels like: {data["main"]['feels_like'] - 273.15:.2f}C\nMinimum temprature: {data["main"]['temp_min'] - 273.15:.2f}C\nMaximum temprature: {data["main"]['temp_max'] - 273.15:.2f}C"
    )

except Exception as e:
    print(f"City not found!  {e}")
