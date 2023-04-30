from aiogram.utils.helper import Helper, HelperMode, ListItem




class States(Helper):
    mode = HelperMode.snake_case

    REGISTER = ListItem()

    QUEST_MORZE = ListItem()
    QUEST_QUIZ = ListItem()

    GO_TO_NEXT = ListItem()

    # QUEST_MORZE = ListItem()
    # Q_QUIZ_1 = ListItem()
