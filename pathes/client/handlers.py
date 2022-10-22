from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime
from loader import dp, bot, qiwi
from . import buttons as btns
from . import functions as func
from . import states as st
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db, cfg

@dp.message_handler(commands=['start'], state='*')
async def startCommand(message: types.Message, state: FSMContext):
    await state.reset_state()
    user = await db.getUser(message.from_user.id)
    if not(user):
        await db.newUser(message.from_user.id, message.from_user.first_name, message.from_user.username)
    await message.answer(
        f'<b>💎 Добро пожаловать в умную ферму киви кошельков\
        \n\n- Моментальные выводы\
        \n- Настройки выводов\
        \n- Вывод на киви / Карту\
        \n- Бесплатный доступ\
        \n- Логирование баланса\
        \n- Уведомления о выводах\
        \n\n🛎 Комиссия фермы</b> - <code>{cfg.commision}</code>%',
        parse_mode='html',
        reply_markup = await btns.start()
    )
    await message.answer(f'<b>Держи меню</b>', parse_mode='html', reply_markup = btns.mainkb)

@dp.message_handler(text=['🎛 Меню'], state='*')
async def menuKey(message: types.Message, state: FSMContext):
    await state.reset_state()
    user = await db.getUser(message.from_user.id)
    balance = await db.getBalanceTokens(message.from_user.id)
    await message.answer(
        f'<b>⚙️ Управление фермой токенов:</b>\
        \n\n<b>💰 Баланс:</b> <code>{round(balance, 2)}</code> <b>₽</b>\
        \n<b>🔑 Токенов:</b> <code>{user.tokensCount}</code>\
        \n\n<b>💷 Мин.вывод:</b> <code>{user.minOutput}.0</code> <b>₽</b>\
        \n<b>💳 Реквизиты для вывода:</b> <code>{user.requisites}</code>\
        \n<b>💣 Автоблокировка:</b> {await func.getColorStatus(user.autoBlock)}\
        \n<b>🔔 Уведомление:</b> {await func.getColorStatus(user.alertBalance)}',
        parse_mode='html',
        reply_markup = await btns.controlKeyboard(alertBalance = user.alertBalance, autoBlock = user.autoBlock)
    )

@dp.callback_query_handler(text='startUse', state='*')
async def startUsingMenu(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_text(
        '<b><i>🚀 Добро пожаловать</i></b>',
        parse_mode='html',
        reply_markup = await btns.main()
    )


@dp.callback_query_handler(text='user&profile', state='*')
async def getUserProfile(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    user = await db.getUser(call.from_user.id)
    balance = await db.getBalanceTokens(call.from_user.id)
    await call.message.edit_text(
        f'<b>👤 Информация о пользователе:</b>\
        \n\nID: <code>{call.from_user.id}</code>\
        \nДней в Боте: <b>{user.daysIn}</b>\
        \nРегистрация: <b>{user.regTime}</b>\
        \n\n📯 Активность в Боте:\
        \n\nВыводов: {user.logsCount} на {user.logsSum} <b>₽</b>\
        \nТокенов: <b>{user.tokensCount}</b>\
        \nБаланс всех токенов: <b>{round(balance, 2)}</b>', 
        parse_mode='html',
        reply_markup=await btns.backMain()
    )

@dp.callback_query_handler(text='user&stats', state='*')
async def getUserStats(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    user = await db.getUser(call.from_user.id)
    balance = await db.getBalanceTokens(call.from_user.id)
    await call.message.edit_text(
        f'<b>📊 Статистика фермы токенов:</b>\
        \n\nВыводов: <b>{user.logsCount}</b> на <b>{user.logsSum}₽</b>\
        \nСейчас токенов: <b>{user.tokensCount}</b>\
        \nТокенов с доступом: <b>{user.tokensCount}</b>\
        \nОбщий баланс токенов: <b>{round(balance, 2)}₽</b>\
        \nИнтервал проверки: <b>{cfg.sleepChecking} сек</b>', 
        parse_mode='html',
        reply_markup=await btns.backMain()
    )

@dp.callback_query_handler(text='user&info', state='*')
async def getInfo(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.edit_text(
        '<b>📑 Информация о боте:\
        \n\n- Моментальные выводы\
        \n- Вывода на киви / карту\
        \n- Блокировка после вывода\
        \n- Изменение баланса\
        \n- Уведомление о выводах\
        \n- И многое другое…</b>',
        parse_mode='html',
        reply_markup = await btns.infoKeyboard()
    )


@dp.callback_query_handler(text='user&control', state='*')
async def openUserControlPanel(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    user = await db.getUser(call.from_user.id)
    balance = await db.getBalanceTokens(call.from_user.id)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(
        f'<b>⚙️ Управление фермой токенов:</b>\
        \n\n<b>💰 Баланс:</b> <code>{round(balance, 2)}</code> <b>₽</b>\
        \n<b>🔑 Токенов:</b> <code>{user.tokensCount}</code>\
        \n\n<b>💷 Мин.вывод:</b> <code>{user.minOutput}.0</code> <b>₽</b>\
        \n<b>💳 Реквизиты для вывода:</b> <code>{user.requisites}</code>\
        \n<b>💣 Автоблокировка:</b> {await func.getColorStatus(user.autoBlock)}\
        \n<b>🔔 Уведомление:</b> {await func.getColorStatus(user.alertBalance)}',
        parse_mode='html',
        reply_markup = await btns.controlKeyboard(alertBalance = user.alertBalance, autoBlock = user.autoBlock)
    )

@dp.callback_query_handler(text_startswith='user&autoBlock&', state='*')
async def changeAutoBlockStatus(call: types.CallbackQuery, state: FSMContext):
    status = int(call.data.split('&')[2])
    await db.updateAutoBlock(call.from_user.id, status)
    await openUserControlPanel(call, state)


@dp.callback_query_handler(text_startswith='user&checkChangeBalance&', state='*')
async def changeAlertBalance(call: types.CallbackQuery, state: FSMContext):
    status = int(call.data.split('&')[2])
    await db.updateAlertBalance(call.from_user.id, status)
    await openUserControlPanel(call, state)

@dp.callback_query_handler(text='user&minOutput', state='*')
async def changeMinOutput(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await st.ChangeMinOutput.first()
    await call.message.edit_text(
        '<b>💷 Введите минимальную сумму:</b>', 
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.message_handler(state=st.ChangeMinOutput.waitSum)
async def setMinOutput(message: types.Message, state: FSMContext):
    try:
        sum = int(message.text)
        if sum < 10:
            await message.answer('<b>⚠️ Минимальная сумма автовывода: </b><code>10</code> <b>₽</b>', parse_mode='html', reply_markup = await btns.backControl())
            return()
        await state.reset_state()
        await db.updateMinOutput(message.from_user.id, sum)
        await message.answer(
            f'<b>💷 Минимальная сумма {sum}₽ установлена.</b>', 
            parse_mode='html',
            reply_markup = await btns.backControl()
        )
    except:
        await message.answer(
            '<b>⚠️ Произошла ошибка! \n\n🖇 Проверьте введенные данные и повторите попытку или вернитесь назад!</b>',
            parse_mode='html',
            reply_markup = await btns.backControl()
        )

@dp.callback_query_handler(text='user&requisites', state='*')
async def updateRequisites(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await st.UserChangeRequisites.first()
    await call.message.edit_text(
        '<b>📱Введите номер вашего кошелька в формате: \
        \n\nПример:</b> <code>79998887733</code>',
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.message_handler(state=st.UserChangeRequisites.waitRequisites)
async def setRequisites(message: types.Message, state: FSMContext):
    await state.reset_state()
    await db.updateRequisites(message.from_user.id, message.text)
    await message.answer(
        f'<b>☑️ Вывод на номер {message.text} включён!</b>',
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.callback_query_handler(text='user&addToken', state='*')
async def addNewToken(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await st.UploadTokens.first()
    await call.message.edit_text(
        '<b>🔑 Введите ключи (api) токены киви от 1 до 100 штук:\
        \n\n📜 Вводить можно каждый токен с новой</b>',
        parse_mode='html',
        reply_markup = await btns.receiveToken()
    )

@dp.message_handler(state=st.UploadTokens.waitTokens)
async def uploadTokens(message: types.Message, state: FSMContext):
    await state.reset_state()
    tokenList = message.text.splitlines()
    checkMessage = await message.answer('<b>⏳ Ожидайте идёт проверка токенов</b>', parse_mode='html')
    resultCheckTokens = await qiwi.uploadTokens(message.from_user.id, tokenList)
    await checkMessage.edit_text(
        f'<b>☑️ Успешно проверили токены</b>\
        \n\n<b>🔴 Нерабочих:</b> <code>{resultCheckTokens[1]}</code>\
        \n<b>🟢 Рабочих:</b> <code>{resultCheckTokens[0]}</code>\
        \n\n<b>💰 Общее количество денег: </b> <code>{resultCheckTokens[2]}</code> <b>₽</b>',
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.callback_query_handler(text='user&removeToken', state='*')
async def deleteToken(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await st.DeleteToken.first()
    await call.message.edit_text(
        '<b>❕ Отправьте токен который хотите удалить</b>',
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.message_handler(state=st.DeleteToken.waitToken)
async def deleteTokenDb(message: types.Message, state: FSMContext):
    await state.reset_state()
    await db.deleteToken(message.text)
    await message.answer(
        '<b>Токен удален!</b>',
        parse_mode='html',
        reply_markup = await btns.backControl()
    )

@dp.callback_query_handler(text='user&reset', state='*')
async def resetUser(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await db.clearUser(call.from_user.id)
    await call.answer('💡 Ваш аккаут сброшен')
    await openUserControlPanel(call, state)

@dp.callback_query_handler(text='user&tokens', state='*')
async def downloadTokens(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    file = open(f'data/cache/{call.from_user.id}.txt', 'w')
    strTokens = ''
    tokens = await db.getTokens(call.from_user.id)
    for token in tokens:
        strTokens+=f'{token.token}\n'
    file.write(strTokens)
    file.close()
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await call.message.answer_document(
            open(f'data/cache/{call.from_user.id}.txt', 'rb'),
            caption = 'Все токены',
            reply_markup = await btns.backControl()
        )
    except:
        await call.answer('💡 У вас нет токенов')