import config

from project.users import User
from project.utils import States
from project.buttons import Buttons
from project.messages import Messages

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from asyncio import sleep



async def q_Animals(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_China(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Wing(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Light(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Shell(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Case(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Iron(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Planet(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Morze(self, quest, user, dp):
    """
    тип квеста: 2 (азбука морзе, шифрование имени пользователя и его последующее сравнение с ответом)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Draw(self, quest, user, dp):
    """
    Тип квеста: 3 (анализ типа сообщения пользователя, проверка на Image)

    :param user: объект типа User
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


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

    # Заводим список пользователей, проходящих сейчас квесты параллельно.
    list_user = {}

    async def register(id, username):

        pre_register_user.remove(id)

        state = dispatcher.current_state(user=id)
        list_user[id] = User(id, username, None)

        await state.set_state(States.REGISTER[0])
        await tg_bot.send_message(id, Messages['reg_name'], reply_markup=types.ReplyKeyboardRemove())


    # Заводим список квестов, свободных для прохождения.
    free_quests = []


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
        await msg.reply("По идее, сейчас я тебя перенаправлю в другую комнату. Ожидай.",
                  reply_markup=types.ReplyKeyboardRemove())

        # TODO: Написать алгоритм выборки свободного квеста по приоритету.
        pass


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
            await state.set_state(States.GO_TO_NEXT[0])

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