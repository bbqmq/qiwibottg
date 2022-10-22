from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from . import functions as func

mainkb = ReplyKeyboardMarkup(resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton(text="🎛 Меню")
		]
	]
)

async def start():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('📜 Информация', url='https://t.me/bbbqmq_govnocoder'),
        InlineKeyboardButton('📑 Правила', url='telegra.ph/Osnovnye-pravila---QiwiGrabber-RoBot-02-23'),
        InlineKeyboardButton('☑️ Начать пользоваться', callback_data='startUse')
    )
    return(keyboard)


async def main():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('⚙️ Управление', callback_data='user&control'),
        InlineKeyboardButton('📊 Статистика', callback_data='user&stats'),
        InlineKeyboardButton('👤 Профиль', callback_data='user&profile'),
        InlineKeyboardButton('📖 Информация', callback_data='user&info')
        )
    return(keyboard)


async def backMain():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('◀️ Назад', callback_data='startUse')
    )
    return(keyboard)


async def infoKeyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('📜 Инструкция', url='t.me/+lGVet0vQQctmYzRi'),
        InlineKeyboardButton('📑 Правила', url='telegra.ph/Osnovnye-pravila---QiwiGrabber-RoBot-02-23'),
        InlineKeyboardButton('👤 Администратор', url='t.me/bbbqmq_govnocoder')
    )
    keyboard.row(InlineKeyboardButton('◀️ Назад', callback_data='startUse'))
    return(keyboard)


async def controlKeyboard(alertBalance: int, autoBlock: int):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('➕ Добавить', callback_data='user&addToken'),
        InlineKeyboardButton('➖ Удалить', callback_data='user&removeToken')
    )

    keyboard.row(InlineKeyboardButton(
        text=f'💣 Автоблокировка {await func.getColorStatus(autoBlock)}', 
        callback_data=f'user&autoBlock&{await func.changeBool(autoBlock)}')
    )

    keyboard.row(InlineKeyboardButton(
        text=f'🔔 Уведомления {await func.getColorStatus(alertBalance)}', 
        callback_data=f'user&checkChangeBalance&{await func.changeBool(alertBalance)}')
    )

    keyboard.add(
        InlineKeyboardButton('💷 Мин.Вывод', callback_data='user&minOutput'),
        InlineKeyboardButton('💳 Реквизиты', callback_data='user&requisites'),
        InlineKeyboardButton('📑 Токены', callback_data='user&tokens'),
        InlineKeyboardButton('🔄 Сбросить', callback_data='user&reset')
    )
    
    keyboard.row(InlineKeyboardButton('◀️ Назад', callback_data='startUse'))
    return(keyboard)


async def backControl():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton('◀️ Вернуться', callback_data='user&control')
    )
    return(keyboard)


async def receiveToken():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton('🔑 Получить токен', url='https://qiwi.com/api'))
    return(keyboard)
