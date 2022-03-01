import bs4
import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5176514754:AAHx4jWsOtLAacgQ6C5-T9D6FHe1y6wnwEo')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("!Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "!Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":

        contents = requests.get('https://random.dog/woof.json').json()
        urLDOG = contents['url']
        bot.send_photo(chat_id, photo=urLDOG, caption="Вот и пёс")

    elif ms_text == "Прислать анекдот":
        bot.send_message(chat_id, text=get_anekdot())


    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="ещё не готово")

    elif ms_text == "Управелние":
        bot.send_message(chat_id, text="ещё не готово")

    elif ms_text == "Помощь" or ms_text == "/help":

        bot.send_message(chat_id, "Автор: Манских Богдан")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="id1")
        key1.add(btn1)
        img = open('Манских Богдан.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:


        bot.send_message(chat_id, text="я слышу, сообщение:"+ ms_text)

# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
