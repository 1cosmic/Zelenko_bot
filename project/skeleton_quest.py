
"""
Список всех квестов для их обработки, фильтрации и т.п. в основном коде.
"""

class Quest():
    def __init__(self, id_quest, name, type, priority):

        self.id_quest = id_quest
        self.name = name
        self.type = type
        self.priority = priority

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


def create_quests():
    """
    Создаём список квестов (для фильтрации по приоритетности).
    """

    res = list()

    # Заполняем список.
    res.append(Quest(1, "Азбука Морзе", "morze", 1))  # Азбука Морзе
    res.append(Quest(2, "Как называется животное на плёнке?", "quest", 3))
    #...

    return res


def free_quests(quests_list):
    return list(filter(lambda x: x.is_free(), quests_list))