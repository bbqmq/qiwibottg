from loader import db, bot



async def getColorStatus(status):
    statuses = {
        False: '🟥',
        True: '🟩'
    }
    return(statuses[status])


async def changeBool(value):
    values = {
        1: 0,
        0: 1
    }
    return(values[value])