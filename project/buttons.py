from aiogram import  types

button_text = {
    "go_to_game": "Начинаем!",
    "name_yes": "Да!",
    "name_no": "Нет, повторить"
}
# Комплект кнопок для ответа пользователя
buttons_of_regs = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    types.KeyboardButton(text=button_text["name_yes"], callback_data="reg_yes"),
    types.KeyboardButton(text=button_text["name_no"], callback_data="reg_no")
)

# Кнопка старта прохождения игры.
button_of_start = types.InlineKeyboardMarkup(resize_keyboard=True)
button_of_start.add(
    types.InlineKeyboardButton(text=button_text["go_to_game"], callback_data="/reg"))



# Словарь всех кнопок.
Buttons = {
    "start": button_of_start,
    "regs": buttons_of_regs
}