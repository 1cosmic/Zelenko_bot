class User:
    def __init__(self, chatId, username, name):
        self.chatId = chatId  # id-чата
        self.username = username  # никнейм в телеграме
        self.name = name  # имя человека при регистрации

        self.__required_quests = list(range(1, 13))  # список квестов для прохождения

    def is_free(self):
        """
        Проверяет, остались ли ещё квесты для прохождения.
        """

        if len(self.__required_quests) == 0:
            return False

        else:
            return True

    def pop_quest(self, id):
        """
        Удаляет квест чей id - в списке оставшихся для прохождения.

        :param id: int, номер квеста
        :return: True
        """

        # Удаляем данный квест из списка.
        self.__required_quests.remove(id)

        return True




class Users_List():

    def __init__(self):
        self.__list_user = []
        self.__max_in_game = 8

    def addUser(self, user):
        if self.__max_in_game <= 8:
            self.__list_user.append(user)
            return True

        else:
            print("WARNING! \nMax user in game!")
            return False

    def removeUser(self, user):
        self.__list_user.remove(user)


    def getCountUsers(self):
        return len(self.__list_user)


    def getUsers(self):
        return self.__list_user


class Users_In_Game(Users_List):
    pass

class Users_Wait_Game(Users_List):
    pass