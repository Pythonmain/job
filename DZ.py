
# -----------------------------------------------------------------------
import requests


def dz1(bot, chat_id):
    # car = get_car()
    bot.send_photo(chat_id, photo=get_car(), caption="Вот тебе собачка!")
    # bot.send_message(chat_id, text=str(car))
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, text="как дела?")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz5_ResponseHandler)

def dz5_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)

def get_car():
    url = ''
    req = requests.get('https://www.1zoom.ru/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8/t2/1/')
    if req.status_code == 200:
        r_json = req.json()
        url = r_json['url']
    return url