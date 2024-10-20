from pyrogram.types import Message

def type_message(message: Message):
    return str(message.chat.type).split(".")[1]