import telebot

bot = telebot.TeleBot('7500587370:AAHjIZoNfSnyXAsuW2rNN2Te6541aX2SNS8')

tasks = {}
@bot.message_handler(commands=['add'])
def add_task(message):
    bot.send_message(message.chat.id, 'Enter task')
    bot.register_next_step_handler(message, save_task)

def save_task(message):
    task = message.text
    print(task)
    user_id = message.chat.id
    if user_id not in tasks:
        tasks[user_id] = []
    tasks[user_id].append(task)
    bot.send_message(user_id, f'The task “{task}” has been added')

@bot.message_handler(commands=['show'])
def show_tasks(message):
    user_id=message.chat.id

    if user_id in tasks and tasks[user_id]:
        text = '\n'.join(tasks[user_id])
        bot.send_message(user_id, f'All tasks: \n{text}')
    else:
        bot.send_message(user_id, 'Tasks not found')



@bot.message_handler(commands=['clear'])
def clear_tasks(message):
    user_id=message.chat.id
    tasks[user_id] = []
    bot.send_message(user_id, f'Tasks deleted')
    


bot.polling()