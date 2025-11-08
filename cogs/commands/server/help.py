import discord
from discord.ext import commands
from datetime import timedelta
import re
import asyncio
from datetime import datetime




class Help(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot



    @commands.slash_command(description="Узнать о всех командах (Неактуально)")
    @commands.guild_only()
    async def help(self, ctx: discord.ApplicationContext):
        help_fields = [
                       discord.EmbedField(name="", value="</server:1258122135113699448> - Показывает информацию о данном сервере (создателя, участников, каналов и т.д.)", inline=False), 
                       discord.EmbedField(name="", value="</userinfo:1258783457438466170> - Показывает информацию о пользователе (если не выбран, то автор команды). Данная команда работает лучше на сервере!", inline=False), 
                       discord.EmbedField(name="", value="</угадай:1258122135113699446> - Мини-игра, где нужно угадать число в радиусе от 1 до 9999. Идея взята с сервера [**MiBrothers**](<https://discord.gg/mibrothers-941320640420532254>)", inline=False), 
                       discord.EmbedField(name="", value="</kick:1258122135113699443> - Исключает пользователя с сервера с возможностью возрата на него", inline=False), 
                       discord.EmbedField(name="", value="</ban:1258122135113699442> - Исключает пользователя с сервера без возможности возрата", inline=False), 
                       discord.EmbedField(name="", value="</mute:1258122135113699441> - Запрещает пользователю разговаривать в каналах (с помощью роли <@&1213444840810090507>)", inline=False), 
                       discord.EmbedField(name="", value="</download_messages:1258433384372371628> - Скачивает сообщения из канала в файл. **Данная команда скоро не будет доступна**", inline=False), 
                       discord.EmbedField(name="", value="</qr create:1258122135113699447> и </qr read:1258122135113699447> - 1. Создает QR код. 2. Читает QR код. Все просто, но с точки зрения кода это сложно...", inline=False),
                       discord.EmbedField(name="<:new_1:1258852540087275693><:new_2:1258852538787037316>", value="</8ball:1258845659448999966> - Выдает 20 случайных ответов на вопрос.")
                       ]
        btn = discord.ui.Button(label="Показать команду", style=discord.ButtonStyle.secondary)
        view = discord.ui.View(btn)
        async def btn_callback(interaction: discord.Interaction):
            embed = discord.Embed(title="Информация о всех командах бота (Неактуально)", description="В этом пункте вы узнаете о каждой команде (приватной или открытой) бота.", fields=help_fields, color=0xf0d826)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            btn.disabled = True
            btn.style = discord.ButtonStyle.green

        btn.callback = btn_callback
        em = discord.Embed(title="Данная команда устарела и скоро будет заменена новой версией!", color=discord.Color.dark_orange())
        await ctx.respond(embed=em, view=view)

def setup(bot):
    bot.add_cog(Help(bot))    