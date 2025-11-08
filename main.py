# ДАЛЕН ИДИ НАХУЙ
# * ДАЛЕН ИДИ НАХУЙ
# ! ДАЛЕН ИДИ НАХУЙ
# ? ДАЛЕН ИДИ НАХУЙ
# todo ДАЛЕН ИДИ НАХУЙ

import discord
from discord.ext import commands, tasks
import discord.gateway
from discord.gateway import DiscordWebSocket
from discord.utils import escape_markdown, escape_mentions
from discord.ui import View, Modal, InputText
from discord import SyncWebhook

import colorama

from captcha.image import ImageCaptcha

import random

import io

import os

from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from colorama import Fore, Style

from idenify import identify
DiscordWebSocket.identify = identify

import asyncio

import requests

os.system('cls' if os.name == 'nt' else 'clear')





bot = discord.Bot(command_prefix='.', intents=discord.Intents.all())




###
#? Эвенты
###
for filename in os.listdir("./cogs/events"): 
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.events.{filename[:-3]}")
        


###
#? Команды
###
for filename in os.listdir("./cogs/commands/"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.commands.{filename[:-3]}")

for filename in os.listdir("./cogs/commands/fun"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.commands.fun.{filename[:-3]}")
        
for filename in os.listdir("./cogs/commands/moderation"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.commands.moderation.{filename[:-3]}")

for filename in os.listdir("./cogs/commands/server"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.commands.server.{filename[:-3]}")


###
#? Тикеты
###
for filename in os.listdir("./cogs/tickets"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.tickets.{filename[:-3]}")

disabled = False
if disabled:
    print(f"{Fore.GREEN}{Style.BRIGHT}Команды{Style.NORMAL} загружены")      

if disabled:
    print(f"{Fore.CYAN}{Style.BRIGHT}Эвенты{Style.NORMAL} загружены {Style.RESET_ALL}{Fore.MAGENTA}")




from cogs.tickets.base import ticket_manager
from discord.ext import tasks
@tasks.loop(seconds=10) # Цикл будет выполняться каждые 10 секунд
async def update_message():
    channel = bot.get_channel(1213412606656651304) # Замените на ID вашего канала
    if channel is not None:
        message = await channel.fetch_message(1265345023885578251) # Замените на ID вашего сообщения
        if message is not None:
            embed = discord.Embed(color=0xf64646, 
                                image=discord.EmbedMedia(url="https://cdn.discordapp.com/attachments/1257431672572477583/1264536073938272316/M6FOXJi-2.gif?ex=669e3a7d&is=669ce8fd&hm=bac0df81d1e24b93c8549ccc6efc94bab1aa32dcea34a4e8737d1a5cede67215&"),
                                )
            
            p_c = bot.get_channel(1229516196379099286)
            pinned = len(p_c.channels)

            uc_c = bot.get_channel(1229516134093684856)
            unclaimed = len(uc_c.channels)

            embed.set_footer(text="ARZ Moderator", icon_url=bot.user.avatar.url)

            await message.edit(f"**Добро пожаловать! Вы попали в канал поддержки Discord сервера ARZ Squad『💻』! Выберите суть вашей проблемы и мы обязательно постараемся вам помочь!**\n\n> :pushpin: - **Количество обращений за всё время**: `{ticket_manager.load_ticket_counter()}`\n> ⚙ - **Необработанных модераторами**: `{unclaimed}`\n> :eyes: - **На рассмотрении**: `{pinned}`\n> :lock: - **Закрытых**: `{ticket_manager.load_closed_tickets()}`", embed=embed)


@bot.command(description="Отображает статистику пользователя")
async def stats(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, "Пользователь (упоминание или id)")):  # type: ignore
    await ctx.defer()
    # Получаем количество сообщений пользователя за все каналы
    message_count = 0
    for channel in ctx.guild.text_channels:
        try:
            # Получаем историю сообщений в канале
            async for message in channel.history(limit=None):
                if message.author == user:
                    message_count += 1
        except discord.Forbidden:
            # Если бот не имеет доступа к каналу, пропускаем его
            continue



    # Проверяем наличие VIP-ролей
    vip_roles = {
        "DIAMOND VIP": "🏆VIP",
        "BRONZE VIP": "🥉VIP",
        "SILVER VIP": "🥈VIP",
        "ADD VIP": "🥇VIP"
    }

    role_vip_value = "None"
    for role_name, emoji in vip_roles.items():
        if discord.utils.get(user.roles, name=role_name):
            role_vip_value = emoji
            break


    mod_roles = {
        "Модератор Discord Сервера": "Модератор",
        "Старший Модератор Discord сервера": "Старший Модератор",
        "Куратор Модерации Discord Сервера": "Куратор Модерации",
        "Главная Модерация Discord сервера": "Главная Модерация",
        "Тех. поддержка Discord сервера": "Тех. поддержка",
        "Руководитель Discord Модерации": "Руководитель Discord"



    }

    role_ds_value = "Пользователь"
    for role_name, display_value in mod_roles.items():
        if discord.utils.get(user.roles, name=role_name):
            role_ds_value = display_value
            break

    color_roles = {
        "Black": "Black",
        "Grey": "Grey",
        "Purple": "Purple",
        "Red": "Red",
        "Orange": "Orange",
        "Lime": "Lime",
        "Pink": "Pink",
        "Olive": "Olive",
        "Blue": "Blue",
        "Yellow": "Yellow",
        "Lilac": "Lilac",
        "Blue Sky": "Blue Sky",
        "Great Blue Green": "Great Blue Green",
    }

    color_roles_value = "None"
    for role_name, dispaly in color_roles.items():
        if discord.utils.get(user.roles, name=role_name):
            color_roles_value = dispaly
            break

    # Получаем общее время, проведенное в голосовых каналах (если нужно, добавьте сюда логику)

    embed = discord.Embed(title=f"Статистика пользователя - {user.name}",
                          thumbnail=user.avatar.url if user.avatar else user.default_avatar.url,
                          color=0x2182be,
                          timestamp=datetime.now())
    embed.add_field(name="💬 Сообщений", value=f"```{message_count}```", inline=False)
    embed.add_field(name="🛡️ Роль DS", value=f"{role_ds_value}", inline=False)
    embed.add_field(name="🎖️ VIP-Статус", value=f"```{role_vip_value}```", inline=False)
    embed.add_field(name="🎨 Цвет", value=f"```{color_roles_value}```")
    embed.set_footer(text=f"Id: {user.id}")
    
    await ctx.respond(embed=embed)
    
    

# Обработка нажатия кнопок модерации

keywords = [
    "*блять*", "*ебать*", "*нахуй*", "*долбаеб*", "*сука*", "*Слава Украине*", "*шлюха*", "*москаль*", "*укроп*",
    "*Слава России*", "*далбаеб*", "*блять*", "*сосать*", "*уебан*", "*хохол*", "*бандера*", "*пиздец*", "*пиздюк*",
    "*мать ебал*", "*безмамный*", "*член*", "*пизда*", "*хуй*", "*ZOV*", "*ЗОВ*", "*Зет*", "*Гойда*",
    "*мбам бам бам мы стреляем по хохлам*", "*Путин хуйло*", "*Зеленский клоун*", "*Слава Україні!*",
    "*слава украине*", "*негр*", "*негритянка*", "*Слава Україні*", "*Батько наш Бандера*", "*хахол*",
    "*Слава Українi*", "*долбаёб*", "*далбаёбина*", "*уебан*", "*poshel naxui*", "*idi naxui*",
    "*sosi*", "*сосо*", "*yeban*", "*yebok*", "*dalbaeb*", "*Slava ZSU*",
]

guild_ids = [
    1273643489451708552
]

#@bot.event
async def on_ready():

    while True:
        for guild_id in guild_ids:
            guild = bot.get_guild(guild_id)

            if guild is None:
                print(f"Сервер с ID {guild_id} не найден!")
                continue

            try:
                # Получаем количество правил на текущем сервере
                rules = await guild.fetch_auto_moderation_rules()
                rule_count = len(rules)

                # Если на сервере меньше 6 правил, создаем недостающие
                for i in range(6 - rule_count):
                    await guild.create_auto_moderation_rule(
                        name=f"Example Rule {rule_count + i + 1}",
                        event_type=discord.AutoModEventType.message_send,
                        trigger_type=discord.AutoModTriggerType.keyword,
                        trigger_metadata=discord.AutoModTriggerMetadata(keyword_filter=keywords),
                        actions=[
                            discord.AutoModAction(
                                action_type=discord.AutoModActionType.block_message,
                                metadata=discord.AutoModActionMetadata()
                            )
                        ],
                        enabled=True
                    )
                    print(f"{colorama.Fore.GREEN}Rule {rule_count + i + 1} created on server {guild_id}!{colorama.Style.NORMAL}")

                await asyncio.sleep(1)  # Ждем 1 секунду перед переходом к следующему серверу

            except Exception as e:
                print(f"An error occurred on server {guild_id}: {e}")

        await asyncio.sleep(3)  # Ждем 10 секунд перед следующей итерацией по всем серверам



async def send_log(message):
    data = {
        "content": message
    }
    requests.post("https://canary.discord.com/api/webhooks/1273210375235698740/LTBb_spv18n4zCt-9_afopJaapDAexx7tZABHx-PJtIkx6ejjnx-P34mDUnEjD_Dwn1s", json=data)


# def webhook_send():
#     with requests.Session() as session:
#         webbhook = SyncWebhook.from_url(url="https://canary.discord.com/api/webhooks/1273210375235698740/LTBb_spv18n4zCt-9_afopJaapDAexx7tZABHx-PJtIkx6ejjnx-P34mDUnEjD_Dwn1s", session=session)
#         webbhook.send(f"{webbhook.channel}\n{webbhook.name}\n{webbhook.source_channel}")


@bot.command(name='тест')
async def test_command(ctx):
    await send_log(f'{ctx.author.name} выполнил команду тест.')
    await ctx.send('Лог отправлен!')

update_message.start()


async def webhook_send(channel_id: int, name: str):
    # Получаем канал по ID
    channel = bot.get_channel(channel_id)
    if channel is None:
        print(f"Канал с ID {channel_id} не найден.")
        return
    
    # Создаем вебхук
    webhook = await channel.create_webhook(name=name)

    # Отправляем сообщение через вебхук
    await webhook.send("Это сообщение отправлено через вебхук!", username=name)

    # Удаляем вебхук после отправки сообщения
    await webhook.delete()


@bot.slash_command(name="captcha", description="Получить капчу")
async def captcha(ctx):
    # Генерируем текст капчи
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    
    # Создаем изображение капчи
    image_captcha = ImageCaptcha()
    captcha_image = image_captcha.generate(captcha_text)
    
    # Сохраняем изображение в байтовый поток
    byte_io = io.BytesIO()
    image_captcha.write(captcha_text, byte_io)
    byte_io.seek(0)

    # Создаем кнопку
    button = discord.ui.Button(label="Ввести", style=discord.ButtonStyle.primary)

    async def button_callback(interaction):
        modal = Modal(discord)
        await interaction.response.send_modal(f"Введите текст капчи: {captcha_text}")

    button.callback = button_callback

    # Создаем представление и добавляем кнопку
    view = View()
    view.add_item(button)

    # Отправляем сообщение с изображением капчи и кнопкой
    await ctx.respond(file=discord.File(byte_io, 'captcha.png'), view=view)



bot.run(os.getenv("TOKEN"))




































