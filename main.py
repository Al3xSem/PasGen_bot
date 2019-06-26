import telebot

import Functions

token = '839979302:AAH73Vl5xval9DpLALGZvIo6yGZ2qlYLr44'

bot = telebot.TeleBot(token)

# Стандартная команда "start"

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/begin', '/help', '/hide')
    bot.send_message(message.from_user.id, "Для создания новой формы выберите команду /begin \n\nЕсли у Вас остались вопросы по использованию бота, выберите команду /help", reply_markup=user_markup)

# Алгоритм работы бота
# При выполнении команды "begin"

@bot.message_handler(commands=['begin'])
def handle_text(message):
    bot.send_message(message.chat.id, "Введите название ресурса и логин через пробел")

    @bot.message_handler(content_types=['text'])
    def handle_text(message):

        t = message.text

        resource_name = "Ресурс:   " + Functions.output(t)[0]
        user_login = "Логин:    " + Functions.output(t)[1]
        new_pas = "Пароль:   " + Functions.password()

        bot.send_message(message.chat.id, "Your new form")
        bot.send_message(message.chat.id, resource_name)
        bot.send_message(message.chat.id, user_login)
        bot.send_message(message.chat.id, new_pas)
        bot.send_message(message.chat.id, "Убедиться в надежности сгенерированного пароля Вы можете на сайте Касперского: https://password.kaspersky.com/ru/")
        bot.send_message(message.chat.id, "Для создания новой формы выберите команду /begin \n\nЕсли у Вас остались вопросы по использованию бота, выберите команду /help \n\n Если Вы спрятали клавиатуру, но хотите ее вернуть, выберите команду /start")



# Содержание команды "help"

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Подробное описание команд, используемых в боте:\n/start - вызывает клавиатуру и позволяет начать взаимодействие с ботом, выбрать нужную команду\n/begin - генерирует пароль и создает форму для его хранения\n")
    bot.send_message(message.chat.id, "/help - описывает ошибки, с которыми может столкнуться пользователь и как их можно избежать\n/hide - скрывает клавиатуру, в дальнейшем Вы сможете ее вернуть, если она Вам понадобится, повторным вводом команды /start\n")
    bot.send_message(message.chat.id, "Возможные ошибки при работе бота:\nПосле выбора команды /begin введите логин и пароль через пробел\nПример:   ресурс: Lostfilm логин: Al3x1893\nСоответственно ввести данные нужно следующим образом: Lostfilm Al3x1893\n")
    bot.send_message(message.chat.id, "Если Вы столкнулись с другими ошибками, присылайте их на аккаунт @Rehor\nОни будут исправлены в ближайшее время\n")



# Содержание команды "hide", убирающей клавиатуру

@bot.message_handler(commands=['hide'])
def handle_text(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "the keyboard has been hidden\n\n If you need keyboard, write the command /start", reply_markup=hide_markup)

bot.polling(none_stop=True, interval=0)
