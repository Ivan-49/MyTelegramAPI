from pyrogram.types import Message
from .sqlite_util import DataBase

db =  DataBase('databases/database.db')
def private_message(message:Message):
   ... 


def group_message(message:Message):
   ...


def bot_message(message:Message):
   ...