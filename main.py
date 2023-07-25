import telebot
from telebot import types

bot_token = '6344866429:AAH4afdEiLG7UYB06Eg7MjGZwcO2knW9Fwc'

bot = telebot.TeleBot(bot_token)




@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Хало, <b>{message.from_user.first_name}{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode= 'html')


@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_path = '112фы2.JPG'


    with open(photo_path, 'rb') as photo_file:
        bot.send_photo(message.chat.id, photo_file)
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text
    bot.reply_to(message, f"Ти написав: {text}. Це не є командою.")

@bot.message_handler(commands= ["web"])
def web(massage):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup("Вебсытк", url = "https://www.google.com/search?q=%D0%BA%D0%B0%D0%BA+%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%B0%D1%82%D1%8C+%D0%B3%D0%B8%D1%82+%D0%BA+%D0%BF%D0%B0%D0%B9+%D1%87%D0%B0%D1%80%D0%BC%D1%83&client=firefox-b-d&biw=1920&bih=965&sxsrf=AB5stBjKr0qgliH-DQSifv4tUXuSQl-B-w%3A1690314157876&ei=rSXAZNyBNaK-wPAPpqyRwAk&ved=0ahUKEwicjMH3zqqAAxUiHxAIHSZWBJgQ4dUDCA4&uact=5&oq=%D0%BA%D0%B0%D0%BA+%D0%BF%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%B0%D1%82%D1%8C+%D0%B3%D0%B8%D1%82+%D0%BA+%D0%BF%D0%B0%D0%B9+%D1%87%D0%B0%D1%80%D0%BC%D1%83&gs_lp=Egxnd3Mtd2l6LXNlcnAiNdC60LDQuiDQv9GA0LjQstGP0LfQsNGC0Ywg0LPQuNGCINC6INC_0LDQuSDRh9Cw0YDQvNGDMgUQABiiBDIFEAAYogQyBRAAGKIEMgUQABiiBDIFEAAYogRIkg5Q1AJYmwhwAXgBkAEAmAGCAaAB2AKqAQMwLjO4AQPIAQD4AQHCAgoQABhHGNYEGLAD4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp#fpstate=ive&vld=cid:8163f65b,vid:1xkWYCJaBAU"))

    bot.send_message(massage.chat.id, 'Isao', reply_markup=markup)


bot.polling(none_stop= True)
