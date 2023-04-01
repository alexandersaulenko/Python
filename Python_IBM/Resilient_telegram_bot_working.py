import telebot #Подключили библиотеку Телебот - для работы с Телеграм
from telebot import types #Подключили дополнения
import config
import os
import datetime

 
bot = telebot.TeleBot(config.token_bot) #bot token in the config.py file 
 
@bot.message_handler(commands=['start'])
def start_menu(message):
    message_text = 'Здравствуйте!\n' \
                    + 'Для авторизации необходимо проверить Ваш номер телефона. Пожалуйста предоставьте данные нажав на кнопку "Отправить номер телефона"'
    message_text_eng = 'Hello ! \n' + 'To authorise you we need to check your phone number, Please share it by pressing the button bellow' 
    bot.send_message(message.chat.id, message_text_eng)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру | Attaching keyboard to the message
    button_phone = types.KeyboardButton(text="Отправить номер телефона | Send phone number", request_contact=True) #Указываем название кнопки, которая появится у пользователя | Name for the button
    keyboard.add(button_phone) #Добавляем эту кнопку | adding the button
    bot.send_message(message.chat.id, "Нажав на кнопку 'Отправить номер телефона' Вы сообщите его для проверки в списке авторизованных пользователей | By pressing the button you are providing us your phone number details", reply_markup=keyboard) #Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)
    print("chat id is:",message.chat.id)



@bot.message_handler(content_types=['contact']) #Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :) 
def contact(message):
    if message.contact is not None: #Если присланный объект <strong>contact</strong> не равен нулю
        if not os.path.exists('contacts.txt'):
            with open('contacts.txt', 'w'):
                pass
        with open('contacts.txt', 'a+') as file_object:
            file_object.seek(0) # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(str(message.from_user.first_name)+" "+str(message.from_user.last_name)+" " +str(message.from_user.id)+" "+str(message.contact.phone_number)+" "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Спасибо за предоставленный номер телефона | Thank you for your phone number information!', reply_markup=keyboard)

        if message.contact.phone_number in config.authorized_numbers:
            bot.send_message(message.chat.id, 'Ваш номер телефона в списке авторизованных пользователей | Your phone number is in an authorised list', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'Ваш номер телефона не в списке авторизованных пользователей! Обратитесь к администратору системы. | Your phone number is NOT in an authorised list', reply_markup=keyboard)



@bot.message_handler(commands=['check']) #user can run this by sending the "/check" command to the bot
def check(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Подтвердить|confirm", callback_data='good')
    item2 = types.InlineKeyboardButton("Отмена|Cancel", callback_data='bad')
    markup.add(item1, item2)
    bot.send_message(config.chatid, "Вам необходимо подтвердить выполнение действия!|Please confirm the action!",reply_markup=markup)
        
@bot.callback_query_handler(func=lambda call: True) #When a user pressed the button this part of the code handle the reply
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Действие было подтверждено| Confirmed')
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Действие было отменено| Canceled')
# remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вам необходимо подтвердить выполнение действия!|Please confirm the action!",reply_markup=None)


@bot.message_handler(content_types=['text']) #Reply on any tezt to the bot
def send_text(message):
    if message.text.lower() is not None:
        bot.send_message(message.chat.id, 'Sorry, I am not a super clever bot and not able to keep the conversation going.')

bot.polling()



#@bot.message_handler(commands=['number']) #Объявили ветку для работы по команде <strong>number</strong>
#def phone(message):
#    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру
#    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) #Указываем название кнопки, которая появится у пользователя
#    keyboard.add(button_phone) #Добавляем эту кнопку
#    bot.send_message(message.chat.id, 'Предоставить омер телефона', reply_markup=keyboard) #Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)
    
