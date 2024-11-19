# Способы вызова функции

flag = False


def comp(adr):
    global flag

    if '@' in adr and '.ru' in adr[-3:] or '.com' in adr[-4:] or '.net' in adr[-4:]:
        flag = True

    else:
        flag = False

    return flag


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if comp(recipient) and comp(sender):

        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')

        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

    if not flag:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
