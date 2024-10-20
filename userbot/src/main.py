from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from conf.config import API_ID, API_HASH
from utils.sqlite_util import DataBase
from utils.type_message import type_message
from utils.message import private_message, group_message, bot_message

client = Client("my_account", API_ID, API_HASH)
# bd = DataBase('database.db')


def all_messages(client: Client, message:Message):
    try:
        type = type_message(message)
        if type == 'PRIVATE':
            private_message(message)
        elif type == 'GROUP':
            group_message(message)
        elif type == 'BOT':
            bot_message(message)
        else:
            raise Exception('Тип сообщения не опознан')
    except Exception as e:
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(f'{e}\n')
            print(e)





if __name__ == "__main__":
    client.add_handler(MessageHandler(all_messages))
    while True:
        client.run()
            