import telebot
import webbrowser
import random

bot =telebot.TeleBot('6956450835:AAH9JDZkYvehFJJdRm-uvkRze477NB4B3q8')


@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.chat.id, 'https://youtu.be/hNxzv3MvZUE', parse_mode='html')
    #webbrowser.open('https://youtu.be/hNxzv3MvZUE')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name} {message.from_user.last_name}, Меня зовут Freddy! я умею присылать мативационные фразы, а также ссылки на классные видео, согласен это мало но я пока нахожусь на раний стадии тестирования')

@bot.message_handler(commands=['Atlantis'])
def site(message):
    bot.send_message(message.chat.id, 'https://youtu.be/eEPTC5mJSlI?si=f_jHwEaov2zCtXTz', parse_mode='html')
    bot.send_message(message.chat.id, f' это довольна класная музычка! мне кажется она поднимит тебе настроение.')
   # webbrowser.open('https://youtu.be/wr8QyE0MepE?si=w3fpUVqvcev1Nth3')


@bot.message_handler(commands=[ 'help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information.Ожидайте информацию. Ну или нет хз когда напишут руководство.</u></em>', parse_mode='html')
#bot.polling() 
    
@bot.message_handler(commands=['violation'])
def violation(message):
 bot.send_message(message.chat.id, f'🚨🚨🚨 Нарушение протоколов безопасности!{message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler()
def info(message):
    if message.text.lower()== ('привет'):
       bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name} {message.from_user.last_name}')
   
    elif message.text.lower() =='id':
        bot.reply_to(message, f'ID:{message.from_user.id}')

    elif message.text.lower() == '/motivation':
        motivations = [' Люди, которые достаточно сумасшедшие, чтобы думать, что они могут изменить мир — это те, кто действительно на это способен. ', 
        ' В любой момент у нас есть два варианта: сделать шаг вперёд к росту или вернуться в безопасное место.',  
        ' Изменения – закон жизни. И те, кто смотрит только в прошлое или только на настоящее, бесспорно, пропустят будущее.', 
        ' Секрет перемен состоит в том, чтобы сосредоточиться на создании нового, а не на борьбе со старым.',
        ' Когда все двигаются вперёд совместными усилиями, успех приходит сам собой',
        'По отдельности мы одна капля. Вместе мы океан',
        'То, что ты ищешь, тоже ищет тебя',
        'Есть два способа прожить жизнь: или так, будто чудес не бывает, или так, будто вся жизнь — чудо',
        'Самый распространенный способ, которым люди отказываются от своей власти, — это думать, что у них ее нет',
        'Хм, мне кажется я допустил ошибку в коде...' 
        'Возможности не приходят сами — вы создаете их', 
        'Чем больше сила, тем больше ответственость.',
        'Даже если вы проходите через ад, продолжайте идти.',
        'Не бойтесь пожертвовать хорошим ради еще лучшего.',
        'Есть два вида людей, которые будут вам говорить, что вы не сможете чего-то добиться: те, кто сами боятся пробовать, и те, кто боятся, что у вас получится.',
        'Бездействие порождает беспокойство и страх. Действие — уверенность и смелость. Если ты хочешь победить страх, не сиди дома и не думай об этом. Встань и действуй.',
        'Одна победа не ведет к успеху, в отличие от постоянного желания побеждать.',
        ' Совсем не важно, как ты ударишь, а важно, КАКОЙ ДЕРЖИШЬ УДАР.',
                
                        ]  # здесь можно добавить свои мотивирующие фразы
        random_motivation = random.choice(motivations)
        bot.reply_to(message, f'Вот тебе мотивация,  {message.from_user.first_name} {message.from_user.last_name}: {random_motivation}' )
 




bot.polling(none_stop=True)