from aiogram.utils.helper import Helper, HelperMode, ListItem




class States(Helper):
    mode = HelperMode.snake_case

    REGISTER = ListItem()

    QUEST_MORZE = ListItem()
    QUEST_QUIZ_1 = ListItem()
    QUEST_QUIZ_2 = ListItem()
    QUEST_QUIZ_3 = ListItem()
    QUEST_QUIZ_4 = ListItem()
    QUEST_QUIZ_5 = ListItem()
    QUEST_QUIZ_6 = ListItem()
    QUEST_QUIZ_7 = ListItem()
    QUEST_QUIZ_8 = ListItem()


    GO_TO_NEXT = ListItem()

    # QUEST_MORZE = ListItem()
    # Q_QUIZ_1 = ListItem()
