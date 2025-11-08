import discord
import os
from dotenv import load_dotenv
import asyncio
import schedule

load_dotenv()

bot = discord.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def sending(ctx):
    
    await ctx.author.send("ы я буду спамить мб")
    print("отправил")

async def send_message():
    user = await bot.fetch_user(1089085012806209547)
    if user:
        await user.send("20:31, прибыл Годжо Сатору")

async def job():
    asyncio.run(await send_message())

@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')
    schedule.every().day.at("20:24").do(job)

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

bot.run(os.getenv("TOKEN"))