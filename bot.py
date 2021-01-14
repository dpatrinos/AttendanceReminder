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
import cryptocompare

#initialize bot and client variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
client = discord.Client()

#global variables
run = True
evan = 1
ethan = 4
toby = 1
tanush = 1
johny = 0
demetri = 0
christian = 0

#ready up
@bot.event
async def on_ready():
    print("Logged in as",bot.user.name)
    ID1 = int(os.getenv('CHANNEL_ID_1'))
    ID2 = int(os.getenv('CHANNEL_ID_2'))
    channel1 = bot.get_channel(ID1)
    channel2 = bot.get_channel(ID2)

    price = 0
    past_prices = []
    while True:

        await asyncio.sleep(55)

        #get crypto price
        old_price = price
        update = cryptocompare.get_price('BTC',curr='USD')
        price = float(update.get('BTC').get('USD'))

        old_price_k = int(old_price/1000)
        price_k = int(price/1000)
        print("Old price: " + str(old_price_k) + "k")
        print("New price: " + str(price_k) + "k")

        #past price loop
        for i in range(price_k+1):
            if not(i in past_prices):
                past_prices.append(i)

        #check whether a new k was hit
        if (price_k>old_price_k and not(price_k in past_prices)):
            print("Shift from " + str(old_price_k) + "k to " + str(price_k) + "k")
            file = discord.File("media/krabs.png", filename="krabs.png")
            await channel2.send(file=file)
            await channel2.send("GIVE IT UP FOR " + str(price_k) + "K")

        #attendence reminding system
        global run
        if run:
            current_time = datetime.now().time()
            day_of_week = datetime.today().weekday()
            if current_time.hour==7 and current_time.minute==10 and not(day_of_week==6 or day_of_week==5):
                print("Time if statement true")
                
                #getQuote()
                #file = discord.File("quote.png", filename="quote.png")
                #await channel1.send(file=file)
                #os.remove("quote.png")

                num = random.randint(0,100)
                if num%2==0:
                    await channel1.send("Top of the morning! Remember to record your attendance.")
                    await asyncio.sleep(6)
                elif num%3==0:
                    await channel1.send("Buenos Días! Recuerde registrar tu asistencia.")
                    await asyncio.sleep(6)
                elif num%5==0:
                    await channel1.send("Bonjour! N'oubliez pas d'enregistrer votre présence.")
                    await asyncio.sleep(6)
                elif num%7==0:
                    await channel1.send("Guten morgen! Denken Sie daran, Ihre Teilnahme aufzuzeichnen.")
                    await asyncio.sleep(6)
                else:
                    await channel1.send("Scrumptuous day! Remember to record your attendance.")
                    await asyncio.sleep(6)
            else:
                print("Time if statment false")

@bot.command(name="pause")
async def pause(ctx):
    print("Pause command received")
    await ctx.send("Attendance reminders paused. Use command \"$resume\" to unpause reminders.")
    global run
    run=False

@bot.command(name="resume")
async def resume(ctx):
    print("Resume command received")
    await ctx.send("Attendance reminder resumed. Use command \"$pause\" to halt reminders.")
    global run
    run=True

@bot.command(name="hello-there")
async def helloThere(ctx):
    print("Kenobi command received")
    file = discord.File("media/grievous.mp4", filename="grievous.mp4")
    await ctx.send(file=file)

@bot.command(name="hurt-feelings")
async def hurtFeelings(ctx):
    print("Feelings command received")
    
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    author_id = ctx.message.author.id

    #determine message author and set gateway to their email
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

    #connect to Comcast servers
    smtp = "smtp.comcast.net"
    port = 587

    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,password)

    #write message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "I'm watching you"
    body = "Don't screw with me."
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    #send message
    server.sendmail(email, sms_gateway, sms)
    await ctx.send("{} Check your email ( ͡° ͜ʖ ͡°)".format(ctx.message.author.mention))

@bot.command(name="i-am-sad")
async def sad(ctx):
    print('Sad command received')

    num = random.randint(1,18)

    name_string = "media/dog" + str(num) + ".jpg"

    file = discord.File(name_string, filename="doggo.jpg")
    await ctx.send(file=file)
    await ctx.send("Here is a doggo for you.")

@bot.command(name="roast-me")
async def roast(ctx):
    print('Roast command received')

    author_id = ctx.message.author.id

    global evan
    global ethan
    global toby
    global tanush
    global johny
    global demetri
    global christian

    if author_id==int(os.getenv('EVAN')):
        if evan==0:
            await ctx.send("On behalf of your parents, I ask, are you gay?")
            evan+=1

        elif evan==1:
            await ctx.send("Your face looks like a door mat")
            evan+=1

        elif evan==2:
            await ctx.send("Maybe you'll program an AI to be your girlfriend one day")
            evan+=1
        
        elif evan==3:
            await ctx.send("Is your ass jealous of the amount of shit that comes out of your mouth.")
            evan+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")
        

    elif author_id==int(os.getenv('ETHAN')):
        if ethan==0:
            await ctx.send("Thunder thighs")
            ethan+=1
    
        elif ethan==1:
            await ctx.send("Imagine saying Adidas so stupidly")
            ethan+=1

        elif ethan==2:
            await ctx.send("Go eat some potatoes")
            ethan+=1
        
        elif ethan==3:
            await ctx.send("Gaelic minus the lic")
            ethan+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")
        
        
    elif author_id==int(os.getenv('TOBY')):
        if toby==0:
            await ctx.send("Side burns. Boom roasted")
            toby+=1

        elif toby==1:
            await ctx.send("Aerospace engineers are poor")
            toby+=1

        elif toby==2:
            await ctx.send("You are a libtard")
            toby+=1

        elif toby==3:
            await ctx.send("You're so pale that if you went out at night, you'd still manage to get sun burn")
            toby+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")

    elif author_id==int(os.getenv('TANUSH')):
        if tanush==0:
            await ctx.send("Your face looks like a melted Hershey's kiss")
            tanush+=1
    
        elif tanush==1:
            await ctx.send("Get a real job")
            tanush+=1

        elif tanush==2:
            await ctx.send("It's hard to roast something that malnutrition has already ravaged")
            tanush+=1

        elif tanush==3:
            await ctx.send("Stop calling me about my car's extended warranty")
            tanush+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")

    elif author_id==int(os.getenv('CHRISTIAN')):
        if christian==0:
            await ctx.send("We know that you wear shorts all year to compensate")
            christian+=1
    
        elif christian==1:
            await ctx.send("You look like Ron Weasley if he never exercised")
            christian+=1

        elif christian==2:
            await ctx.send("You drive a Subaru. Boom roasted.")
            christian+=1
        
        elif christian==3:
            await ctx.send("Everything about you says that you're the illegitimate child of Conan and a muppet")
            christian+=1
        
        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")

    elif author_id==int(os.getenv('JOHNY')):
        if johny==0:
            await ctx.send("You're Bulgarian. Boom roasted.")
            johny+=1
    
        elif johny==1:
            await ctx.send("No one like a socialist")
            johny+=1

        elif johny==2:
            await ctx.send("You're as greasy as Rem")
            johny+=1

        elif johny==3:
            await ctx.send("The trombone isn't the only thing you blow")
            johny+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")

    else:
        if demetri==0:
            await ctx.send("The Greek economy. Boom roasted")
            demetri+=1
    
        elif demetri==1:
            await ctx.send("John Stamos if John Stamos was gay")
            demetri+=1

        else:
            await ctx.send("Sorry! All out of roasts for you, for now at least")

@bot.command(name="mom")
async def mom(ctx, arg):
    print('Mom command received')

    if arg=="do":
        for i in range(0,10):
            await ctx.send("I did your mom")
    
    elif arg=="said":
        for i in range(0,10):
            await ctx.send("That's what your mom was saying")

    elif arg=="tanush":
        for i in range(0,10):
            await ctx.send("Tanush's mom")

    else:
        for i in range(0,10):
            await ctx.send("Your mother")

def getQuote():
    print("Fetching quote")
    email = os.getenv("MICRO_E")
    password = os.getenv("MICRO_P")
    
    main_driver = driver()
    main_driver.microsoftLogin(email, password)
    
    src = main_driver.getSrc()
    print(src)
    
    urllib.request.urlretrieve(src, "quote.png")
    main_driver.closeDriver()

bot.run(TOKEN)