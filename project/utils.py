from aiogram.utils.helper import Helper, HelperMode, ListItem




class States(Helper):
    mode = HelperMode.snake_case

    REGISTER = ListItem()
    QUEST_MORZE = ListItem()
    Q_OUIZ_1 = ListItem()