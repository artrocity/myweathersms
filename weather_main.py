# Import libraries
import requests


def main():
    weather_data = make_api_connection()
    if weather_data:
        weather_id = get_current_weather(weather_data)
        check_weather(weather_id)


def make_api_connection() -> list[dict]:
    """
    Summary:
        Attempts to obtain the openweathermap API data for current weather
    Returns:
        list[dict]: JSON data of current weather
    Called By:
        weather_data in main() function
    """
    # Set API parameters
    parameters = {
        "lat" : "insert your value here",
        "lon" : "insert your value here",
        "appid" : "insert your value here"
    }

    # Attempt to obtain API
    try:
        weather_response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
        weather_response.raise_for_status()
        # Store weather API data via JSON
        return weather_response.json()
    except requests.exceptions.RequestException as e:
        print("Unable to obtain the API, error: ", str(e))
        return None


def get_current_weather(weather:list[dict]) -> int:
    """
    Summary:
        Takes the argument weather and extracts the weather ID from the list of dictionaries
    Args:
        weather (list[dict]): A list of dictionaries containing all pertinent data for the current weather
    Returns:
        int: The weather "id", which directly correlates to the atmospheric conditions
    Called by:
        weather_id in main() function
    """
    weather_id = weather["weather"][0]["id"]
    return weather_id


def check_weather(weather_id:int) -> None:
    """
    Summary:
        Takes an int as input and compares it vs known Openweathermap Weather Codes 
        to alert you to current weather conditions
    Args:
        weather_id (int): Takes an ID code as an argument
    Returns:
        None: Prints a statement
    Called by:
        main()
    """
    if 200 <= weather_id <= 600:
        print("It's going to rain, bring an umbrella")
    elif 600 <= weather_id <= 700:
        print("It's going to snow, dress warm")
    elif weather_id == 800:
        print("It's going to be a clear day! Enjoy the sun.")
    elif weather_id > 800:
        print("It's going to be cloudy outside")


if __name__ == "__main__":
    main()
