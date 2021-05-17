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

	#TIMERS
	#command is at. 
	#a-Alfonso. t-timer. ' ' - to separate it from time constant
  elif msg.startswith('$at '):
    x = msg.split(" ")
    name = x[1]
    print(name)
    inTime = x[2].split(":")
    hour = inTime[0]
    minute = inTime[1]
    second = inTime[2]
   
    await channel.send("name: " + name + " hour: " +hour + " minute: " + minute + " second: " + second)

	#commad is ast 
	#s = seconds
  elif msg.startswith('$ast '):
	  x = msg.split(" ")
	  name = x[1]
	  t = x[2]
	  await channel.send("timer " + name + " set for " + t + " seconds")
  
  #commad is amt 
	#m = minutes
  elif msg.startswith('$amt '):
	  x = msg.split(" ")
	  name = x[1]
	  t = x[2]
	  await channel.send("timer " + name + " set for " + t + " minutes")

  #commad is aht 
	#h = hours
  elif msg.startswith('$aht '):
	  x = msg.split(" ")
	  name = x[1]
	  t = x[2]
	  await channel.send("timer " + name + " set for " + t + " hours")

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