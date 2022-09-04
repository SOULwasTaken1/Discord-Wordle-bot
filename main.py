#import panel
import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive #use this only if you run this on replit
from discord_components import *
import random #to pick a random word
from discord.ext import commands
from Emojies import *
from Emojies import yellowEmoji, greenEmoji, grayEmoji #these are the discord emotes You make.

# important variable
key = "YOUR TOKEN HERE" #you can use .env instead too
bot = commands.Bot(command_prefix = '~')

def wordpick(): 
    with open("words.txt") as f: 
        words = f.read().splitlines() 
        return random.choice(words)

@bot.command()
async def wordle(ctx):
  pfp = ctx.author.avatar_url
  attempt = 0
  word = wordpick().upper()
  guessLeft = 5
  guess = ''
  emoji = ''
  embed1 = discord.Embed(title='Wordle',description='Your goal is to guess a 5-letter word. Goodluck. \n \n Do `~help wordle` to learn more.', color=0x631cba)
  embed1.set_thumbnail(url=pfp)
  await ctx.send(embed=embed1)
  while guess != word and guessLeft >= 0:
     
    guess1 = await bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    guess = guess1.content.upper()
    for letter in guess[0]:
      if guess[0] == word[0]:
        emoji += greenEmoji[guess[0]]
      elif guess[0] in word:
        emoji += yellowEmoji[guess[0]]
      elif guess[0] != word[0]:
        emoji += grayEmoji[guess[0]]   
      else:
        return
      
    for letter in guess[1]:
      if guess[1] == word[1]:
        emoji += greenEmoji[guess[1]]
      elif guess[1] in word:
        emoji += yellowEmoji[guess[1]]
      elif guess[1] != word[1]:
        emoji += grayEmoji[guess[1]]
      else:
        return
       
    for letter in guess[2]:
      if guess[2] == word[2]:
        emoji += greenEmoji[guess[2]]
      elif guess[2] in word:
        emoji += yellowEmoji[guess[2]]
      elif guess[2] != word[2]:
        emoji += grayEmoji[guess[2]]
      else:
        return

    for letter in guess[3]:
      if guess[3] == word[3]:
        emoji += greenEmoji[guess[3]]
      elif guess[3] in word:
        emoji += yellowEmoji[guess[3]]
      elif guess[3] != word[3]:
        emoji += grayEmoji[guess[3]]
      else:
        return
        
    for letter in guess[4]:
      if guess[4] == word[4]:
        emoji += greenEmoji[guess[4]]
      elif guess[4] in word:
        emoji += yellowEmoji[guess[4]]
      elif guess[4] != word[4]:
        emoji += grayEmoji[guess[4]]
      else:
        return
    attempt += 1
    embed2 = discord.Embed(title=f'',description=f'{emoji}\n **{guessLeft} Guess Left**', color=0x631cba)
    embed2.set_thumbnail(url=pfp)
    embed2.set_author(name=f"{ctx.author.name}", icon_url=pfp)
    await ctx.send(embed=embed2)
    guessLeft -= 1

    if guess == word:
      guessLeft -= 10
    emoji = ''
    guess = ''
    
  sendW = ''
  sendL = ''
  win = 'WON'
  lost = 'LOST'
  for letter in win:
    sendW += greenEmoji[letter]
  for letter in lost:
    sendL += yellowEmoji[letter]
  if guess1.content.upper() == word:
    embed = discord.Embed(title='Wordle',description=f"{sendW} \n You **Win**.You guessed the word in **{attempt}** tries", color=0x631cba)
    await ctx.send(embed=embed)
    
  elif guessLeft <= 0 and guess1.content.upper() != word:
    embed = discord.Embed(title='Wordle',description=f'{sendL}\nYou **Lost**. The word was **{word}**. Better luck next time', color=0x631cba)
    embed.set_thumbnail(url=pfp)
    await ctx.send(embed=embed)
  
keep_alive() #if you use replit
bot.run(key)
