import os
import asyncio
import discord
from discord.ext import commands
from datetime import datetime
import time
from dotenv import load_dotenv
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from webdriver import driver
import urllib.request

#initialize bot and client variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
client = discord.Client()

#global variables
run = True

#ready up
@bot.event
async def on_ready():
    print("Logged in as",bot.user.name)
    ID = int(os.getenv('CHANNEL_ID'))
    channel = bot.get_channel(ID)
    
    while True:
        await asyncio.sleep(10)
        global run
        if run:
            current_time = datetime.now().time()
            day_of_week = datetime.today().weekday()
            if True:#current_time.hour==7 and current_time.minute==2 and not(day_of_week==6 or day_of_week==5):
                print("Time if statement true.")
                getQuote()
                file = discord.File("quote.png", filename="quote.png")
                await channel.send(file=file)
                os.remove("quote.png")
                num=random.randint(0,100)
                if num%2==0:
                    await channel.send("Top of the morning! Remember to record your attendance.")
                    await asyncio.sleep(60)
                elif num%3==0:
                    await channel.send("Buenos Días! Recuerde registrar tu asistencia.")
                    await asyncio.sleep(60)
                elif num%5==0:
                    await channel.send("Bonjour! N'oubliez pas d'enregistrer votre présence.")
                    await asyncio.sleep(60)
                elif num%7==0:
                    await channel.send("Guten morgen! Denken Sie daran, Ihre Teilnahme aufzuzeichnen.")
                    await asyncio.sleep(60)
                else:
                    await channel.send("Scrumptuous day! Remember to record your attendance.")
                    await asyncio.sleep(60)
            else:
                print("Time if statment false.")

@bot.command(name="pause")
async def pause(ctx):
    print("Pause command received.")
    await ctx.send("Attendance reminders paused. Use command \"$resume\" to unpause reminders.")
    global run
    run=False

@bot.command(name="resume")
async def resume(ctx):
    print("Resume command received.")
    await ctx.send("Attendance reminder resumed. Use command \"$pause\" to halt reminders.")
    global run
    run=True

@bot.command(name="hello-there")
async def helloThere(ctx):
    print("Kenobi command received.")
    file = discord.File("media/grievous.mp4", filename="grievous.mp4")
    await ctx.send(file=file)

@bot.command(name="hurt-feelings")
async def hurtFeelings(ctx):
    print("Feelings command received.")
    
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    author_id = ctx.message.author.id

    if author_id==int(os.getenv('EVAN')):
        sms_gateway = os.getenv('EVAN_E')

    elif author_id==int(os.getenv('ETHAN')):
        sms_gateway = os.getenv('ETHAN_E')
        
    elif author_id==int(os.getenv('TOBY')):
        sms_gateway = os.getenv('TOBY_E')

    elif author_id==int(os.getenv('TANUSH')):
        sms_gateway = os.getenv('TANUSH_E')

    elif author_id==int(os.getenv('CHRISTIAN')):
        sms_gateway = os.getenv('CHRISTIAN_E')

    else:
        sms_gateway = os.getenv('DEMETRI_E')

    smtp = "smtp.comcast.net"
    port = 587

    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,password)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "I'm watching you"
    body = "Don't screw with me."
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    await ctx.send("{} Check your email ( ͡° ͜ʖ ͡°)".format(ctx.message.author.mention))

@bot.command(name="i-am-sad")
async def sad(ctx):
    print('Sad command received.')

    num = random.randint(1,17)

    name_string = "media/dog" + str(num) + ".jpg"

    file = discord.File(name_string, filename="doggo.jpg")
    await ctx.send(file=file)
    await ctx.send("Here is a doggo for you.")

def getQuote():
    print("Fetching quote")
    email = os.getenv("MICRO_E")
    password = os.getenv("MICRO_P")
    main_driver = driver()
    main_driver.microsoftLogin(email, password)
    src = main_driver.getSrc()
    print(src)
    urllib.request.urlretrieve(src, "quote.png")
    

bot.run(TOKEN)