#MTQ4ODAzOTc5NDM5NDI2NzY1OA.GAdchG.5Qta9sBqwLLQhAVThSEZBXIkJqlYOxmk3VNwko --- Bot token

#https://discord.com/oauth2/authorize?client_id=1488039794394267658&permissions=2048&integration_type=0&scope=bot --- Bot link

import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQ4ODAzOTc5NDM5NDI2NzY1OA.GAdchG.5Qta9sBqwLLQhAVThSEZBXIkJqlYOxmk3VNwko') # Replace with your own token.