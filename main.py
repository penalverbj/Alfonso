import discord
import os
import constants

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

	#timer message
	#command is ast. 
	#a-Alfonso. t-timer. ' ' - to separate it from time constant
  if message.content.startswith('$at '):
    await message.channel.send('timer registered')

  if message.content.startswith('$ahelp'):
	  await message.channel.send(constants.instructions)
  if message.content.startswith('$atimers'):
    await message.channel.send(constants.timers)

client.run(os.environ['TOKEN'])