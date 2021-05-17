import discord
import os
import constants

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
  channel = message.channel
  if message.author == client.user:
    return

	#timer message
	#command is ast. 
	#a-Alfonso. s-seconds flag. t-timer. ' ' - to separate it from time constant
  if msg.startswith('$at '):
    x = message.split(" ")
    name = x[1]
    print(name)
    time = x[2].split(":")
    hour = time[0]
    minute = time[1]
    second = time[2]
    print("hour: " +hour + " minute: " + minute + " second: " + second)
    sec = msg[5:] #gets the number of secs
    await channel.send('timer registered for ' + sec + "seconds")

  #instruction commands
  elif msg.startswith('$ahelp'):
	  await channel.send(constants.instructions)
  elif msg.startswith('$atimers'):
    await channel.send(constants.timers)
  elif msg.startswith('$areminders'):
    await channel.send(constants.reminders)
  elif msg.startswith('$apolls'):
    await channel.send(constants.polls)

client.run(os.environ['TOKEN'])