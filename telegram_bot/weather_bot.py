import telebot
import requests
bot = telebot.TeleBot('7586880240:AAEkvuyFXft-UVtRETl8qCIkPeXhd4IVeRs')
api_key = '27cb877c67d640890c532148547f5cf1'
@bot.message_handler(commands=['start', 'hi'])
def hi(message):

    bot.reply_to(message, 'Hi!\nMessage /find_weath "city name" and you will get the weather in the city you entered.')

@bot.message_handler(commands=['find_weath'])
def find_weather(message):
    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, 'Enter city name: ')
        return
    
    city_name = args[0].strip().lower()
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    #http://api.openweathermap.org/data/2.5/weather?q=london&appid=27cb877c67d640890c532148547f5cf1&units=metric
    try:
        response = requests.get(URL)
        data = response.json()
        if data['cod'] == '404':
            bot.reply_to(message, 'Enter an existing city')
        else:
            print(data)
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            weather_info = f'Weather in {city_name}:\Description: {description}\nWind sped: {wind_speed}\Temperature: {temp}\Humidity: {humidity}'
            bot.reply_to(message, weather_info)
    except Exception as e:
        bot.reply_to(message, 'Server malfunctions')


bot.infinity_polling()