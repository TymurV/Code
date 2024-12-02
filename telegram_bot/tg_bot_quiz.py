import telebot
from telebot import types

bot = telebot.TeleBot('7500587370:AAHjIZoNfSnyXAsuW2rNN2Te6541aX2SNS8')

questions = [
    {
        'question': 'How much is 2+2', 
        'options': ['4', '2', '10', '3'],
        'correct_answer': 0
    },
    {
        'question': 'What language this code is written in',
        'options': ['HTML', 'C++', 'Python', 'Java'],
        'correct_answer': 2
    },
    {
        'question': 'What is the weather like right now',
        'options': ['1', '10', '4', '-1'],
        'correct_answer': 1
    }
]


results = {}
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    results[chat_id] = {'correct': 0, 'current_question': 0}
    send_question(chat_id)


def send_question(chat_id):
    question_index = results[chat_id]['current_question']
    print(question_index)
    if question_index < len(questions):
        question = questions[question_index]['question']
        options = questions[question_index]['options']

        inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
        for index, option in enumerate(options):
            button = types.InlineKeyboardButton(
                option, callback_data=str(index))
            inline_keyboard.add(button)
        bot.send_message(chat_id, question, reply_markup=inline_keyboard)
    else:
        show_results(chat_id)


def show_results(chat_id):
    bot.send_message(chat_id, f'You answered {results[chat_id]['correct']}/{len(questions)} questions correctly')
    del results[chat_id]

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    chat_id = call.message.chat.id
    user_answer = int(call.data)
    #print(user_answer)

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=None)

    question_index = results[chat_id]['current_question']
    correct_answer = questions[question_index]['correct_answer']

    if user_answer == correct_answer:
        results[chat_id]['correct'] += 1
    print(results)
    results[chat_id]['current_question'] += 1
    send_question(chat_id)




bot.polling()