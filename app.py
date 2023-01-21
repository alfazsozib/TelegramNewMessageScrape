from telethon.sync import TelegramClient,events

name = '' 
api_id = ''
api_hash = "" 
chat = ""

client = TelegramClient(name,api_id,api_hash)
@client.on(events.NewMessage(chats= chat))
async def my_event_handler(event):
    s = event.raw_text
    print(s)

client.start()
client.run_until_disconnected()





