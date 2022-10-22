from peewee import SqliteDatabase
from .setters import *
from .getters import *
from .models import Token


db = SqliteDatabase('data/database/database.db')
db.connect()
db.create_tables([Token])











# async def getUser(userId: int):
#     try:
#         user = User.get(User.userId == userId)
#     except User.DoesNotExist:
#         user = None
#     return(user)



# async def newUser(userId: int, firstName: str = None, userName: str = None, refCode: str = 0):
#     try:
#         User.create(
#             userId = userId,
#             firstName = firstName,
#             userName = userName,
#             refCode = refCode
#         )
#     except Exception as e:
#         print(e)
#     return()


# async def getAllUsers():
#     try:
#         users = User.select()
#         return(users)
#     except:
#         pass
#     return()


# async def usersCount():
#     try:
#         users = User.select().count()
#         return(users)
#     except:
#         pass
#     return()


# async def countRef(refCode: str):
#     try:
#         response = User.select().where(User.refCode == refCode).count()
#         return(response)
#     except:
#         pass
#     return()



# async def newChanel(name: str, url: str, chanelId: int):
#     try:
#         Chanel.create(
#             name = name,
#             url = url,
#             chanelId = chanelId
#         )
#     except:
#         pass
#     return()


# async def getChanels():
#     try:
#         chanels = Chanel.select()
#         return(chanels)
#     except:
#         pass
#     return()


# async def delChanel(id):
#     Chanel.delete().where(id==id).execute()
#     return()