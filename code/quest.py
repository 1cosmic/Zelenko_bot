"""
Данный объект отвечает за структуру квест-загадок.
Будет специальнвя функция-инициализатор, которая создает 6-9 квест-загадок в оператике.
Далее - ссылки на эти загадки будут использоваться в ваших функциях.

Приведённая структура является примером для вашего кода.
Опирайтесь на неё.

По существу, в вашу функцию будет передаваться объект класса Quest.
"""


class Quest():
    def __init__(self, id, type, priority, question, hints, answer, media):
        self.answer = answer  # хранит ответ пользователя
        self.id = id  # id вопроса
        self.type = type  # тип (один из трех: загадка, азбука-морзе, рисование)
        self.priority = priority  # приоритет

        self.question = question  # вопрос
        self.hints = hints  # список из 3х подсказок
        self.media = media  # медиа, если имеется

        self.__occupy_by_user = None  # занят пользователем = User()
        self.__free = True  # свободен ли для прохождения в настоящий момент


    def is_free(self):
        '''
        Если квест сейчас свободен - вернёт True.
        Иначе - False.
        '''

        return self.__free


    def occupy(self, user):
        """
        Занимает данный квест, если он свободен.
        """

        if self.__free == True:
            self.__free = False
            self.__occupy_by_user = user

            return True

        else:
            return False


    def free(self):
        '''
        Освобождает квест, если пользователь его прошёл.
        '''

        if self.__free == False:
            self.__free = True
            self.__occupy_by_user = None

            return True

        else:
            return False
