
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Задание-1":
        dz1(bot, chat_id)

    elif ms_text == "Задание-2":
        dz2(bot, chat_id)

    elif ms_text == "Задание-3":
        dz3(bot, chat_id)

    elif ms_text == "Задание-4":
        dz4(bot, chat_id)

    elif ms_text == "Задание-5":
        dz5(bot, chat_id)

    elif ms_text == "Задание-6":
        dz6(bot, chat_id)

# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    my_name, my_age = "Богдан", 19
    my_name_X5 = (my_name + " ") * 5
    bot.send_message(chat_id, "Имя: %s, Возраст %s, \nИмя повторённое 5 раз: %s" % (my_name, my_age, my_name_X5))
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    age_answer = lambda message, joke: bot.send_message(chat_id,f"{joke} {message.text}? \nТянешь на все {round(int(message.text) / 2)}!")
    age_check = lambda message: age_answer(message, "Целых") if (int(correct_age(bot, chat_id, message.text)) <= 18) else age_answer(message, "Всего")
    qwerty = lambda message: my_input(bot, chat_id,f"Привет, {correct_name (bot, chat_id, message.text)}  \nСколько тебе лет?",age_check)
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)
# -----------------------------------------------------------------------

def dz3(bot, chat_id):
    qwerty = lambda message: bot.send_message(chat_id, "{}\n{}\n{}\n{}".format(message.text[1:-1], message.text[::-1],message.text[-3:], message.text[:5]))
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    qwerty = lambda message: bot.send_message(chat_id,f"В твоём имени {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)


# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    mult = lambda x: int(x[0]) * int(x[1])
    addit = lambda x: int(x[0]) + int(x[1])
    age_ans = lambda message: bot.send_message(chat_id,"Произведение цифр твоего возраста: {}\nСумма цифр твоего вораста: {}".format(mult(message.text), addit(message.text)))
    my_input(bot, chat_id, "Сколько тебе лет?", age_ans)

def dz5_ResponseHandler(bot, chat_id, age_int):
    qwerty = lambda message: bot.send_message(chat_id,
    "{}\n{}\n{}\n{}".format(message.text.upper(), message.text.lower(),
    message.text.capitalize(),
    message.text[0].lower() + message.text[1:].upper()))
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    proc_answer = lambda message: bot.send_message(chat_id, "Абсолютно точно верно, да, да, ты угадал!") if (message.text == "1") else bot.send_message(chat_id, "Нет, хах")
    my_input(bot, chat_id, "Чему равен натуральный логарифм числа \"e\"? ", proc_answer)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):



    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)


def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)

        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
