import telebot

bot = telebot.TeleBot('') 

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Какой Баланс:")
    
user_data = {}

@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if 'num1' not in user_data:
        user_data['num1'] = float(message.text)
        bot.send_message(message.chat.id, "Какой коэффициент:")
        
    elif 'num2' not in user_data:
        user_data['num2'] = float(message.text)
        bot.send_message(message.chat.id, "Сколько % от баланса хочешь выигрывать:")
        
    elif 'num3' not in user_data:
        user_data['num3'] = float(message.text)
        bot.send_message(message.chat.id, "Сколько нужно отыграть:")

    elif 'num4' not in user_data:
        user_data['num4'] = float(message.text)

        
        num1 = user_data['num1']
        num2 = user_data['num2'] 
        num3 = user_data['num3']
        num4 = user_data['num4']
        
        percent = (num1 / 100) * num3
        sum = (percent + num4) / (num2 - 1)
        
        bot.send_message(message.chat.id, f"Ставь: {sum}")
        user_data.clear()
        
bot.polling()

