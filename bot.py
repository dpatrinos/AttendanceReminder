
import os
import asyncio
import discord
from discord.ext.commands import Bot
from datetime import datetime
import time
from dotenv import load_dotenv

#initialize bot variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(command_prefix='$')

#ready up
@bot.event
async def on_ready():
    print("Logged in as",bot.user.name)

#command initiate
@bot.command(name="initiate")
async def initiate(ctx):
    await ctx.send('Attendance Reminders Initiated')
    count=0
    while True:
        current_time = datetime.now().time()
        day_of_week = datetime.today().weekday()
        if current_time.hour==13 and current_time.minute==12 and current_time.second==0 and not(day_of_week==6 or day_of_week==5):
            if count%2==0:
                await ctx.send("Top of the morning! Remember to record your attendance.")
                count=count+1
                await time.sleep(60)
            elif count%3==0:
                await ctx.send("Buenos Días! Recuerde registrar tu asistencia.")
                count=count+1
                await time.sleep(60)
            elif count%5==0:
                await ctx.send("Bonjour! N'oubliez pas d'enregistrer votre présence.")
                count=count+1
                await time.sleep(60)
            elif count%7==0:
                await ctx.send("Guten morgen! Denken Sie daran, Ihre Teilnahme aufzuzeichnen.")
                count=count+1
                await time.sleep(60)
            else:
                await ctx.send("Scrumptuous day! Remember to recrod your attendance.")
                count=count+1
                await time.sleep(60)
            
bot.run(TOKEN)