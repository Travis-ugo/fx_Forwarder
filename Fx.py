import logging
from telethon.sync import TelegramClient, events
from telethon import TelegramClient, events

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

api_id = 1652138
api_hash = 'b2f0d235e8f8d7f4d6a11a39058aef55'
bot_token  = '1251418314:AAGaPAc7pcpKWzluP-PYYhGk9LbcSMtbcCM'

client = TelegramClient('TravisTon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    txt = event.message.message
    id = event.chat_id
    print(txt)
    await client.send_message(-425803138, txt)


client.start()
client.run_until_disconnected()
