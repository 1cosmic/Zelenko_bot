from aiogram import  types

button_text = {
    "go_to_game": "Начинаем!",

    "name_yes": "Да!",
    "name_no": "Нет, повторить",

    "reg_yes": "Да",
    "reg_no": "Нет",
}
# Комплект кнопок для ответа пользователя
buttons_of_regs = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    types.KeyboardButton(text=button_text["reg_yes"]),
    types.KeyboardButton(text=button_text["reg_no"])
)

# Кнопка старта прохождения игры.
button_of_start = types.InlineKeyboardMarkup(resize_keyboard=True)
button_of_start.add(
    types.InlineKeyboardButton(text=button_text["go_to_game"], callback_data="!reg"))

# Клавиатура старта прохождения игры.
key_of_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_of_start.add(
    types.KeyboardButton(text=button_text["go_to_game"], callback_data="!reg"))



# Словарь всех кнопок.
Buttons = {
    "start": button_of_start,
    "regs": buttons_of_regs,
    "key_start": key_of_start,
}