from telethon import TelegramClient

api_id = 1652138
api_hash = 'b2f0d235e8f8d7f4d6a11a39058aef55'

Client = TelegramClient('TravisTon', api_id,api_hash)
async def main():
   me = await Client.get_me()
   print(me.stringify())
   
   username =  me.username
   print(username)
   print(me.phone)


   async for dialog in Client.iter_dialogs():
      print(dialog.name, 'has ID', dialog.id)

   await Client.send_message('me', 'Hello, myself!')   
  
   await Client.send_file('me', 'https://cnet1.cbsistatic.com/img/tNIpYQ55NFzQYz5N7veo2Dq03YU=/0x0:800x533/1600x900/2018/10/04/6fc72a94-e983-4c59-ac53-b3f13ebbb848/titans-robin-dick-grayson-warner-bros-b.jpg') 

   await Client.send_file('me','https://media.comicbook.com/2018/11/titans-dc-universe-comic-book-influence-1142487-640x320.jpeg')

   await Client.send_file('me', 'https://9jamo.com/wp-content/uploads/2019/10/Lovely_9jamo.com1_.mp3')

   await Client.send_file('homeless', 'https://d274.cdn-me.net/c.php?s=eNoBOADH%252F6UgvyXb4LsnKa9LeyFYEUhhhyoQO7TWNBtdgmps1yTH%252Bwm3vv31DjVLV9GO%252F9kxAxK3LAGbsGWExAgZSQ%253D%253D')

   await Client.send_message('homeless', 'welcome to the new group all. homeboys')

with Client:
  Client.loop.run_until_complete(main())

  @Client.invoke(ForwardMessagesRequest(
    from_peer=get_input_peer(-406847902),
    id=[-406847902],
    andom_id=[generate_random_long()],
    to_peer=get_input_peer(-406847902,  -425803138)