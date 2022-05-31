import speech_recognition as sr  # SpeechRecognition 3.8.1
import threading
from datetime import datetime


# -----------------------------------------------------------------------
def getAudioFromURL(URL):
    from urllib.request import urlopen

    data = urlopen(URL).read()
    return data


# -----------------------------------------------------------------------
def getTextFromVoice(audioData):
    import tempfile
    from pydub import AudioSegment

    with tempfile.NamedTemporaryFile() as temp_ogg:
        with tempfile.NamedTemporaryFile() as temp_wav:
            temp_ogg.write(audioData)
            temp_ogg.seek(0)
            try:
                AudioSegment.from_file_using_temporary_files(temp_ogg, 'ogg').export(temp_wav, format='wav')
            except FileNotFoundError as e:
                print("Установите и проверьте работоспособность библиотеки ffmpeg!")
                return "Установите и проверьте работоспособность библиотеки ffmpeg!"

            r = sr.Recognizer()
            # with sr.Microphone(device_index=2) as source:
            with sr.AudioFile(temp_wav) as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language='ru-RU').lower()
                    return query
                except Exception as e:
                    return "Ошибка распознавания:\n" + str(e)


# -----------------------------------------------------------------------
def say_text(msg, file=None):
    import pyttsx3

    tts = pyttsx3.init()
    tts.setProperty('voice', 'ru')
    tts.setProperty('rate', 180)
    tts.setProperty('volume', 1)

    if file is None:
        tts.say(msg)
        tts.runAndWait()
    else:
        tts.save_to_file(msg, file)
        tts.runAndWait()


# -----------------------------------------------------------------------
def say_time(time=None, file=None):
    from pytils import numeral

    time = datetime.now() if time is None else time
    txt_hour = numeral.get_plural(time.hour, "час, часа, часов")
    txt_minute = "%s %s" % (numeral.in_words_int(time.minute, numeral.FEMALE), numeral.choose_plural(time.minute, "минута, минуты, минут"))

    if time.second > 0:
        txt_second = "%s %s" % (numeral.in_words_int(time.second, numeral.FEMALE), numeral.choose_plural(time.second, "секунда, секунды, секунд"))
        txt_to_speach = f"{txt_hour} {txt_minute} {txt_second}"
    elif time.minute == 0:
        txt_to_speach = f"{txt_hour} ровно"
    else:
        txt_to_speach = f"{txt_hour} {txt_minute}"

    say_text(txt_to_speach, file)


# -----------------------------------------------------------------------
def timer(interval, func, argsFunc=[], start=None, stop=None):


    # запустим выполнение в отдельном потоке
    objTimer = threading.Timer(0, func, args=argsFunc)
    objTimer.start()


    now = datetime.now()
    ms = (now.hour * 60 * 60 + now.second) * 1000000 + now.microsecond
    d = interval * 1000000
    delay = (d - (ms - (ms // d) * d)) / 1000000

    objTimer = threading.Timer(delay, timer, args=[interval, func])
    objTimer.start()

# -----------------------------------------------------------------------
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    # ======================================= реализация игры в 21
    if ms_text == "Текущее время":
        name_audio = 'Текущее время.ogg'
        # say_time(file=name_audio)
        # with open(name_audio, 'rb') as audio:
            # temp_wav.seek(0)
            # size = len(temp_wav.read())
            # bot.send_chat_action(message.from_user.id, 'upload_audio')
            # bot.send_audio(chat_id, audio)



# -----------------------------------------------------------------------
# для отладки работы модуля, запуск таймера с вызовом голосового синтезатора текущего времени
# запустим таймер, синхронизация секунд произойдёт в первом вызове
if __name__ == "__main__":
    timer(interval=60, func=say_time)
    # say_time(datetime(2022, 5, 5, 3, 4, 5, 0))  # для отладки