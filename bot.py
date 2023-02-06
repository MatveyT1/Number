from main import bot, offset
from database import creating_database, insert_data_seen_users, get_seen_user

if __name__ == '__main__':
    while True:
        msg, user_id = bot.get_event()
        if msg == 'начать':
            bot.greeting(user_id)
            sex: int = 0
            bot.write_msg(user_id, 'Введи пол (1 - женский, 2 - мужской)')
            while True:
                msg, user_id = bot.get_event()
                try:
                    if msg == '1' or msg == '2':
                        sex: int = int(msg)
                    else:
                        raise ValueError
                except ValueError:
                    bot.write_msg(user_id, 'Введи корректный пол')
                else:
                    break
            age_from: int = 0
            bot.write_msg(user_id, 'Введи минимальный возраст')
            while True:
                msg, user_id = bot.get_event()
                try:
                    if int(msg) <= 0:
                        raise ValueError
                    else:
                        age_from = int(msg)
                except ValueError:
                    bot.write_msg(user_id, 'Введи корректный возраст')
                else:
                    break
            age_to: int = 0
            bot.write_msg(user_id, 'Введи максимальный возраст')
            while True:
                msg, user_id = bot.get_event()
                try:
                    if int(msg) <= 0 or int(msg) < age_from:
                        raise ValueError
                    else:
                        age_to = int(msg)
                except ValueError:
                    bot.write_msg(user_id, 'Введи корректный возраст')
                else:
                    break
            bot.write_msg(user_id, 'Введи город')
            msg, user_id = bot.get_event()
            city: str = msg
            creating_database()
            bot.search_users(sex, age_from, age_to, city)
            bot.start_searching(user_id, offset)
            insert_data_seen_users(bot.person_id(offset))
            bot.write_msg(user_id, 'Жми на кнопку "Далее", чтобы продолжить поиск.\n'
                                      'Чтобы поставить лайк фото, напиши номер фото.\n'
                                      'Чтобы закончить поиск, напиши "пока".')
        elif msg == 'далее':
            for i in range(0, 1000):
                offset += 1
                bot.start_searching(user_id, offset)
                insert_data_seen_users(bot.person_id(offset))
                bot.write_msg(user_id, 'Жми на кнопку "Далее", чтобы продолжить поиск.\n'
                                      'Чтобы поставить лайк фото,напиши номер фото.\n'
                                      'Чтобы закончить поиск, напиши "пока".')
                break
        elif msg == '1' or msg == '2' or msg == '3':
            bot.like_photo(get_seen_user(), user_id, msg)
        elif msg == 'пока':
            bot.write_msg(user_id, "Пока((")
        else:
            bot.greeting(user_id)
