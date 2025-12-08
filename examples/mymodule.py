# mymodule.py

import requests


def f():
    """Example function that returns a string."""
    return "This is f"


# def g():
#     """Example function that is not yet implemented."""
#     pass


def pyt(a: float, b: float) -> float:
    """Calculate the length of the hypotenuse of a right triangle."""
    return (a**2 + b**2) ** 0.5


def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def get_yr_weather_temperature(lat: float, lon: float) -> float:
    """Fetch weather data for a given location from the Yr API."""
    base_url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    url = f"{base_url}?lat={lat}&lon={lon}"
    headers = {"Accept": "application/json", "User-Agent": "mymodule-example/1.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    temperature = response.json()["properties"]["timeseries"][0]["data"]["instant"][
        "details"
    ]["air_temperature"]
    return temperature


if __name__ == "__main__":
    print(get_yr_weather_temperature(lat=55.68888, lon=12.5))
