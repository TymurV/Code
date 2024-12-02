import telebot
bot = telebot.TeleBot('7547295693:AAFei7d0jrUa8Nky_wXtO65seKphkjPqt5g')
@bot.message_handler(commands=['start', 'hi'])
def hi(message):

    bot.reply_to(message, 'Hi!\nMessage /find "rectangle" or "circle" and body measurements')

@bot.message_handler(commands= ['find'])
def find_area(message):
    args = message.text.split()[1:]
    print(args)

    if len(args) < 2:
        bot.reply_to(message, 'few arguments')
        return

    figure_name = args[0].lower()
    if figure_name == 'rectangle':
        if len(args) != 3:
            bot.reply_to(message, 'the figure "rectangle" needs two sides')
            return
        rectangular_area = float(args[1]) * float(args[2])
        bot.reply_to(message, f'The area of a rectangle is: {rectangular_area}')

    elif figure_name == 'circle':
        if len(args) != 2:
            bot.reply_to(message, 'incorrect number of parameters for the figure is entered "circle"')
            return
        Circle_area = float(args[1]) / 2
        bot.reply_to(message, f'The radius of the circle is: {Circle_area}')

    else:
        bot.reply_to(message, 'Incorrect figure name')
        return

bot.infinity_polling()