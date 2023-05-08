from random import randint

import config

from project.users import User
from project.utils import States
from project.buttons import Buttons
from project.messages import Messages
from project.skeleton_quest import create_quests, free_quests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from asyncio import sleep

flag_for_hints = 0

# =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
# =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
# Функции для внутренней работы программы (автоматизаторы).

# =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
# =-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=

if __name__ == "__main__":

    ### ==========

    # Для инициализации токена необходимо вбить его вместо config.TOKEN.
    # Однако, если вы хотите работать в команде и с git`ом, то лучше заведите файл config,
    # в котором создайте переменную TOKEN и присвойте ей значение вашего TG-бота.
    token = config.TOKEN

    ### ==========

    # Создаём асинхронного бота.
    tg_bot = Bot(token)
    dispatcher = Dispatcher(tg_bot, storage=MemoryStorage())
    dispatcher.middleware.setup(LoggingMiddleware())

    # Список пользователей, проходящих регистрацию.
    pre_register_user = []

    # Заводим список пользователей, зарегистрированных на прохождение.
    list_user = {}

    # Список пользователей, находящихся в очереди на прохождение (в случае пробок).
    await_user = []

    async def register(id, username):

        pre_register_user.remove(id)

        state = dispatcher.current_state(user=id)
        list_user[id] = User(id, username, None)

        await state.set_state(States.REGISTER[0])
        await tg_bot.send_message(id, Messages['reg_name'], reply_markup=types.ReplyKeyboardRemove())


    # Создаём список квестов для прохождения.
    list_quest = create_quests()


    async def go_to_next_quest(user=None, quest=None):

        if user == None:
            for u in await_user:
                if quest in u.required_quest:
                    index_q = list_quest.index(quest)
                    list_quest[index_q].occupy(u)

                    # ДОПИСАТЬ правильную установку состояний в зависимости от квеста.

                    await dispatcher.current_state(user=u).set_state(States.QUEST_MORZE[0])
                    await tg_bot.send_message(u, "Перенаправляю на следующий квест...")

        if quest == None:

            print("Пытаюсь обработать пользователя.")

            for q in free_quests(list_quest):
                print(q)
                if q in user.required_quests():
                    print("Прохожу основную логику работы.")

                    index_q = list_quest.index(q)
                    list_quest[index_q].occupy(user)

                    # ДОПИСАТЬ правильную установку состояний в зависимости от квеста.

                    await dispatcher.current_state(user=user.chatId).set_state(States.QUEST_MORZE[0])
                    await tg_bot.send_message(user, "Перенаправляю на следующий квест...")


    # TODO: Написать функцию распрделения пользователей по комнатам.

    @dispatcher.message_handler(state='*', commands=['start'])
    async def start(message: types.Message):

        # TODO: Изменить приветствие, добавить медиа и т.п.
        id = message.from_user.id

        # Добавляем пользователя в очередь на регистрацию.
        if (id not in pre_register_user) and (id not in list_user.keys()):
            pre_register_user.append(id)

            # Чистим историю диалога, если человек вышел за границы наших возможностей и познал Дзен.
            # await tg_bot.delete_message(message.chat.id, message.message_id)

        # Приветствие.
        await message.answer(Messages['start'], reply_markup=Buttons['key_start'])
        await sleep(1)
        await tg_bot.send_message(id, "Тебя ждёт увлекательное приключение!", reply_markup=Buttons['start'])


    @dispatcher.message_handler(state=States.GO_TO_NEXT[0])
    async def run_next_quest(msg):
        """
        Функция распределения пользователей по комнатам-квестам.

        :param message:
        :return:
        """
        id = msg.from_user.id
        state = dispatcher.current_state(user=id)

        # Debug информация.
        await msg.answer(f"Квесты на прохождение:\n{list_user[id].required_quests()}")

        if list_user[id].is_free:
            if id not in await_user:

                await msg.answer("Сейчас проверим, свободны ли квесты?")

                if len(free_quests(list_quest)) > 0:
                    print("Пытаюсь перевести человека на квест...")
                    await go_to_next_quest(list_user[id])

                else:
                    await_user.append(id)
                    print("Погоди немного, сейчас освободится локация и я тебя проведу к ней.")

            # await tg_bot.send_message(id, "Сейчас я тебя отправлю на следующий квест. Приготовься!")
            # await_user.remove(id)
            #
            # await msg.answer("Пока все квесты заняты, подожди немного.")
            #
            # else:


        else:
            msg.reply("Ты успешно прошёл все комнаты! Красавчик, брат.")

        await msg.reply("По идее, сейчас я тебя перенаправлю на другой квест. Ожидай.",
                        reply_markup=types.ReplyKeyboardRemove())

        # TODO: Написать алгоритм выборки свободного квеста по приоритету.
        pass


    @dispatcher.message_handler(state="*", commands={"morze", "quiz_1", "quiz_2", "quiz_3", "quiz_4", "quiz_5",
                                                     "quiz_6", "quiz_7", "quiz_8"})
    async def start_quests(msg: types.Message):

        id = msg.from_user.id
        state = dispatcher.current_state(user=id)

        if msg.text == "/morze":
            await state.set_state(States.QUEST_MORZE[0])
            await tg_bot.send_message(id, Messages['question_morze'])

        if msg.text == "/quiz_1":
            await state.set_state(States.QUEST_QUIZ_1[0])
            await tg_bot.send_message(id, Messages['quiz_1'])

        if msg.text == "/quiz_2":
            await state.set_state(States.QUEST_QUIZ_2[0])
            await tg_bot.send_message(id, Messages['quiz_2'])

        if msg.text == "/quiz_3":
            await state.set_state(States.QUEST_QUIZ_3[0])
            await tg_bot.send_message(id, Messages['quiz_3'])

        if msg.text == "/quiz_4":
            await state.set_state(States.QUEST_QUIZ_4[0])
            await tg_bot.send_message(id, Messages['quiz_4'])

        if msg.text == "/quiz_5":
            await state.set_state(States.QUEST_QUIZ_5[0])
            await tg_bot.send_message(id, Messages['quiz_5'])

        if msg.text == "/quiz_6":
            await state.set_state(States.QUEST_QUIZ_6[0])
            await tg_bot.send_message(id, Messages['quiz_6'])

        if msg.text == "/quiz_7":
            await state.set_state(States.QUEST_QUIZ_7[0])
            await tg_bot.send_message(id, Messages['quiz_7'])

        if msg.text == "/quiz_8":
            await state.set_state(States.QUEST_QUIZ_8[0])
            await tg_bot.send_message(id, Messages['quiz_8'])


    @dispatcher.message_handler(state=States.QUEST_MORZE[0])
    async def q_Morze(msg: types.Message):

        id = msg.from_user.id
        code = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.',
                'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..',
                'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-',
                'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
                'щ': '--.-', 'ъ': '.--.-.', 'ь': '-..-', 'ы': '-.--', 'э': '..-..', 'ю': '..--',
                'я': '.-.-',
                }
        name = list_user[id].name
        coded = ''
        for char in name.lower():
            coded += code[char]

        my_str = msg.text
        my_str = my_str.replace('…', '...')
        my_str = my_str.replace('—', '--')

        if my_str != coded:
            t = ''
            if len(my_str) < len(coded):
                for i in range(len(coded)-len(my_str)):
                    my_str+='*'

            if len(my_str) > len(coded):
                my_str = my_str[:len(coded)]

            for i in range(len(coded)):
                if my_str[i] != coded[i]:
                    t+='*'
                else:
                    t+=coded[i]

            await tg_bot.send_message(id, text=f"Нет, что-то здесь не так. Попробуй еще раз. Звездочками обозначены места с ошибками.\n {t}")
            return
        else:
            state = dispatcher.current_state(user=msg.from_user.id)
            await tg_bot.send_message(id, text="Молодец! Все верно!\nКвест пройден!")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_1[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "3":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")

        else:
            flag_for_hints = randint(1, 2)
            if flag_for_hints == 0:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Обратите внимение на "
                                "Музу, "
                                "которая спряталась в углу шкафа")
                flag_for_hints = 1
            else:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: провести эксперемент "
                                "можно в "
                                "шкафу.")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_2[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "1675":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")
        else:
            await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка 1: Чтобы узнать,"
                            "кто и сколько проходит за час, необходимо подняться на чердак.")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_3[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "тигр":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")
        else:
            flag_for_hints = randint(1, 2)
            if flag_for_hints == 1:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Обратите внимание на "
                                "небольшие полки в углу стола.")
            else:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: ООбычно плёнка хранится в "
                                "маленьких цилиндрических ёмкостях. Попробуйте её найти.")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_4[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "лестница":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Это правильный ответ!")
            await msg.reply("Квест пройден!")
        else:
            flag_for_hints = randint(1, 2)
            if flag_for_hints == 1:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Чтобы отыскать нужную "
                                "ракушку, найдите стену с аналогиями на кухне.")
            else:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Если посмотреть на аналогии "
                                "архитектора, то можно заметить стрижа, по его образу люди создали летательные "
                                "аппараты. А что изображено на другой фотографии?")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_5[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "танграм":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")
        else:
            flag_for_hints = randint(1, 2)
            if flag_for_hints == 1:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Чтобы собрать древнюю "
                                "китайскую игру, необходимо вынуть все деревянные элементы из формы, "
                                "а затем расположить их таким образом, чтобы получилась фигура. ")
            else:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Три головоломки находятся "
                                "около входа в чулан.")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_6[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "2":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Это правильный ответ!")
            await msg.reply("Квест пройден!")
        else:
            flag_for_hints = randint(1, 2)
            if flag_for_hints == 1:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Чемоданы, с которыми "
                                "архитектор ездит в путешествия, хранятся в чулане.")
            else:
                await msg.reply("Нет, что-то здесь не так. Попробуй еще раз. Подсказка: Открывая каждый, попробуйте "
                                "найти, в каком чемодане чувствуется запах апельсинов. ")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_7[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "1":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")
        else:
            await msg.reply("Нет, что-то здесь не так. Попробуй еще раз.")


    @dispatcher.message_handler(state=States.QUEST_QUIZ_8[0])
    async def q_Quiz(msg: types.Message):
        id = msg.from_user.id
        if msg.text == "4":
            state = dispatcher.current_state(user=msg.from_user.id)
            await msg.reply("Молодец! Все верно!")
            await msg.reply("Квест пройден!")
        else:
            await msg.reply("Нет, что-то здесь не так. Попробуй еще раз.")


    @dispatcher.message_handler(commands=['quit'])
    async def quit_from_game(message):
        """
        Выход из игры.

        :param message:
        :return:
        """
        pass


    @dispatcher.message_handler(state=States.REGISTER[0])
    async def register_user(msg: types.Message):
        """
        Регистрация пользователей.

        :param msg:
        :return:
        """

        id = msg.from_user.id
        state = dispatcher.current_state(user=id)

        if msg.text == "Да" and list_user[id].name != None:
            await msg.reply("Отлично! Мы готовы начинать.")
            await state.reset_state()

            # Включить после написания готовой логики распределения по квестам.
            # await state.set_state(States.GO_TO_NEXT[0])

        elif msg.text == "Нет":
            await msg.answer(Messages['reg_name'])
            list_user[id].name = None

        else:
            list_user[id].name = msg.text

            await tg_bot.send_message(id, "Убедись, что твоё имя написано правильно.")
            await sleep(1.5)

            await msg.reply(f"Тебя зовут {list_user[id].name}, верно?", reply_markup=Buttons['regs'])


    @dispatcher.callback_query_handler(lambda c: c.data == "!reg")
    async def register_user_by_button(callback_query: types.CallbackQuery):
        """
        Активация регистрации пользователя: по кнопке.

        :param callback_query:
        :return:
        """

        id = callback_query.from_user.id
        username = callback_query.from_user.username

        if id in pre_register_user:
            await register(id, username)


    @dispatcher.message_handler()
    async def process_user_answer(msg: types.Message):
        """
        Обработчик различных сообщений при нулевом состоянии.

        :param msg:
        :return:
        """

        id = msg.from_user.id
        state = dispatcher.current_state(user=msg.from_user.id)

        if msg.from_user.id in pre_register_user:
            return await register(id, msg.from_user.username)

        await msg.reply("Для начала работы введи команду: /start")


    executor.start_polling(dispatcher)