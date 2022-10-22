from aiogram.dispatcher.filters.state import State, StatesGroup

class ChangeMinOutput(StatesGroup):
    waitSum = State()


class UserChangeRequisites(StatesGroup):
    waitRequisites = State()


class UploadTokens(StatesGroup):
    waitTokens = State()


class DeleteToken(StatesGroup):
    waitToken = State()