# myweathersms
Weather Information App

# Summary
    Uses Openweathermap and sends an API request for current weather data. Compares the weather ID code to tell you the current days atmospheric 
    conditions via a sms text message

## Libraries/Modules
    -requests
    -from twilio.rest import Client


### Usage
    - In order to use this app for your own purposes, you will need to change a few items.

    -make_api_connection():
        -Change the parameters variable to match your current lat/long and your appid api key

 #### Design implementations
    - In order to work more with APIs I have decided to use this version to text via the Twilio app


