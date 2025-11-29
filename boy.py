import telebot
from config import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import *
bot = telebot.TeleBot(TOKEN)


def markup_for_welcome():
    markup = InlineKeyboardMarkup(row_width=2)
    itembtn1 = InlineKeyboardButton('выдать список професий',callback_data="m1a1")
    itembtn2 = InlineKeyboardButton('дать наводящие вопросы',callback_data="m1a2")
    itembtn3 = InlineKeyboardButton('выбирете професстю с которой хотите свезать жизнь',callback_data="m1a3")
    itembtn4 = InlineKeyboardButton('посмотреть топ профессий что выбирают',callback_data="m1a4")
    markup.add(itembtn1, itembtn2,itembtn3, itembtn4)
    return markup

def markup_professions():
    markup = InlineKeyboardMarkup(row_width=2)
    itembtn1 = InlineKeyboardButton('врач',callback_data='doctor')
    itembtn2 = InlineKeyboardButton('архитектор',callback_data='architect')
    itembtn3 = InlineKeyboardButton('прогрмаммист',callback_data='programmer')
    itembtn4 = InlineKeyboardButton('учитель',callback_data='teacher')
    itembtn5 = InlineKeyboardButton('дизайнер',callback_data='designer')
    itembtn6 = InlineKeyboardButton('инженер',callback_data='engineer')
    itembtn7 = InlineKeyboardButton('журналист',callback_data='journalist')
    itembtn8 = InlineKeyboardButton('юрист',callback_data='lawyer')
    itembtn9 = InlineKeyboardButton('предприниматель',callback_data='entrepreneur')
    itembtn10 = InlineKeyboardButton('Биотехнолог',callback_data='biotechnologist')
    itembtn11 = InlineKeyboardButton('ювелир',callback_data='jeweler')
    back = InlineKeyboardButton('назад',callback_data='back_to_main')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,itembtn11, back)
    return markup




def qestion_markup():
    markup = InlineKeyboardMarkup(row_width=2)
    itembtn1 = InlineKeyboardButton('высокая зарплата',callback_data='big_salary')
    itembtn2 = InlineKeyboardButton('легкость в обучении',callback_data='easy_learning')
    itembtn3 = InlineKeyboardButton('возможность удаленки',callback_data='remote_work')
    itembtn4 = InlineKeyboardButton('творчиство',callback_data='creativity')
    itembtn5 = InlineKeyboardButton('востребовоность профессии',callback_data='demanded_profession')
    itembtn6 = InlineKeyboardButton('гуманитарные специальности',callback_data='humanities')
    itembtn7 = InlineKeyboardButton('крапотливая работа',callback_data='meticulous_work')
    back = InlineKeyboardButton('назад',callback_data='back_to_main')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7,back)
    return markup





@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "я бот который поможет тебе выбрать професию?", reply_markup=markup_for_welcome())



@bot.message_handler(commands=['profesion'])
def send_profesion(message):
    bot.reply_to(message, "выбери професию чтобы узнать о ней подробнее:", reply_markup=markup_professions())


mode = 'text'
@bot.callback_query_handler(func=lambda call: call.data)
def callback_handler(call):
    global mode
    def change(text):
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            reply_markup=markup_for_welcome()
            )

    if call.data == "back_to_main":
        mode = 'text'
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="я бот который поможет тебе выбрать професию?",
            reply_markup=markup_for_welcome()
            )
        return
    elif call.data == "m1a1":
        mode = 'text'
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="список професий(в будушем мы их увеличем не забывайте нас):",
            reply_markup=markup_professions()
            )
        return
    elif call.data == "m1a2":
        mode = 'text'
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="выбири что для тебя более важно(в будушем мы их увеличем не забывайте нас):",
            reply_markup=qestion_markup()
            )
        return
    elif call.data == "m1a3":
        mode = 'choose_profession'
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="выберите какую-то:",
            reply_markup=markup_professions()
            )
        return
    elif call.data == "m1a4":
        top = top_professions('databas.db')
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"топ профессий что выбирают:{top}",
            )
        return
    elif call.data == "doctor":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "если вы думаете связать свою жизнь с медициной, то вам необходимы хорошие знания по биологии и химии. будет очень трудное и долгое обучение.Большая ответственность за жизни и здоровье людей.Стресс и эмоциональное давление — сложные ситуации, пациенты, тяжёлые случаи.Непростой график — дежурства, ночные смены, иногда мало свободного времени.Иногда невысокая зарплата на стартe. стоит идти на этот путь только если есть истинная любовь к медицине и желание помогать людям.")
        elif mode == 'choose_profession':
            plus_doctor('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "architect":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "если у вас есть идея идти на архитектора только для того чтобы созадвать красивые здания то вы ошибаетесь. творчиская часть в меньшинстве перед матиматической и логической, но она есть. обучение будет довольно трудным с постояными проектами. также вы будете ответственным за целостность здания и людей. конкуренция в этой сфере небольшая, если учились усердно — работу найти можно быстро.")
        elif mode == 'choose_profession':
            plus_architect('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "programmer":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "профессия программиста подходит людям с аналитическим складом ума, которые любят решать задачи и разбираться в сложных системах. обучение может быть как долгим так и коротким. профессия постоянно развивается → нужно быть готовым к непрерывному обучению. высокая конкуренция для новичков, но высокая зарплата и частая удаленка.")
        elif mode == 'choose_profession':
            plus_programmer('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "teacher":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "профессия учителя требует терпения, коммуникабельности и умения объяснять материал доступно. работа эмоционально сложная и требует умения справляться с конфликтами. зарплата часто не соответствует нагрузке, но профессия делает огромный вклад в общество.")
        elif mode == 'choose_profession':
            plus_teacher('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "designer":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "профессия дизайнера требует творческого мышления, владения графическими программами и знаний основ дизайна. конкуренция высокая, особенно в начале. важно постоянно развивать навыки и портфолио.")
        elif mode == 'choose_profession':
            plus_designer('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "engineer":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "профессия инженера требует сильных знаний математики и физики. обучение долгое и сложное. много командной работы и ответственности за проекты. спрос на инженеров высокий.")
        elif mode == 'choose_profession':
            plus_engineer('databas.db')
            change("спасибо за участие в опросe.")
        return


    elif call.data == "journalist":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "журналисту нужно уметь писать, быстро реагировать на события и передавать информацию понятно. работа может быть стрессовой. конкуренция высокая, но профессия подходит тем, кто любит искать и рассказывать истории.")
        elif mode == 'choose_profession':
            plus_journalist('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "lawyer":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "для профессии юриста нужна отличная память, уверенность и хладнокровность. обучение теоретическое, с большим количеством законов. работа может быть стрессовой, особенно при судебных разбирательствах. высокая конкуренция, но высокие доходы при опыте.")
        elif mode == 'choose_profession':
            plus_lawyer('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "entrepreneur":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "предприниматель — это человек, который готов рисковать и брать ответственность. нет фиксированной зарплаты — всё зависит от идей и упорства. успех требует креативности, самоотдачи и анализа рынка.")
        elif mode == 'choose_profession':
            plus_entrepreneur('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "biotechnologist":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "биотехнолог — профессия для тех, кто любит биологию, химию и работу в лабораториях. обучение длительное. биотехнологи создают лекарства, агротехнологии и экологические решения. спрос на специалистов растёт.")
        elif mode == 'choose_profession':
            plus_biotechnologist('databas.db')
            change("спасибо за участие в опросе.")
        return


    elif call.data == "jeweler":
        if mode == 'text':
            bot.send_message(call.message.chat.id,
                            "ювелир должен иметь творческое мышление, внимание к деталям и терпение. работа кропотливая, но позволяет создавать уникальные украшения. конкуренция высокая, но профессия подходит тем, кто любит ручной труд и эстетику.")
        elif mode == 'choose_profession':
            plus_jeweler('databas.db')
            change("спасибо за участие в опросе.")
        return   
     
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, "Я пока реагирую только на кнопки и команды отправте /start или /help чтобы начать.")


if __name__ == '__main__':
    bot.polling()