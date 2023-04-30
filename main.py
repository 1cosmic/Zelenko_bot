import config

from project.users import User
from project.utils import States
from project.buttons import Buttons
from project.messages import Messages

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware



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
    list_user = []

    # Заводим список квестов, свободных для прохождения.
    free_quests = []



    # TODO: Написать функцию распрделения пользователей по комнатам.

    # @dp.message_handler(state='*', commands=[''])
    # async def process_setstate_command(message: types.Message):
    #
    #     argument = message.get_args()
    #     state = dispatcher(user=message.from_user.id)
    #
    #     if not argument:
    #         await state.reset_state()
    #         return await message.reply(MESSAGES['state_reset'])
    #
    #     if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
    #         return await message.reply(MESSAGES['invalid_key'].format(key=argument))
    #
    #     await state.set_state(TestStates.all()[int(argument)])
    #     await message.reply(MESSAGES['state_change'], reply=False)



    @dispatcher.message_handler(commands=['start'])
    async def start(message: types.Message):

        # TODO: Изменить приветствие, добавить медиа и т.п.

        # Добавляем пользователя в очередь на регистрацию.
        if message.from_user.id not in pre_register_user:
            pre_register_user.append(message.from_user.id)

        # Приветствие.
        await message.reply(Messages['start'], reply_markup=Buttons['start'])


    @dispatcher.message_handler(commands=['next_quest'])
    async def run_next_quest(message):

        # TODO: Написать алгоритм выборки свободного квеста по приоритету.
        pass


    @dispatcher.message_handler(commands=['quit'])
    async def quit_from_game(message):
        pass


    @dispatcher.message_handler(state=States.REGISTER)
    async def register_user(msg: types.Message):
        await msg.reply("Continue of register user.")

    @dispatcher.message_handler()
    async def process_user_answer(msg: types.Message):

        state = dispatcher.current_state(user=msg.from_user.id)

        if msg.from_user.id in pre_register_user:
            await state.set_state(States.REGISTER)
            return await msg.reply("Приступаю к регистрации.")

        await msg.reply("В данный момент я не умею обрабатывать такое сообщение.")




    executor.start_polling(dispatcher)